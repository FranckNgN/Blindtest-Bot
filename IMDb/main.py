import imdb

ia = imdb.IMDb()
name = 'Star Wars'

search = ia.search_movie(name)

for i in search:
    print(i)