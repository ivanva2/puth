strok=input()
for i in range(len(strok)):
    if i==2:
        continue
    elif strok[i]=="c":
        print("найден символ с")
print("длина строки = ",len(strok))
print("строка без последнего символа", strok[:-1])


