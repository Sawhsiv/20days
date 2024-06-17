inp=[1,2,3,2,4]
n=[]
for i in range(len(inp)):
    for j in range(1,len(inp)):
        if inp[i]<inp[j]:
            n.append(inp[j])
            break
print(n)
