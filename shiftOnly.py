n = int(input('200までの整数を入力:'))
numList = []
for i in range(n):
    numList.append(int(input()));

while len(numList) == n:
    #'2で割っても整数'という条件分岐入れたい
    numList = list(filter(lambda x: x / 2, numList))
