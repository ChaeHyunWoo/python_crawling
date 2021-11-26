# mongodb 퀴즈  1. 매트릭스 평점 가져오기 / 2. 매트릭스평점과 같은 평점의 영화 가져오기/ 3. 매트릭스 영화의 평점을 0으로 만들기
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
#1번 문제
target_movie = db.movies.find_one({'title':'매트릭스'})['star'] # 여기에 ['star']star을 넣어도되고 하단 movie 바로 뒤에 넣어도가능
print(target_movie)
#2번 문제
target_movie = db.movies.find_one({'title':'매트릭스'})
target_star = target_movie['star']

movies = list(db.movies.find({'star': target_star}))
for movie in movies:
    print(movie['title'])
#3번 문제
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})



