num=int(input())
if num<=1:
    print("not an prime")
else:
    for i in range(2,(num**0.5)+1):
        if num%i==0:
            print("not an prime")
            break
    else:
        print("prime")
            