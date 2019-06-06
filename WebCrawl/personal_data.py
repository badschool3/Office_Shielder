from personal_json import *
#from personal_feeling import *

from pprint import pprint
import pandas as pd
from collections import Counter
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import os
from konlpy.tag import *

#matplotlib 그래프 한글 깨짐 방지. 폰트 설정.
font_fname = 'C:/Windows/Fonts/NanumGothic.ttf'
font_family = fm.FontProperties(fname=font_fname).get_name()
plt.rcParams["font.family"] = font_family
plt.rcParams['font.size'] = 20.
plt.rcParams['xtick.labelsize'] = 11.
plt.rcParams['ytick.labelsize'] = 11.
plt.rcParams['axes.labelsize'] = 15.

#개인 아이디 크롤링 결과 호출 
main()
with open(names+"_twitter.json",encoding='UTF-8') as json_file:
    json_data = json.load(json_file)
from pprint import pprint
'''pprint(len(json_data))
print("\n")
pprint(json_data)'''

#개인 정보 데이터 셋 저장 
personal_list = [names for x in range(len(json_data))] 
personal_set = pd.DataFrame(personal_list, columns=["id"])
personal_set["user_time"] = [json_data[x]["created_time"] for x in range(len(json_data))]
personal_set["user_message"] = [json_data[x]["message"] for x in range(len(json_data))]
personal_set["uesr_tags"] = [json_data[x]["hashtags"] for x in range(len(json_data))]
personal_set["user_link"] = [json_data[x]["link"] for x in range(len(json_data))]
#pprint(personal_set)

#주로 활동하는 시간 파악
arr = list(personal_set["user_time"])
isarr = [int((((arr[x].split())[1].split(":"))[0])) for x in range(len(arr))]
result = Counter(isarr)
def f1(x):
	return result[x]
key_max = max(result.keys(), key=f1)

#빈도수 바탕 주제 분석 - 형태소 분리
arr2 = list(personal_set["user_message"])
#pprint(arr2)

okt = Okt()
def tokenize(doc):
     return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

train_docs = [(tokenize(arr2[x])) for x in range(len(arr2)-1)]
#pprint(train_docs)

#빈도수 바탕 주제 분석 - 감정 분석
with open('train_docs.json', 'w', encoding="utf-8") as make_file:
    json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
with open("train_docs.json",encoding='UTF-8') as json_file:
    json_data2 = json.load(json_file)

## 더 작성되어야 할 

#크롤링 분석 완료
user_profile = [names]
user_profile = pd.DataFrame(user_profile, columns=["id"])

user_profile["time"] = str(key_max)
user_profile["user_topic"] = 0
user_profile['emotion'] = 0

pprint(user_profile)
print("%s님이 주로 활동하는 시각은 %d시 입니다"%(names, key_max))
