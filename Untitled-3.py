strok=input()
slov=strok.split()
a={}
for i in slov:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
print("самое длинное слово - ",max(slov,key=len))
print("наиболее часто встречающееся слово - ",max(a,key=a.get))
