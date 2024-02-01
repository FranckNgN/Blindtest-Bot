from jikan4.jikan import Jikan
import requests as req
import urllib.request
import os

def pictureJpgDL(jpgUrl, folder, jpgName):
    urllib.request.urlretrieve(jpgUrl, folder + jpgName)#r'D:\Pictures\Blindtest\test\test.jpg'

rootPath = 'D:\\Pictures\\Blindtest\\'

jikan = Jikan()
#------------Anime-------------------
anime = jikan.search_anime('tv', 'one piece')
animeData = anime.data[0]
#TODO add english title
animeTitle= animeData.title.replace(':','')
animeID = animeData.mal_id
animeStatus = animeData.status #Finished Airing

try:
    os.mkdir(rootPath + animeTitle)
    print('create folder')
except:
    pass 

#------------Characters------------------
carac = jikan.get_anime_characters(animeID)#kimetsu s1
data = carac.data

if len(data) == 0:
    print('error no caracter data')
x = data[0]

imageUrlList = []

for i in range(len(data)):
    caracData = carac.data[i]
    name = caracData.character.name
    role = caracData.role
    images = caracData.character.images
    jpg = images.jpg
    jpgUrl = jpg.image_url

    if role != 'Supporting':
        pictureJpgDL(jpgUrl, rootPath + animeTitle  + '\\', name + '.jpg')

    # if i <= 10:
    #     pictureJpgDL(jpgUrl, rootPath + animeTitle  + '\\', name + '.jpg')
    #     if data[i].role == 'Supporting':
    #         i+=1


# role =x.role
# name = x.character.name
# images = x.character.images
# jpg = images.jpg
# jpgUrl = jpg.image_url

# pictureJpgDL(jpgUrl, r'D:\Pictures\Blindtest\Kimetsu no Yaiba', name + '.jpg')

# path = r'D:\\Pictures\\Blindtest\\'


