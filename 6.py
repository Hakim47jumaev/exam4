def sum_of_wowels(a):
    sdict={
        "A":4,
        "E":3,
        "I":1,
        "O":0,
        "u":0
    }
    cnt=0
    for i in a :
        for j in sdict:
            if i.upper() ==j:
                cnt+=sdict[i.upper()]


    return cnt
a=input()
print(sum_of_wowels(a))
# s="K"
# s=s.lower()
# print(s)