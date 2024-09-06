import numpy as np
import os
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-17.0.2\bin'

import pandas as pd
pd.set_option('display.max_rows',1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',1000)
pd.set_option('max_colwidth', 1000)

X_train_data = pd.read_csv('train_stopwords_reviews.csv',index_col=0)
X_test_data = pd.read_csv('test_stopwords_reviews.csv',index_col=0)

print(X_train_data.info())
print(X_train_data.loc[X_train_data['document'].isnull()])
X_train_data.dropna(how='any',inplace=True)
X_test_data.dropna(how='any',inplace=True)
print(X_train_data.info())

# 데이터 토큰화 및 정수 인코딩
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

word_size = 11775
tokenizer = Tokenizer(word_size)
tokenizer.fit_on_texts(X_train_data['document']) # 빈도수에 따른 정수 매칭


from konlpy.tag import Okt
import os
import re

okt = Okt()
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

from tensorflow.keras.models import load_model
best_newlstm_model = load_model('best_LSTM_model.h5')


def new_review_predict(review_string):
    new_sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣\s]', '', review_string)
    new_sentence = okt.morphs(new_sentence, stem=True)
    new_sentence = [word for word in new_sentence if not word in stopwords]
    print(new_sentence)

    encoded = tokenizer.texts_to_sequences([new_sentence])
    sentence_padding = pad_sequences(encoded, maxlen=30)
    print(sentence_padding)

    score = float(best_newlstm_model.predict(sentence_padding))
    if(score > 0.5):
        print('{:.2f}% 긍정리뷰\n'.format(score*100))
    else:
        print('{:.2f}% 부정리뷰\n'.format((1-score) * 100))

new_review_predict('이 영화 굿 잼')
new_review_predict('이렇게 재미없는 영화는 처음')
new_review_predict('뭐 이런 영화가 다 있어')
new_review_predict('에잇 돈 날렸네')
new_review_predict('이 영화 꼭 추천 도장 꽉!')
new_review_predict('그냥')