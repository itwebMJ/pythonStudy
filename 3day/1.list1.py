'''
a = [1,2,3]
b = ['asdasd', 'trert']
c = [12.34, 56]
d = [True, True, False]

e = []

print(a[0]) #리스트의 0번방 값 출력
print(a[1])
print(a[2])

for i in range(0, 3):
    print(a[i],end='')
print()

for i in a:
    print(i,end='')
print()
'''
'''
b = ['aaa', 'bbb', 'ccc']
print('b의 길이 : ', len(b))
print('asdfgh의 길이 : ', len('asdfgh'))
print('b의 요소 출력 : ')
for i in range(0, len(b)):
    print(b[i], end=', ')
print()

for i in b:
    print(i, end=', ')
print()
'''

#숫자 10개를 입력받아 리스트에 저장한 뒤 출력
num =[]
for i in range(1, 11):
    num.append(int(input('숫자 입력 : ')))
for i in range(0, len(num)):
    print(num[i], end=', ')
print()

#5명의 점수를 입력받아 총점과 평균 출력
score = [0]*5
sum1 = 0
for i in range(0,5):
    score[i] = int(input('score : '))
    sum1 += score[i]
avg1 = sum1/len(score)
print('총점 : ',sum1,'/ 평균 : ',avg1)

s = sum(score)

print('총점 : ',s)

