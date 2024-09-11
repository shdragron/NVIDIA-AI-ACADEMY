# 1_2_freq.py
import nltk
import re

# print(nltk.corpus.webtext.fileids())

# 퀴즈: wine.txt. 파일을 가져와서 토큰으로 나눠주세요

wine = nltk.corpus.webtext.raw('wine.txt')
# print(wine)

# tokenzie
# tokens = re.findall(r'\w+', wine)
tokens = nltk.RegexpTokenizer(r'\w+').tokenize(wine)
print(len(tokens))
# 한글자 단어 삭제 'a', 't'
tokens = [str for str in tokens if len(str) > 1]
print(len(tokens))
# print(tokens)

# 삭제 'and', 'but', 'the'
tokens = [str for str in tokens if str not in ['the','and','but']]
print(len(tokens))
# print(tokens)

# -> 불용어
tokens = nltk.RegexpTokenizer(r'\w+').tokenize(wine)

# nltk.download('stopwords')
stop_word = nltk.corpus.stopwords.words('english')

tokens = [str for str in tokens if not str in stop_word]
print(len(tokens))










