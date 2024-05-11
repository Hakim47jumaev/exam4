list1=input().split()
min=list1[0]
k=0
for i in range(len(list1)):
    if list1[i]<min:
        min=list1[i]
        k=i
big=list1[k+1]
for i in range(k+1,len(list1)):
    if list1[i]>big:
        big=list1[i]
print(int(big)-int(min))