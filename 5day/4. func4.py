def printListArr(arr):
    for i in arr:
        print(i, end=', ')
    print()

def printSumMaxMin(arr):
    print('리스트의 합 : ', sumList(arr))
    print('최댓값 : ', maxList(arr))
    print('최솟값 : ', minList(arr))

def main(): #main함수. 프로그램의 시작점
    a= [1,2,3,4,5]
    printListArr(a)
    printSumMaxMin(a)

    b = [9,8,7,6,5]
    printListArr(b)
    printSumMaxMin(b)
def sumList(arr):
    sumArr = 0
    for i in arr:
        sumArr += i
    return sumArr

def maxList(arr):
    max = arr[0] #첫 요소를 max값으로 초기화,  리스트 요소와 하나씩 비교하면서 더 큰값을 만나면 바로 max로 교체
    for i in range(0, len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max
def  minList(arr):
    min = arr[0]
    for i in range(0, len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min
#main() 호출
main()
