import jieba
import zhon.hanzi
from nltk.corpus import stopwords
import nltk

import jieba.posseg as psg
print(nltk.find("."))

punc = zhon.hanzi.punctuation  # 要去除的中文标点符号
baidu_stopwords = stopwords.words('baidu_stopwords')  # 导入停用词表
jieba.load_userdict(r"D:/2022spring/project/mood/mood/mydict.txt")
# 读入文件
#with open('E:\Python_code\Big_data\homework4\水浒传.txt', encoding="utf-8") as fp:
    #text = fp.read()

data=["我真的好绝望","想找个说说话的人 再也不敢也不想向身边的人倾诉。","工作的时候,同事就说我特别扫兴,什么时候看见我都是拉着一张别人欠我钱的脸,其实我也不想的,但真的高兴不出来,我自己都觉得自己的笑特别假"]

def wordfreq(text):
    ls=[]
    for i in text:
        cut=jieba.lcut(i)# 分词
        for j in cut:
            ls.append(j)
    counts = {}
    for i in ls:
        if len(i) > 1:
            counts[i] = counts.get(i, 0) + 1
    for word in baidu_stopwords:  # 去掉停用词
        counts.pop(word, 0)
    ls1 = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    return ls1
        
#result=wordfreq(data)

def freq_class(text):
    ls=[] 
    for seq in text:
        for x in psg.cut(seq):
            if len(x.word)>1:
                if x.word not in baidu_stopwords:
                    ls.append((x.word,x.flag))
                
    #计算词频
    counts = {}
    for i in ls:
        counts[i] = counts.get(i, 0) + 1
    #for word in baidu_stopwords:  # 去掉停用词
        #counts.pop((word,"\w"), 0)
        #counts.pop(word, 0)
    ls1 = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    return ls1
   
result=freq_class(data) 
        

'''
# 统计词频
counts = {}
for i in ls:
    if len(i) > 1:
        counts[i] = counts.get(i, 0) + 1

# 去标点（由于我这里不统计长度为1的词，去标点这步可省略）
# for p in punc:
#     counts.pop(p,0)

for word in baidu_stopwords:  # 去掉停用词
    counts.pop(word, 0)

ls1 = sorted(counts.items(), key=lambda x: x[1], reverse=True)  # 词频排序

#print(ls1[:20])
'''