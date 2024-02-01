from jikan4.jikan import Jikan
import requests as req
import urllib.request
import os


jikan = Jikan()

anime = jikan.get_anime_characters(38000)
data = anime.data

x = data[0]
role =x.role
name = x.character.name
images = x.character.images
jpg = images.jpg
jpgUrl = jpg.image_url
print('test')

searchAnime = jikan.search_anime('tv', 'naruto')

kimetsu = jikan.search_anime('tv', 'kimetsu no yaiba')
kimetsu1 = kimetsu.data[0]
kimetsu1Id = kimetsu1.mal_id

def pictureJpgDL(jpgUrl, folder, jpgName):
    urllib.request.urlretrieve(jpgUrl, folder + jpgName)#r'D:\Pictures\Blindtest\test\test.jpg'


pictureJpgDL(jpgUrl, r'D:\\Pictures\\Blindtest\test\\', 'test.jpg')