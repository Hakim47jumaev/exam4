def is_harshad(a):
    b=0
    k=a
    while k>0:
        c=k%10
        b+=c
        k=k//10
     
    if a%b==0:
        return True
    else:
        return False
a=int(input())
print(is_harshad(a))