def getUniqueList(seq:list):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]

def trimNum(num:int):
    num = str(num)
    if len(num) < 4:
        for i in range(4-len(num)):
            num = '0'+num
    if num[-2:] == '60':
        num = str(int(num[:2])+1)+'00'
    return num

def appendingTime(times:list):
    isAppended = False
    returnList = []
    for i in range(len(times)):
        if isAppended:
            isAppended = False
            continue
        start = times[i][0]
        end = times[i][1]
        if i == len(times)-1:
            returnList.append([start, nextEnd])
            return returnList
        nextStart = times[i+1][0]
        nextEnd = times[i+1][1]
        if end >= nextStart: #次のリストと合体
            returnList.append([start, nextEnd])
            isAppended = True #合体したら次のリストはスキップしたい
        else:
            returnList.append([start, end])
    print('前:' + str(len(times)))
    print('後:' + str(len(returnList)))
    if len(times) == len(returnList): #合体ない
        return returnList
    else:
        print('再帰処理')
        return appendingTime(returnList) #再帰処理上手く行ってない


n = int(input())
times = []
for i in range(0,n):
    s,e = map(int,input().split('-'))
    if s % 5 != 0:
        s = s // 5 * 5 #直前の5分単位に丸める
    if e % 5 != 0:
        e = (e // 5 + 1) * 5#直後の5分単位に丸める
    times.append([s,e])
    #数字を丸めて挿入
    #listに[開始時刻,終了時刻]として挿入し、開始時刻順にソート
    #for文でずらしながら前後で終了時刻と開始時刻を比較する
times.sort()
times = getUniqueList(times)
print(times)
print('テスト')
returnList = appendingTime(times)
returnList = appendingTime(returnList)
# returnList = []
# point = 0
# endTimeAppend = 0
# #開始時刻、終了時刻を変数として持っておいて、途切れたらリセットする
# for i in range(len(times)-1):
#     if i < point:
#         continue
#     start = times[i][0]
#     end = times[i][1]
#     for j in range(i, len(times)):
#         nextStart = times[j][0]
#         nextEnd = times[j][1]
#         if end >= nextStart:
#             #続ける
#             if i == len(times)-1:
#                 returnList.append([start, nextEnd])
#             if end < nextEnd:
#                 end = nextEnd
#         else:
#             returnList.append([start, end])
#             point = j
#             break
print(returnList)
returnList.sort()
for each in returnList:
    start = trimNum(each[0])
    end = trimNum(each[1])
    print('出力')
    print('{}-{}'.format(start, end))
