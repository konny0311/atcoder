import itertools
n,m = map(int, input().split())
relation = {}
for i in range(m):
    x, y = map(int, input().split())
    relation.setdefault(x,[x]).append(y) #javaのHash宣言みたい
    relation.setdefault(y,[y]).append(x)
groups = list(relation.values())
# print(groups)
#TODO'違いに知り合い'という状態をどうやって表すか
# 重複組み合わせを考えてそれらの最大論理積が答えでは?
results = []
for i in range(2,len(groups)+1):
    for v in itertools.combinations(groups,i):
        # print(v)
        intersection = set(v[0])
        for each in v:
            intersection = intersection & set(each)
        results.append(len(intersection))
if results:
    print(max(results))
else:
    print(1)
