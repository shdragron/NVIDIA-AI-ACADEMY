# 3_2_pandas.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 10) # 전체 출력
# pd.set_option('display.width', 10) # 전체 출력

# UserID::MovieID::Rating::Timestamp
# UserID::Gender::Age::Occupation::Zip-code
# MovieID::Title::Genres

users = pd.read_csv('ml-1m/users.dat',
                     delimiter='::', engine='python', header=None,
                     names ='UserID::Gender::Age::Occupation::Zip-code'.split('::'))
movies = pd.read_csv('ml-1m/movies.dat',
                     delimiter='::', engine='python', header=None,
                     names ='MovieID::Title::Genres'.split('::'),encoding='cp1251')
ratings = pd.read_csv('ml-1m/ratings.dat',
                     delimiter='::', engine='python', header=None,
                     names ='UserID::MovieID::Rating::Timestamp'.split('::'))

# print(users)
# print(movies)
# print(ratings)

data = pd.merge(pd.merge(users, ratings),movies) # 데이터 일체화
# print(data.head(), end = '\n\n')
# print(data.tail(), end = '\n\n')
# 피보팅 관점을 가져가는 것
df1 = pd.DataFrame.pivot_table(data,values='Rating',index= 'Gender')
print(df1, end='\n\n')

df2 = pd.DataFrame.pivot_table(data,values='Rating',columns= 'Gender')
print(df2, end='\n\n')



# 퀴즈: 평점을 성별, 나이별로 보여주세요

df3 = pd.DataFrame.pivot_table(data,values='Rating',index= 'Age')
print(df3, end='\n\n')

# 퀴즈: 성별 평점을 pivot_table 없이 numpy로 구해보세요.

# print(data.Gender.values == 'F')
# print(data.Rating[data.Gender.values == 'F'])
# print(np.average(data.Rating[data.Gender.values == 'F']))
# print(np.mean(data.Rating[data.Gender.values == 'F']))
# print(np.std(data.Rating[data.Gender.values == 'F']))

# 	*  1:  "Under 18"
# 	* 18:  "18-24"
# 	* 25:  "25-34"
# 	* 35:  "35-44"
# 	* 45:  "45-49"
# 	* 50:  "50-55"
# 	* 56:  "56+"
lab = np.array(["Under 18", "18-24", "25-34","35-44","45-49","50-55","56+"])

df3.plot(kind='bar',colormap= 'jet')
plt.xticks(range(len(lab)),lab, rotation=45)
plt.show()









