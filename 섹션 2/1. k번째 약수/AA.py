x, y = map(int,input().split())
dirtn= []

for i in range(1,x+1):
    if x % i == 0:
        dirtn.append(i)

if len(dirtn)<y-1:
    print(-1)
else:
    print(dirtn[y-1])

        