for i in range(int(input())):
    n=input()
    a=n[:len(n)//2]
    b=n[len(n)//2:]
    c=n[:len(n)//2]
    d=n[(len(n)//2)+1:]
    if (len(n)%2==0):
        if(sorted(a)==sorted(b)):
            print("YES")
        else:
            print("NO")
    else:
        if(sorted(c)==sorted(d)):
            print("YES")
        else:
            print("NO")
