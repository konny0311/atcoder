#とてもシンプルなのに浮かばなかった
s = input()
s = s.replace('eraser','').replace('erase','').replace('dreamer','').replace('dream','')
if s:
    print('NO')
else:
    print('YES')

# import itertools
#
# s = input()
# t = ''
# words = ['dreamer', 'dream', 'eraser', 'erase']
#
# def checkWords(s:str):
#     words = ['dreamer', 'dream', 'eraser', 'erase']
#     if s[:4] in words:
#         if s[4:6] == 'er':
#             return checkWords(s[6:])
#         return checkWords(s[4:])
#
# #sの文字数からwordsの組み合わせを考える
# #sとtが合致すればYes
# cnt = len(s)
# num0fWords = cnt//5
# # print(num0fWords)
# found = False
# for eachList in list(itertools.permutations(words, num0fWords)):
#     texts = ''
#     for i in eachList:
#         texts += i
#     # print(texts)
#     if texts == s:
#         print('YES')
#         found = True
#         break
# if not found:
#     print('NO')
