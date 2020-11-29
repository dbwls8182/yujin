inputInt = int(input())

loopCount = 0
sum = 0

while sum < inputInt:
    loopCount += 1
    sum += loopCount

sum -= loopCount

if loopCount % 2 == 0:
    print('{}/{}'.format(inputInt - sum, loopCount - (inputInt - sum) + 1))
else:
    print('{}/{}'.format(loopCount - (inputInt - sum) + 1, inputInt - sum))git