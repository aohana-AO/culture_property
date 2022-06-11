from django.test import TestCase

# Create your tests here.

import pandas as pd
from .models import Bunka
"""
df = pd.read_csv('app/user.csv')

for _, row in df.iterrows():
 dict_data = row.to_dict()
 User.objects.create(**dict_data)

question = User.objects.all()
print(question.count())  # 5
print(User.objects.all())

"""
df = pd.read_csv('app/382019_cultural_property.csv')
df=df.loc[:,['名称','緯度','経度','文化財分類','種類','愛媛県松山市住所','URL','数','単位']]
print(df)
for _, row in df.iterrows():
 dict_data = row.to_dict()
 Bunka.objects.create(**dict_data)

question = Bunka.objects.all()
print(question.count())  # 5
print(Bunka.objects.all())
