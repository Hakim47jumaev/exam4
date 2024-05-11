def char_appears(str1,lt):
    mylst=[]
    mylist=str1.split()
     
    for i in mylist:
        cnt=0
        for j in range(len(i)):
            if i[j].lower()==lt:
                cnt+=1
            
        mylst.append(cnt)
    return mylst
a=input()
b=input()
print(char_appears(a,b)),
