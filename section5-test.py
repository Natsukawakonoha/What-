import requests
from bs4 import BeautifulSoup
url1='http://www.pm25x.com/'
html=requests.get(url1)
sp1=BeautifulSoup(html.text,'html.parser')

city=sp1.find("a",{"title":"天津PM2.5"})
citylink=city.get("href")
url2=url1+citylink#这种有可能只有半截链接

html2=requests.get(url2)
sp2=BeautifulSoup(html2.text,'html.parser')
PM=sp2.find("div",{"class":"aqivalue"})

print("PM2.5 in TJ  is",PM.text)




import  requests,os
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'http://www.ustb.edu.cn/'
html=requests.get(url)
html.encoding="utf-8"
sp=BeautifulSoup(html.text,'html.parser')

images_dir="images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

links=sp.find_all(['a','img'])
for link in links:
    src=link.get("src")
    href=link.get("href")      
    attrs=[src]
    
    for attr in attrs:
        if src!=None and ('.jpg' in src or '.png' in src):
            print(src)
            full_path = attr
            filename=full_path.split('/')[-1]
            ext=filename.split('.')[-1]
            filename=filename.split('.')[-2]
            
            if 'jpg' in ext:
                filename=filename+'.jpg'
            else: 
                filename=filename+'.png'
            
            try:
                image=urlopen(full_path)
                f=open(os.path.join(images_dir,filename),'wb')
                f.write(image.read())
                f.close
            except:
                print("error!")
        
        
#del attr,attrs,ext,filename,images_dir,links,src,url

import os
full_path=os.path.abspath("Nes.txt")#这东西在哪里.
base=os.path.basename("Nes.txt")#文件会直接给文件名
basex=os.path.basename(full_path)#非文件，链接使用不用引号
basead=os.path.dirname(__file__)#2_!!!!
baseada=os.path.dirname(full_path)#这东西在哪里?
ex=os.path.exists("Nes.txt")
siz=os.path.getsize("Nes.txt")
iab=os.path.isabs(base)
ifi=os.path.isfile("Nes.txt")
idir=os.path.isdir("Nes.txt")
sp=basead.split('/')[-1]
spp=os.path.splitdrive(full_path)
ui=os.path.join(basead+"/"+base)

cur_path=os.path.dirname(__file__)
sample_tree=os.walk(cur_path)
for direname,subdir,files in sample_tree:
    print("文件路径：",direname)
    print("目录列表：",subdir)
    print("文件列表：",files)
print()

import shutil#copy包
cur_path=os.path.dirname(__file__)
destfile=cur_path+"/"+"images"+"/"+"1'.txt"
shutil.copy("Nes.txt",destfile)

os.system("notepad"+"Nes.txt")


 
    

content='''New  MOSTIMA
'''

f=open('file1.txt','w')#如果没有即刻创建
f.write(content)

f.close()



f=open('file1.txt','r')#如果没有即刻创建
for line in f:
    print(line,end=" ")
f.close()
import paddle.fluid
paddle.fluid.install_check()

