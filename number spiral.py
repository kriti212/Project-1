t = int(input())

for _ in range(t):
    y, x = map(int, input().split())

    if x%2==1 and x>=y:
        result=(x*x)-(y-1)
    elif x%2==0 and x>=y:
        result=pow((x-1),2)+y
    elif y%2==1 and y>=x:
        result=pow((y-1),2)+x
    elif y%2==0 and y>=x:
        result=(y*y)-(x-1)

    print(result)
