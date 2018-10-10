from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
deg, dis = map(int, input().split())
degrees = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
Tdeg = ''
if 3487.5 <= deg or deg < 112.5:
    Tdeg = 'N'
else:
    degIndex = int(round(deg / 225, 0))
    Tdeg = degrees[degIndex]

ms = float(Decimal(str(dis/60)).quantize(Decimal('0.1'), rounding = ROUND_HALF_UP))
winds = [0.2,1.5,3.3,5.4,7.9,10.7,13.8,17.1,20.7,24.4,28.4,32.6]
winds.append(ms)
winds.sort()
# winds = list(set(winds)) #重複削除
print(winds)
Twind = winds.index(ms)

Tdeg = 'C' if Twind == 0 else Tdeg
print(Tdeg, Twind)
