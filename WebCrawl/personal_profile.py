from personal_feeling import *
from personal_topic import *

if(emot == 'pos'):
	emots = '긍정'
elif(emot == 'neg'):
	emots = '부정'
else:
	emots = '중립'

#크롤링 분석 완료
user_profile = [names]
user_profile = pd.DataFrame(user_profile, columns=["id"])

user_profile["time"] = str(key_max)
user_profile["user_topic"] = pointlist[0]
user_profile['emotion'] = emot

pprint(user_profile)
print("%s님이 매체를 주로 활동하는 시각은 %d시 입니다."%(names, key_max))
print("%s님이 관심을 가질 주제로는 본문에서 %s번 빈도가 나타난 %s가 있습니다."%(names, pointlist[1], pointlist[0]))
print("%s님이 주제에 대해 주로 나타내는 성향은 %s입니다."%(names, emots))

plt.bar(fxs, fnumber)
plt.ylabel("단어 수")
plt.title("단어 계산 (예외)")
plt.xticks([i + 0.5 for i, _ in enumerate(fword)], fword, rotation = 90)
plt.show()
