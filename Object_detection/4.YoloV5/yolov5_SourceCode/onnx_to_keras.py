import onnx
# import tensorflow as tf
# from tensorflow.python import keras
from onnx.backend.base import Backend
#from onnx2keras import onnx_to_keras

import torch
import os
import keras
#torch.hub.load('./','custom','')
# Load ONNX model
# onnx_model = onnx.load('yolov5s.onnx')
# tf_rep = Backend.prepare(onnx_model)
# #
# # #tf_rep = onnx_tf.backend.prepare(onnx_model)
# keras.models.save_model(tf_rep,'yolov5s.h5',save_format='h5')

# Call the converter (input - is the main model input name, can be different for your model)
# k_model = onnx_to_keras(onnx_model,input_names=['images'] , input_shapes=(1, 3, 416, 416))

model_name='./yolov5s.pt'
#model_name='yolov5s.onnx'
model = torch.hub.load(os.getcwd(), 'custom', source='local', path = model_name, force_reload=True)
#model = torch.hub.load(os.getcwd(), 'custom', source='local', path = model_name)
#model = torch.hub.load('./', 'custom', source='local', path = model_name)
torch.save(model, './yolov5s.h5')
#keras.models.save_model(model,'yolov5s.h5',save_format='h5')
#
#
# # # Load the trained model from the .pt file
# # model = torch.hub.load('./', 'custom','yolov5s.pt', source='local')
# #
# # Export the model to ONNX format
# torch.onnx.export(model, torch.randn(1, 3, 640, 640), 'yolov5s.onnx', opset_version=11)