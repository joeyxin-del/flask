import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import app as APPLICATION
import json
import word_cut
db = SQLAlchemy(APPLICATION.app)

class fine_data(db.Model):
    __tablename__="finedata"
    id=db.Column(db.String(255),primary_key=True,name="id")
    thit=db.Column(db.String(255),name="非此即彼")#this&that
    #thit=db.Column(db.String(255),name="非此即彼")
    
    comment=db.Column(db.String(255),name="comment")
    
    
    def list2dict(self):
        dic=[]
        for u in self:
            u=u._asdict()
            dic.append(u)
        return dic
    def list2list(self):
        dic=[]
        for u in self:
            u=u._asdict()
            dic.append(str(u.values())[14:-3])
        return dic

data=db.session.query(fine_data.comment).all()
data=fine_data.list2list(data)

'''
freq=word_cut.freq_class(data)

f=open(r"D:/2022spring/project/mood/mood/word_freq.txt","w")
 

for line in freq:
    f.write(str(line)+'\n')
f.close()

'''
f=open(r"word_freq.txt","r")
freq=f.readlines()

for i in range(len(freq)):
    freq[i]=freq[i].split(",")
    freq[i][0]=freq[i][0][3:-1]
    freq[i][1]=freq[i][1][2:-2]
    freq[i][2]=freq[i][2][:-2]

topic=[]
for i in freq:
    if i[1]=="n":
        topic.append(i)
        
value=[]
for i in topic[:200]:
    value.append({"name":i[0],"value":i[2]})

echart6_data={
    'title': '热点词频统计',
    'data':value[:70]}

echart7_data={
    'title': '热点词频统计',
    'data':value}
print(len(data))