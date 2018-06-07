# 求最大子列和

def Max1(list_seq):

    N = len(list)
    max_sum = 0

    for i in range(N):
        max_temp = 0

        for j in range(i,N):
            max_temp += list_seq[j]

            if max_temp > max_sum:
                max_sum = max_temp

    print(max_sum)

def Max2(list_seq):

    N = len(list_seq)
    max_sum = 0
    max_temp = 0
    
    for i in range(N):
        max_temp += list_seq[i]

        if max_temp > max_sum:
            max_sum = max_temp
        elif max_temp < 0:
            max_temp = 0

    print(max_sum)

if __name__ == '__main__':

    list = [5,1,2,3,-2,1,5,10,20,-15,2]

    Max1(list)
    Max2(list)
       