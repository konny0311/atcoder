n = int(input())
numList = []
for i in input().split():
    numList.append(int(i));

num = 0
even = True
while even:
    for i, each in enumerate(numList):
        if each % 2 != 0:
            even = False
        numList[i] = each / 2
    num += 1
print(num-1)

#より良い回答
n = input()
a = list(map(int, input().split()))
cnt = 0
while all(i%2==0 for i in a):
    a = [i/2 for i in a]
    cnt +=1
print(cnt)
