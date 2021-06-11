'''
1. a라는 이름의 리스트를 생성. 숫자 1,2,3,4,5로 초기화해서 생성하시오

2. a의 요소를 하나씩 출력

3. a의 인덱스가 2인 요소의 값을 13으로 변경하시오

4. a의 요소중 짝수만 출력

5. a의 인덱스가 2인 요소를 삭제하시오

6. 이름이 b인 2줄 3칸 리스트를 생성. 모두 0으로 초기화해서 생성

7. 0번줄의 2번방 요소를 10으로 변경하고 출력

8. b의 요소를 0번 줄은 [1,2,3], 1번 줄은 [4,5,6]로 변경

9. b의 모든 요소 출력
'''
a = [0]*5

for i in range(0,5):
    a[i] = i+1
print(a)
for i in range(0,5):
    print(a[i])
print()

a[2] =13
print(a)

for i in range(0,5):
    if a[i] % 2 == 0:
        print(a[i], end=',')
print()
del a[2]
print(a)


b = [[0]*3,[0]*3]

b[0][2]=10
print(b)
num = 1
for j in range(0,2):
    for i in range(0,3):
        b[j][i] =num
        num +=1
print(b)
for j in range(0,2):
    for i in range(0,3):
     print(b[j][i], end=', ')