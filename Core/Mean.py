data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def mean(listVar):
    total = 0 

    for i in listVar:         #Each element from list gets added to find total
        total += i

    return total/len(listVar)

x = mean(data)
print(x)
