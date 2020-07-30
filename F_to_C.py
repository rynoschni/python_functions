def convo(fern):
    ctemp = ((fern - 32) / 1.8)
    return round(ctemp, 2)

my_temp = convo(0)

print (my_temp)

