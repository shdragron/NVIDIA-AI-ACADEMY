import numpy as np
import pandas as pd
import os
os.environ['JAVA_HOME'] = r'C:\Program Files\Java\jdk-17.0.2'

#header = 0 ==> 파일의 첫 번째 줄에 열 이름이 있음
#delimiter = \t ==> 필드가 탭으로 구분되는 것을 의미한다.
#quoting = 3 ==> 인용구("최고의 최고) 표현등..큰따옴표를 무시하도록 한다.(그대로 사용)
train_data = pd.read_csv('ratings_train.csv',header=0,delimiter='\t', quoting=3)
#print(train_data)
#print(train_data.info())
train_data.dropna(how='any',inplace=True)
#print(train_data.info())
train_data['label'] = train_data['label'].astype('int64')
#print(train_data.info())
print(train_data['document'].nunique())
print(train_data['label'].nunique())

train_data.drop_duplicates(subset=['document'],inplace=True)
#print(train_data.info())

train_data['document'] = train_data['document'].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣\s]','',regex=True)
train_data['document'] = train_data['document'].str.replace('^\s+','',regex=True)
train_data['document'] = train_data['document'].replace('',np.NaN)
print(train_data.loc[train_data['document'].isnull()])

train_data.dropna(how='any', inplace=True) # 한 행에 하나라도 np.NaN 이 있으면 해당 행 삭제
print(train_data.info())

test_data = pd.read_csv('ratings_test.csv', header=0, delimiter='\t', quoting=3)
test_data.dropna(how='any', inplace=True)
test_data['label'] = test_data['label'].astype('int64')

test_data.drop_duplicates(subset=['document'],inplace=True)

test_data['document'] = test_data['document'].str.replace('[^ㄱ-ㅎㅏ-ㅣ가-힣\s]','',regex=True)
test_data['document'] = test_data['document'].str.replace('^\s+','',regex=True)
test_data['document'].replace('',np.NaN, inplace=True)
test_data.dropna(how='any',inplace=True)
print(test_data.info())

# 불용어 제거
from konlpy.tag import Okt
from tqdm import tqdm   # tqdm 4.62.0 version 설치

okt = Okt()

stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

X_train = []
for sentence in tqdm(train_data['document']):
    tokenized_sentence = okt.morphs(sentence, stem=True)
    sentence_removed_stopwords = \
        [word for word in tokenized_sentence if not word in stopwords]
    X_train.append(' '.join(sentence_removed_stopwords))

print(X_train[:5])
train_data['document'] = X_train

X_test = []
for sentence in tqdm(test_data['document']):
    tokenized_sentence = okt.morphs(sentence, stem=True) # 토큰화
    sentence_removed_stopwords = \
        [word for word in tokenized_sentence if not word in stopwords] # 불용어 제거
    X_test.append(' '.join(sentence_removed_stopwords))

print(X_test[:5])
test_data['document'] = X_test

train_data.to_csv('train_stopwords_reviews.csv') # 불용어 제거 train 리뷰 문장 파일로 저장
test_data.to_csv('test_stopwords_reviews.csv')