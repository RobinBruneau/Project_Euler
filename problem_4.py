max = 0
for k in range(100,1000):
    for j in range(100,1000):
        v = str(k*j)
        rv = v[len(v)::-1]
        if v == rv :
            if int(v)> max :
                max = int(v)

print(max)