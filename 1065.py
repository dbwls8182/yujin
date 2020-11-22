num = 0

def ishansu(x) :
    global num
    if x//100 - x%100//10 is x%100//10 - x%10:
        num += 1

N = int(input())
for i in range(1, N+1) :
    if i < 100:
        num += 1
    else :
        ishansu(i)
print(num)