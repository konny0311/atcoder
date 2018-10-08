#賢いコード
n = int(input())
a = sorted(list(map(int, input.split())), reverse = True)
print(sum(a[::2]) - sum(a[1::2])) #(index0 ~ 最後を2step) - (index1 ~ 最後を2stepで)


def getOneNumFromArray(nums:list):
    if len(nums) > 0:
        maxNum = max(nums)
        indexOfMaxNum = nums.index(maxNum)
        return nums.pop(indexOfMaxNum)
    else:
        return 0


n = int(input())
nums = []
for i in input().split():
    nums.append(int(i))
aliceSum = 0
bobSum = 0
while len(nums) > 0:
    alicesNum = getOneNumFromArray(nums)
    aliceSum += alicesNum
    bobsNum = getOneNumFromArray(nums)
    bobSum += bobsNum

print(aliceSum-bobSum)
