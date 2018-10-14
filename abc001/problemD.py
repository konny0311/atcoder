def getUniqueList(seq:list):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

n = int(input())
times = []
for i in range(0,n):
    s,e = map(int,input().split('-'))
    s = s // 5 #直前の5分単位に丸める
    if e % 5 == 0:
        e //= 5
    else:
        e = (e // 5 + 1)#直後の5分単位に丸める
    times.append([s,e])
    #数字を丸めて挿入
    #listに[開始時刻,終了時刻]として挿入し、開始時刻順にソート
    #for文でずらしながら前後で終了時刻と開始時刻を比較する
times.sort()
times = getUniqueList(times)
imoz = [0]*481
for i in range(len(times)):
    imoz[times[i][0]] += 1 #開始時刻に1追加
    # print(times[i][1])
    imoz[times[i][1]] -= 1 #終了時刻に-1追加
# print(imoz)
addedList = []
num = 0
for i in imoz:
    num += i
    addedList.append(num)
# print(addedList)
summarized = [i for i in range(len(addedList)) if addedList[i] > 0]
# print(summarized)
start = summarized[0]
end = 0
finalList = []
for i in range(len(summarized)):
    if i < len(summarized)-1:
        if summarized[i+1] - summarized[i] > 1:
            end = summarized[i]+1
            finalList.append([start*5, end*5])
            start = summarized[i+1]
    else: #indexが最後から２番目に来た時は-2,-1は必ず連続する
        #print(summarized[i])
        finalList.append([start*5, (summarized[i]+1)*5])

# print(finalList)
for each in finalList:
    print('{:04}-{:04}'.format(each[0], each[1]))
