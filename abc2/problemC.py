Xa, Ya, Xb, Yb, Xc, Yc = map(int, input().split())
result = abs((Xb-Xa)*(Yc-Ya)-(Yb-Ya)*(Xc-Xa)) / 2
print(result)
