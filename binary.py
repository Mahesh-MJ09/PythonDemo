pos = -1


def search(lst,targetvalue):
    lower = 0
    upper = len(lst) - 1

    for i in range(len(lst)):
        mid = (lower+upper)//2
        if lst[mid] == targetvalue:
            globals()['pos'] = mid
            return True
        elif lst[mid] < targetvalue :
            lower = mid+1
        else:
            upper = mid-1

    return False

lst = [1,2,3,4,5,16,18,38]
targetvalue = 38

if search(lst , targetvalue):
    print("element found at index : " , pos)
else:
    print("element not found : " , pos)