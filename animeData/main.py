from mal import *
import pandas as pd
from jikanpy import Jikan

i = 23999
res = {}
res['id'] = []
res['url'] = []
res['title'] = []
res['titleEng'] = []
res['titleJap'] = []
res['opening'] = []
res['ending'] = []
res['genres'] = []
res['rank'] = []
res['score'] = []
res['scoredBy'] = []
res['episodes'] = []
res['licensors'] = []
res['aired'] = []
res['status'] = []

jikan = Jikan()

while i < 28000:
    try:
        x = jikan.anime(i)
        res['id'].append(x['mal_id'])
        res['title'].append(x['title'])
        res['titleEng'].append(x['title_english'])
        res['titleJap'].append(x['title_japanese'])
        res['opening'].append(x['opening_themes'])
        res['ending'].append(x['ending_themes'])
        res['genres'].append(x['genres'])
        res['rank'].append(x['rank'])
        res['score'].append(x['score'])
        res['scoredBy'].append(x['scored_by'])
        res['episodes'].append(x['episodes'])
        res['licensors'].append(x['licensors'])
        res['aired'].append(x['aired'])
        res['status'].append(x['status'])
        res['url'].append(x['url'])
        print(i, x['title'])
        i += 1

    except Exception as e:
        i += 1
        print(e)

pd.DataFrame(res).to_excel('28000.xlsx')
