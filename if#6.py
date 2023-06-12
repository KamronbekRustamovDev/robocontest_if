n=int(input())
if n%3==0:
    print("3",end=' ')
if n%5==0:
    print("5",end=' ')
if n%7==0:
    print("7",end=' ')
if n%3!=0 and n%5!=0 and n%7!=0:
    print("-1")
