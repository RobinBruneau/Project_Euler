

bissect = [31,29,31,30,31,30,31,31,30,31,30,31]
non_bissect = [31,28,31,30,31,30,31,31,30,31,30,31]
jour = 1
dimanche = 0
for k in range(1900,2001):
    if k == 1900 :
        l = non_bissect
    elif k%4 == 0 :
        l = bissect
    else :
        l = non_bissect

    for m in range(1,13):
        jour += l[m-1]

        if k>=1901:
            if jour%7 == 6 :
                dimanche += 1


if jour % 7 == 6 :
    dimanche -= 1
print(dimanche)