def slovar(strok):
    slov=strok.split()
    a={}
    for i in slov:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    return(a)
def samdlin(strok):
    slov=strok.split()
    return(max(slov,key=len))
def naibolvs(strok):
    a=slovar(strok)
    return(max(a,key=a.get))
