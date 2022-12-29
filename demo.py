qu = [1, 2, 3]
def area(a, b):
    dx = min(a[2], b[2]) - max(a[0], b[0])
    dy = min(a[3], b[3]) - max(a[1], b[1])
    if dx > 0 and dy > 0:
        return dx*dy
    else:
        return 0

a = [1, 2, 3, 4]
b = [2, 3 , 4, 5]

if area(a, b) <= 0:
    qu = []

print(qu)