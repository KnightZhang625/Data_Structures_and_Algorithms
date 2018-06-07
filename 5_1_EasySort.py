def bubble_Sort(array):

    length = len(array)

    for i in range(length,0,-1):

        for j in range(i-1):

            temp = array[j]

            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    
    return array

def select_Sort(array):

    length = len(array)

    for i in range(length):
        temp = i

        for j in range(i,length-1):

            if array[temp] > array[j+1]:
                temp = j+1

        array[i],array[temp] = array[temp],array[i]

    return array

def insert_Sort(array):

    length = len(array)

    for i in range(1,length):

        for j in range(i,0,-1):

            if array[j] < array[j-1]:
                array[j],array[j-1] = array[j-1],array[j]
            else:
                break

    return array

if __name__ == '__main__':

    l1 = [5,2,6,10,25,21,15]

    # print(bubble_Sort(l1))
    # print(select_Sort(l1))

    print(insert_Sort(l1))
















