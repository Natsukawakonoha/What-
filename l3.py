list=["Vangguard","Sniper","Guard","Caster","Defender","Medic","Specialist","Supporter"]
list2=[0,2,3,4,5]
Rhodes=list[2:7:2]
#print(Rhodes)
del list[0:6:2]
n=len(Rhodes)
u=min(list)#其实是字符首位ASCII码在对比
v=max(list)
w=Rhodes.index("Defender")
R=Rhodes*2
r=R.count("Guard")
Rhodes.append("Doctor")
Rhodes.extend(R)
Rhodes.insert(10,"New")#某元素，后面的元素顺延
list2.insert(2,7)
list2.reverse()
list2.sort()
ex=list2.pop()#把最后一位拿出来然后在列表里删掉
Rhodes.remove("Defender")

##这里注意！必须通过append 和insert来添加已经成型的列表元素
#这里证实：未知列表元素数量的话不能insert!也就是不能把元素插进原本没有地地方
#，而是先有存储空间 后才能插入元素再然后才拓宽列表
#iny=[]
#t=p=sum=0
#while(p!=-1):
#   p=int(input("第%d个学生的成绩是 "%(t+1)))
#   iny.insert(t,p)     
#   sum+=p
#   t+=1
#iop=(sum+1)/(t-1)
#print("the total is %d"%int(sum+1))
#print("the average is %f" % iop)#print无法识别我的意图，要新开数据
del list
#score=[]
#total=inscore=0
#while(inscore!=-1):
#    inscore=int(input("请输入学生成绩:"))
#    score.append(inscore)
#print("共有%d位学生"%(len(score)-1))
#for i in range(0,len(score)-1):
#    total+=score[i]
#average=total/(len(score)-1)
#print("本班成绩：%d 分，平均成绩：%5.2f 分"%(total,average))

#元组
#Te= (1,2,3,4)
#te=list(Te)
#
##字典：一一对应 弱化顺序概念,提供两种独立概念相互关联的数据结构
#cost={"Vina":14,"Blue posion":12,"Texas":12,"Vina":12}#前者为键，后者为值,只认后键
#print(cost)
#
#cost["Texas"]=11#键只能删不能改，
#cost["Angelina"]=16#不过可以直接加上去
#del cost["Vina"]#删除的时候不管对应几个一样的键全带走
##cost.clear()这个直接抄家
##del cost #地基都没了
#cost_cp=cost.copy()#复制是在字典类定义里面的
#c=cost.get("Texas",9)
#b="Vina" in cost
#
#jobs={"Darknight":70,"WhiteMegic":70.5,"Monk":61}
#jobs_s=jobs.values()#这个不会存储起来?
#print(jobs_s)
#jos=jobs.setdefault("Ninja")
#jobs["Ninja"]=70.12
#jos=jobs.setdefault("Ninja")

#Arknights={"Amiya":96,"Shiron":120,"Shining":90}
##Ark=Arknights.items()
##list_ark=list(Ark)
##use=0
#for i in range(3,5):
#    N=input("No.%d student's Name is: " % (i+1))
#    G=int(input("No.%d student's Grade is: " % (i+1)))
#    Arknights[N]=G
##Ark_names=list(Arknights.keys())
##Ark_Grades=list(Arknights.values())
##
##for j in range(5):
##    print("The stdudent %s's Grade is %d"%(Ark_names[j],Ark_Grades[j]))
#Ark_its=list(Arknights.items())
#for names,grades in Ark_its:#尽快适应这种用法！
#    print("The stdudent %s's Grade is %d"%(names,grades))

#def ctof(c):#它可以在任意的位置
#    f=c*1.8+32
#    fu=c*1.6
#    return f,fu #会以元组的方式输出！！！这很重要！
#
#cx=float(input("please input the C "))
#print(ctof(cx))
#
#def plus(a,b=7):#default必须最后一个
#    c=a+b
#    return c
#an=int(input("please input parameter1:"))
#bn=int(input("please input parameter2:"))
#print(plus(an))#8+7
##print(plus(an,bn))
##print(plus(b=17,a=97))
#
###参数优先级：制定para=xxx!(即使打乱顺序也一样)，可以无视默认 >>正常参数变量 
#
#def mutplus(*parameters):
#    sum=0
#    for i in parameters:
#        sum+=i
#    return sum
#
#print("The number is %d" % mutplus(3,5,98))#几个都可以

def scope():#局部变量只在函数内出现并生效，在函数内优先级更高，如果套globe可，同名按先后处理以强制让它是全局
    global var1
    var1=1
    print(var1,var2)
    
var1=10
var2=20

scope()
print(var1,var2)

innum = 0
lis=[]
while(innum!=-1):
    innum=int(input("请输入正整数(-1:结束):"))
    lis.append(innum)
print("共输入 %d 个数"% len(lis))
print("最大数为:%d"% max(lis))
print("最小数为:%d"% min(lis))
print("和为:%d"% sum(lis))
print("从大到小排序:{}".format(sorted(lis,reverse=True)))

import random
re=random.random()


