import random
humans = []
def human_creator(id):
    age = random.randint(1,100)
    weight = random.randint(20,150)
    height = random.randint(20,350)
    health = random.randint(0,100)
    human = {'id':id,'age':age,'weight':weight,'height':height,
    'health':health}
    return human

ftns_hmn_list=[] #a list for humans and their fittnesses
fittness_list=[]
def fittness(human): #age*height*health/weight
    fittness_score =int(human['age']*human['health']*human['height']/human['weight'])
    return fittness_score
    
def crossOver(human1,human2):
    rnd = random.randint(0,1)
    if rnd == 0 :
        weight = human1['weight']
    else :
        weight = human2['weight']
    rnd = random.randint(0,1)
    if rnd == 0 :
        height = human1['height']
    else :
        height = human2['height']
    rnd = random.randint(0,1)
    if rnd == 0 :
        health = human1['health']
    else :
        health = human2['health']     
    human = {'id': int(str(human1["id"]) + str(human2["id"]) ),'age':1,'weight':weight,'height':height,'health':health}
    return human
    
def sortt(a): #sort humans by their fittnesses
    x=[]
    b=a.copy()
    while len(b)>0:
        for i in range(0,len(b)):
            minn=b[0][0]
            minnn=b[0]
            for j in range(1,len(b)):
                if b[j][0]<minn:
                    minn=b[j][0]
                    minnn=b[j]
                
            x.append(minnn)
            b.remove(minnn)
    return x

for id in range(1,21):
    a = human_creator(id)
    humans.append(a)
    b = fittness(a)
    fittness_list.append(b)
   
for i in range(1,21): #making ftns_hmn_list
    ftns_hmn_list+=[[fittness_list[i-1],humans[i-1]]]
    
for j in range(1,21): #inheritance for 20 generation
    ftns_hmn_list=sortt(ftns_hmn_list)
    for i in range (len(ftns_hmn_list)-1,len(ftns_hmn_list)-9,-2): # making childs from 4 pair parents that have most fittnesses
        child=crossOver(ftns_hmn_list[i][1],ftns_hmn_list[i-1][1])
        ftns_hmn_list+=[[fittness(child),child]]
        
ftns_hmn_list=sortt(ftns_hmn_list)

for i in range(len(ftns_hmn_list)-1,-1,-1):
    print(i+1,"=",ftns_hmn_list[i])
    

    
