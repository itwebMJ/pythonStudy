'''a = [2, 8, 6, 4]
for idx, i in enumerate(a):
    print(idx, ':', i)

a=[2,8,6,4]
for idx, i in enumerate(a):
    print('a[',idx,'] = ', )
'''
a = [9,8,7,6,5]

print(a)

for i in a:
    print(i)

#enumerate():반복자. 리스트에서 요소를 하나씩 순서대로 추출하는 것을 반복
#반복적으로 방번호와 요소를 추출해서 반환
'''
for idx, i in enumerate(a):
    print('idx:', idx, ', i:', i)
'''
for idx, i in enumerate(a):
    print('a[',idx,']=',i)

#숫자 10개 입력받아 저장
#a = [0]*10 =>[0,0,0,0,0,0,0,0,0,0]. 인덱스로 값 저장 가능(0~9)
a = []  #빈 리스트 생성.
for i in range(0, 5):#10회 반복.
    a.append(int(input('num:')))

print(a)
#요소 중 최대값 찾기
max = a[0]  #min:최대값을 담을 변수
for i in a:
    if max<i:   #i가 최대값
        max = i
print('max:', max)

#요소 중 최소값 찾기
min = a[0]  #min:최소값을 담을 변수
for i in a:
    if min > i: #i가 최소값
        min = i
print('min:', min)

s_num = int(input("검색할 숫자:"))
flag = True #찾았는지 표시. 못찾았을때 True, 찾았을때 False.
for i in range(0, len(a)):
    if a[i]==s_num:
        print(i, '번째 방에 있음')
        flag = False
        break
if flag:#flag가 True이면 if문은 True가 되므로 실행
    print('not found')