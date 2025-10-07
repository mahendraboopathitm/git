num=int(input())
if num<=1:
    print("not an prime num")
else:
    for i in range(2,(num**0.5)+1):
        if num%i==0:
            print("not an prime num")
            break
    else:
        print("prime num")
            