x=input()
x1=[]
y=input()
for i in range(len(x)):
    if x[i]==('(' ):
        x1.append(x[i])
    elif  x[i]==('[' ):
        x1.append(x[i])
    elif x[i]==('{' ):
        x1.append(x[i])    

print(x1)        