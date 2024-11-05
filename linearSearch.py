
pos = -1            # if element doesnt found...


def search(lst , targetvalue):

    for currentvalue in range(len(lst)):
        if lst[currentvalue] == targetvalue:    #checking current value and targetvalue are equal using loop...

            globals()['pos'] = currentvalue
            return True                     #if found...

    return False

lst = []
x = int(input("no.of elements uh wanted in lst : "))

for i in range(x):
    n = int(input("element {} :  ".format(i+1)))
    lst.append(n)
    pass

targetvalue = int(input("enter target value to search : " ))

if search(lst,targetvalue):
    print("element found at index : " , pos)
else:
    print("element not found : " ,  pos)
















lst = [1,2,3,4,38,16,5]
targetvalue = 38