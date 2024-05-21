A, B, V = map(int, input().split())

x = (V - B) / (A - B)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)


# 올라가는 높이: A
# 내려오는 높이: B
# 소요되는 일수: x (무조건 정수임! 7일, 8일, ...)
# 올라가야 하는 높이: V
# Ax - B(x-1) = V
# Ax - Bx + B = V
# (A - B)x + B = V
# x = (V - B) / (A - B)