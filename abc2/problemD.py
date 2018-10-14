n,m = map(int, input().split())
relation = {}
for i in range(m):
    x, y = map(int, input().split())
    relation.setdefault(x,[]).append(y) #javaのHash宣言みたい
    relation.setdefault(y,[]).append(x)
print(relation)
#TODO'違いに知り合い'という状態をどうやって表すか
#各valueの中身を見に行ってkeyが入っている数を得る?
