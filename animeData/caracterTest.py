import os
import pandas as pd
import random

rootPath = 'D:\\Pictures\\Blindtest\\'

os.walk(rootPath)

animeCaracPathList = [x[0].split(rootPath)[1] for x in os.walk(rootPath)][1:]

seriesNumb = 4
batchNumb = 10

result = {}

for i in range(seriesNumb):
    result['serie' + str(i)] = {'anime': [], 'caracters': []}

for key in result.keys():
    for batch in range(batchNumb):
        anime = animeCaracPathList[random.randint(0, len(animeCaracPathList)-1)]
        animePath = rootPath + anime 
        caracterList = os.listdir(animePath)
        caracterPick = caracterList[random.randint(0, len(caracterList)-1)].split('.jpg')[0]
        result[key]['anime'].append(anime)
        result[key]['caracters'].append(caracterPick)

for key in result.keys():
    pd.DataFrame(result[key]).to_excel('D:\\Project\\Blindtest Bot\\animeData\\' + key +'.xlsx', index = False)
