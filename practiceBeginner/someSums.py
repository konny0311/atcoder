def dividePerDigit(num):
    lst = []
    while num > 0:
        lst.append(num%10)
        num//=10
        lst.reverse()
    return lst

n, a, b = map(int, input().split())
sumOfsum = 0
for each in range(1,n+1):
    digits = dividePerDigit(each)
    total = 0
    for i in digits:
        total += i
    if a <= total and total <= b:
        sumOfsum += each
print(sumOfsum)
