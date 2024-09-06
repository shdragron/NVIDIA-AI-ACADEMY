import numpy as np
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
#print(tokenizer.word_index)

X_train_data['sequences'] = tokenizer.texts_to_sequences(X_train_data['document'])
X_test_data['sequences'] = tokenizer.texts_to_sequences(X_test_data['document'])
print(X_train_data[:5])
print(X_test_data[:5])

X_train_data.reset_index(drop=True, inplace=True)
X_test_data.reset_index(drop=True, inplace=True)

print(X_train_data[25:30]) # 텅빈 데이터 발생

drop_train_idx = [idx for idx, sentence in enumerate(X_train_data['sequences']) if len(sentence) < 1]
print(drop_train_idx)
drop_test_idx = [idx for idx, sentence in enumerate(X_test_data['sequences']) if len(sentence) < 1]
print(drop_test_idx)

X_train_data.drop(drop_train_idx, axis=0, inplace=True)
X_test_data.drop(drop_test_idx, axis =0, inplace=True)

X_train_data.reset_index(drop=True, inplace=True)
X_test_data.reset_index(drop=True, inplace=True)

y_train = np.array(X_train_data['label'])
y_test = np.array((X_test_data['label']))
print(len(y_train), len(y_test))

X_train_pades = pad_sequences(X_train_data['sequences'], maxlen=30)
X_test_pades = pad_sequences(X_test_data['sequences'], maxlen=30)

print(len(X_train_pades[0]))
print(X_train_pades[:1])