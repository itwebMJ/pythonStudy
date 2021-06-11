'''
a = [1, 2, 3, 4, 5]
print(a)

a[2] = 30
print(a)

del a[2]
print(len(a))

del a[1:3] #범위로 삭제(1-2)
print(a)

a.remove(1) #값을 찾아서 삭제. 없는 값이면 에러
print(a)

b = [2, 7, 4, 5, 3]
print(b.index(7))

list.sort(b)#정렬
print(b)
'''
'''
index 함수 사용하지 않고
탐색
리스트 10개 숫자 입력받아서 저장
1.최댓값, 최소값,
max= 첫 요소 #가장 큰 값을 담을 변수
max의 값과 각 방의 값을 비교해서 현재 max 값보다  큰 값이면 바로 max 할당

2. 찾고싶은 값 입력받아서 그 값의 위치 출력. 없으면 없다고 출력
s_num = input()
for 배열 길이만큼:
    if s_num ==a[i]:
        있다
    else :
        없다
'''
'''
#1.최댓값, 최소값,
num_list = []
for i in range(0,5):
    num_list.append(int(input('숫자를 입력하시오 : ')))
print(num_list)
max = num_list[0]  # 첫 요소를 할당
min = num_list[0]
'''
'''
for i in range(0, len(num_list)):
        if max < num_list[i] :
            max = num_list[i]
        if min > num_list[i] :
            min = num_list[i]
print('최대값 : ', max, ' /최소값 : ', min)
count_index = -1
#2. 찾고싶은 값 입력받아서 그 값의 위치 출력. 없으면 없다고 출력
s_num = int(input('찾고싶은 값 입력 : '))
for i in range(0, len(num_list)):
    if s_num ==num_list[i]:
        print('있다')
        count_index+=1
    if i == len(num_list)-1 and count_index <0:
        print('없다')
'''
a = [2, 8, 6, 4]
for idx, i in enumerate(a):
    print(idx, ':', i)

#숫자 10개 입력받아 저장
a = []
for i in range(0, 10):
    a.append(int(input('num:')))

print(a)

max = a[0] #첫 요소 할당(초기 기준값). 현재까지 가장 큰 값 저장
max_idx = -1
for idx, i in enumerate(a):  #
    if max < i:#max보다 더 큰 값을 만나면 max를 그 값으로 교체
        max=i
        max_idx=idx
print('max:', max, ' / max위치:', max_idx)


min = a[0]
min_idx = -1
for idx, i in enumerate(a):  #
    if min > i:
        min=i
        min_idx=idx
print('min:', min, ' / min위치:', min_idx)



#순차 탐색
s_num = int(input("검색할 숫자:"))
flag = True#찾았나 표시. 못찾았을때 True,
for idx, i in enumerate(a):
    if s_num == i:
        print(idx,' 방에 있음')
        flag = False
        break
if flag:
    print('not found')

