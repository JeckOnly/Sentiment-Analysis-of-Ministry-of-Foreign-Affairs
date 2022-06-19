from harvesttext import HarvestText
import requests
import matplotlib.pyplot as plt
from getBid import getBidList
from pinglun import online_save

ht = HarvestText()


bidList = getBidList()
pinglunResultList = []
emotionalList = []
print(len(bidList))
print(bidList)
for bid in bidList:
    result = online_save(bid)
    result = result.replace('\n', '').replace('\r', '')
    result = ht.clean_text(result)
    pinglunResultList.append(result)

for pinglun in pinglunResultList:
    try:
        ht.build_sent_dict(pinglun, min_times=1)
        emotionalList.append(ht.analyse_sent(pinglun))
    except:
        print()
    else:
        print()


plt.plot(emotionalList,color='b',linewidth=0.5,linestyle='-',label='数据三')#linestyle指定线形为点
plt.legend(loc=2)#标签展示位置，数字代表标签具位置
plt.xlabel('time')
plt.ylabel('rate')
plt.title('3119005208')
plt.show()






