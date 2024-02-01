import pandas as pd
import re
import ast
import json
from  matplotlib import pyplot as plt
import os



df = pd.read_excel(r'D:\Project\Blindtest Bot\animeData\4000.xlsx', index_col = 0)

test = df['opening'].apply(lambda x: x.replace(r'\xa0', ' '))
test = test.apply(lambda x: x.replace("'", ''))
test = test.apply(lambda x: x.strip('][').split(', '))

test