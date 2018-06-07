def merge(a,b):

    temp = []

    h=j=0

    while h<len(a) and j < len(b):

        if a[h] < b[j]:
            temp.append(a[h])
            h += 1
        else:
            temp.append(b[j])
            j += 1

    if h < len(a):

        temp.extend(a[h:])

    if j < len(b):

        temp.extend(b[j:])

    return temp

def sort(array):

    if len(array) <= 1:
        return array

    middle = len(array) // 2

    left = sort(array[:middle])
    right = sort(array[middle:])

    return merge(left,right)

if __name__ == '__main__':

    array = [5,1,2,10,20,15,30,12]

    print(sort(array))