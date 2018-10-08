#正解コード
n, y = map(int, input().split())
for i in range(n + 1):
    for j in range(n - i + 1):
        if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
            print(i, j, n - i - j)
            exit()
print("-1 -1 -1")

# #TLEになるし序長
# n,y = list(map(int, input().split()))
# cnt = False
# maxA = y//10000
# while not cnt:
#     for a in reversed(range(maxA+1)): #10000円札の枚数:a
#         if cnt:
#             break
#         for b in reversed(range(n-a+1)): #5000円札の枚数:b
#             if cnt:
#                 break
#             # for c in reversed(range(n-a-b+1)): #1000円札の枚数
#             c = n-a-b
#             total = 10000*a + 5000*b + 1000*c
#             if total == y and cnt is not True:
#                 print('{} {} {}'.format(a,b,c))
#                 cnt = True
#                 exit(0)
#                 # if total < y:
#                 #     print('-1 -1 -1')
#                 #     cnt = True
#                 #     break
#
# if not cnt:
#     print('-1 -1 -1')
