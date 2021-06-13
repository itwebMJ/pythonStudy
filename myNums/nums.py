nums = []

#숫자를 nums 리스트에 저장
def addNum1():
    num = int(input('num:'))
    #nums = 'aaa'#새 지역변수(str 타입)
    nums.append(num)  #전역 객체를 사용하여 메서드 호출. global 필요없음

def addNum2(num): #함수 호출할때 값 하나를 괄호에 넣어서 호출해라
    print('addNum2() 호출됨')
    nums.append(num)

def printNums():
    print('printNums() 호출됨')
    print('숫자 개수:', len(nums))
    for i in nums:
        print(i, end=', ')
    print()

#탐색함수: 탐색한 결과 리턴
# 파라메터 받을 수도 있고 / 함수 안에서 직접 키보드로 입력 받을 수도 있다
#0번방부터 마지막방까지 요소를 하나씩 꺼내 찾을 값과 비교. 같은 값 있으면 루프 빠져나옴
def search1(num): #검색할 값을 파라메터로 받음
    print('search1() 호출됨')
    for idx, i in enumerate(nums):#i는 요소
        if i==num:
            return idx

def search2(num):
    print('search2() 호출됨')
    for i in range(0, len(nums)):#i는 인덱스
        if nums[i] == num:
            return i

def search3():
    print('search3() 호출됨')
    num = int(input('찾고 싶은 num:'))
    for i in range(0, len(nums)):#i는 인덱스
        if nums[i] == num:
            return i

def search4():
    print('search4() 호출됨')
    num = int(input('찾고 싶은 num:'))
    idx = search2(num)
    printIdx(idx)

def printIdx(idx):
    print('printIdx() 호출됨')
    if idx==None:
        print('not found')
    else:
        print(idx, '위치에 있음')

#삭제함수. 2개 (파람있음. 파람없음)
def delNum1(num):
    print('delNum1() 호출됨')
    if num in nums: #in 연산자: 오른쪽의 리스트에서 왼쪽값이 포함되어 있으면 True, 없으면 False반환
        nums.remove(num)
    else:
        print('없는 숫자. 삭제 취소')

def delNum2():
    print('delNum2() 호출됨')
    num = int(input('삭제할 숫자:'))
    try:
        nums.remove(num) #값을 찾아서 삭제. 값이 없으면 예외발생
    except:
        print('없는 숫자. 삭제 취소')

    '''
    if num in nums:
        nums.remove(num)
    else:
        print('없는 숫자. 삭제 취소')
    '''