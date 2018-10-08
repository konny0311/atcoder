km = int(input())/1000
if km < 0.1:
    print('00')
elif 0.1 <= km <= 5:
    vv = int(10*km)
    vv = str(vv)
    if len(vv) < 2:
        vv = '0' + str(vv)
    print(vv)
elif 6 <= km <= 30:
    print(int(km + 50))
elif 35 <= km <= 70:
    print(int((km-30)/5 + 80))
elif 70 < km:
    print('89')
