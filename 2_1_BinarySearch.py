# 二分查找, 递归版本

def binarySearch(list,start,end,target):

    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if list[mid] == target:
            return True
        elif list[mid] < target:
            return binarySearch(list,mid+1,end,target)   # 记住 return
        else:
            return binarySearch(list,start,mid-1,target)

def test(list,target):

    start = 0
    end = len(list) - 1
    
    while start <= end:
        mid = (end + start) // 2
        if list[mid] == target:
            return True
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False

if __name__ == '__main__':

    list = [1,2,3,4,5,6,7,8]

    print(test(list,3))