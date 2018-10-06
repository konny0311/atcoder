def proc(i):
    return int(i) + 1

a,b,c =map(proc, [input() for i in range(3)])
x = int(input())
if x % 50 != 0:
    x = int(input('xは50の倍数です。再入力してください'))
cnt = 0
for ai in range(a):
    for bi in range(b):
        for ci in range(c):
            total = 500 * ai + 100 * bi + 50 * ci
            if x == total:
                cnt += 1
print(str(cnt))
