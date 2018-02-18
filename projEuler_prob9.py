
def pythagorean_triplet():
    """highest values any of a,b,c can attain"""
    c = 998
    while c > 3: #lowest value c can attain
        b = c - 1
        while b > 2:
            a = 1000 - b - c
            if (a*a == c*c - b*b) & (a > 0):
                return a,b,c
            else:
                b -= 1
        c -= 1

a,b,c = pythagorean_triplet()
print(a,b,c)
print(a*b*c)