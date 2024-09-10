import tensorflow.keras.backend as K
from tensorflow.keras.layers import concatenate

def xywh2minmax(xy, wh):
    xy_min = xy - (wh / 2)  # 중심좌표를==>xmin,ymin 로 변환
    xy_max = xy + (wh / 2)  # 중심좌표를==>xmax,ymax 로 변환

    return xy_min, xy_max


def iou(pred_mins, pred_maxes, true_mins, true_maxes):
    intersect_mins = K.maximum(pred_mins, true_mins)
    intersect_maxes = K.minimum(pred_maxes, true_maxes)
    intersect_wh = K.maximum(intersect_maxes - intersect_mins, 0.)
    intersect_areas = intersect_wh[..., 0] * intersect_wh[..., 1]

    pred_wh = pred_maxes - pred_mins
    true_wh = true_maxes - true_mins
    pred_areas = pred_wh[..., 0] * pred_wh[..., 1]
    true_areas = true_wh[..., 0] * true_wh[..., 1]

    union_areas = pred_areas + true_areas - intersect_areas
    iou_scores = intersect_areas / union_areas

    return iou_scores


def yolo_head(feats):
    # Dynamic implementation of conv dims for fully convolutional model.
    conv_dims = K.shape(feats)[1:3]  # assuming channels last
    # In YOLO the height index is the inner most iteration.
    conv_height_index = K.arange(0, stop=conv_dims[0])
    conv_width_index = K.arange(0, stop=conv_dims[1])
    conv_height_index = K.tile(conv_height_index, [conv_dims[1]])

    # TODO: Repeat_elements and tf.split doesn't support dynamic splits.
    # conv_width_index = K.repeat_elements(conv_width_index, conv_dims[1], axis=0)
    conv_width_index = K.tile(
        K.expand_dims(conv_width_index, 0), [conv_dims[0], 1])
    conv_width_index = K.flatten(K.transpose(conv_width_index))
    conv_index = K.transpose(K.stack([conv_height_index, conv_width_index]))
    conv_index = K.reshape(conv_index, [1, conv_dims[0], conv_dims[1], 1, 2])
    conv_index = K.cast(conv_index, K.dtype(feats))

    conv_dims = K.cast(K.reshape(conv_dims, [1, 1, 1, 1, 2]), K.dtype(feats))

    box_xy = (feats[..., :2] + conv_index) / conv_dims * 448
    box_wh = feats[..., 2:4] * 448

    return box_xy, box_wh


def yolo_loss(y_true, y_pred):
    # label 데이터 추출 분리
    label_class = y_true[..., 5:]  # ? * 7 * 7 * 20
    label_box = y_true[..., :4]  # ? * 7 * 7 * 4
    response_mask = y_true[..., 4]  # ? * 7 * 7
    response_mask = K.expand_dims(response_mask)  # ? * 7 * 7 * 1

    # 예측 데이터 추출 분리
    predict_class = y_pred[..., 10:]  # ? * 7 * 7 * 20
    predict_trust1 = y_pred[..., 4]  # ? * 7 * 7 * 1
    predict_trust2 = y_pred[..., 9]  # ? * 7 * 7 * 1
    # 이후 추론단계에서는 예측 box 2개 별
    # predict_trust1 * predict_class 과  predict_trust2 * predict_class
    # 로 NMS 수행
    predict_trust =  K.stack([predict_trust1, predict_trust2],axis=3)

    predict_box1 = y_pred[..., :4]  # ? * 7 * 7 * 4
    predict_box2 = y_pred[..., 5:9]  # ? * 7 * 7 * 4
    predict_box = K.stack([predict_box1, predict_box2],axis=3)


    # label, predict box shape 변경
    _label_box = K.reshape(label_box, [-1, 7, 7, 1, 4])
    _predict_box = K.reshape(predict_box, [-1, 7, 7, 2, 4])

    # 라벨 min xy, max xy 좌표로 변환
    label_xy, label_wh = yolo_head(_label_box)  # ? * 7 * 7 * 1 * 2, ? * 7 * 7 * 1 * 2
    label_xy = K.expand_dims(label_xy, 3)  # ? * 7 * 7 * 1 * 1 * 2
    label_wh = K.expand_dims(label_wh, 3)  # ? * 7 * 7 * 1 * 1 * 2
    label_xy_min, label_xy_max = xywh2minmax(label_xy, label_wh)  # ? * 7 * 7 * 1 * 1 * 2, ? * 7 * 7 * 1 * 1 * 2

    # 두 예측 좌표를 두개의 min xy, max xy 좌표로 변환
    predict_xy, predict_wh = yolo_head(_predict_box)  # ? * 7 * 7 * 2 * 2, ? * 7 * 7 * 2 * 2
    predict_xy = K.expand_dims(predict_xy, 4)  # ? * 7 * 7 * 2 * 1 * 2
    predict_wh = K.expand_dims(predict_wh, 4)  # ? * 7 * 7 * 2 * 1 * 2
    predict_xy_min, predict_xy_max = xywh2minmax(predict_xy, predict_wh)  # ? * 7 * 7 * 2 * 1 * 2, ? * 7 * 7 * 2 * 1 * 2

    iou_scores = iou(predict_xy_min, predict_xy_max, label_xy_min, label_xy_max)  # ? * 7 * 7 * 2 * 1
    print("iou_scores : ")
    print(iou_scores)
    # best_ious ==> 두 box의 iou 값 [[44]
    #                               [40]]] 중 axis=4로 각각 최대값 찾아
    #                               ==> [44 40] 으로 차원 변환
    #
    best_ious = K.max(iou_scores, axis=4)  # ? * 7 * 7 * 2
    print('best_ious : ')
    print(best_ious)
    # 차원 축소한 [44 40]  값중 큰값 선택 [44]
    best_box = K.max(best_ious, axis=3, keepdims=True)  # ? * 7 * 7 * 1

    # tf.cast() ==> Boolean형태인 경우 True이면 1, False이면 0을 출력
    # box_mask ==> [ 0 1 ] 로 변환  ==> loss에 책임있는  predictor 선택하기 위함
    box_mask = K.cast(best_ious >= best_box, K.dtype(best_ious))  # ? * 7 * 7 * 2

    no_object_loss = 0.5 * (1 - box_mask * response_mask) * K.square(0 - predict_trust)
    #object_loss = box_mask * response_mask * K.square(1 - predict_trust)
    object_loss = box_mask * response_mask * K.square(best_ious - predict_trust)
    confidence_loss = no_object_loss + object_loss
    confidence_loss = K.sum(confidence_loss)

    class_loss = response_mask * K.square(label_class - predict_class)
    class_loss = K.sum(class_loss)

    _label_box = K.reshape(label_box, [-1, 7, 7, 1, 4])
    _predict_box = K.reshape(predict_box, [-1, 7, 7, 2, 4])

    label_xy, label_wh = yolo_head(_label_box)  # ? * 7 * 7 * 1 * 2, ? * 7 * 7 * 1 * 2
    predict_xy, predict_wh = yolo_head(_predict_box)  # ? * 7 * 7 * 2 * 2, ? * 7 * 7 * 2 * 2

    box_mask = K.expand_dims(box_mask)
    response_mask = K.expand_dims(response_mask)

    box_loss = 5 * box_mask * response_mask * K.square((label_xy - predict_xy) / 448)
    box_loss += 5 * box_mask * response_mask * K.square((K.sqrt(label_wh) - K.sqrt(predict_wh)) / 448)
    box_loss = K.sum(box_loss)

    loss = confidence_loss + class_loss + box_loss

    return loss
