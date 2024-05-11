from datetime import datetime ,timedelta
a=input()
a=datetime.strptime(a,"%d.%m.%Y")
b=timedelta(days=5)
c=a-b
c=datetime.strftime(c,"%d.%m.%Y")
print(c)