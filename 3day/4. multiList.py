'''
#다차원 리스트
다차원 리스트는 복잡한 구조와 데이터를 표현하기 위해 사용.
리스트를 요소로 갖는 리스트
'''
'''
a = [[1,2,3],[4,5,6]]
print(a[0])
print(a[1])

for i in a:
    for j in i:
        print(j, end=',')
    print()
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        a[i][j]*=10
        print(a[i][j], end=', ')
    print()
for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        a[i][j] = int(input('num : '))
print(a)
'''
'''
#성적처리 프로그램
3명의 번호, 국, 영, 수 입력받아 각 학생의 총점, 평균 계산해서 결과 출력
번호  국어  영어  수학  총점  평균
1     55   88   55   200   58
2     55   88   55   200   58
3     55   88   55   200   58
a[i].append(j+1)
        a[i].append(int(input('num : ')))
        a[i].append(sum(a[i][1:3]))
        a[i].append(sum(a[i][1:3])/3)
    
'''
score = [[0]*6, [0]*6, [0]*6]
title = ['번호','국어', '영어', '수힉', '총점', '평균']
for i in range(0, 3):
    for j in range(1, 4):
        score[i][j] = int(input(title[j] +' : '))
        score[i][4] +=score[i][j]
    score[i][0] = i+1
    score[i][5] = score[i][4]/3

for i in title:
    print(i, end='\t')
print()

for i in score:
    for j in i:
       print(j, end='\t')
    print()
'''
for i in range(0, len(score)):
    for j in range(0, 3):
        score[i][0] = i+1
        score[i][j+1] = int(input('num : '))
        score[i][4] = sum(score[i][1:4])
        score[i][5] = sum(score[i][1:4])/3
print('번호\t국어\t영어\t수학\t총점\t평균')

for i in score:
    for j in i:
       print(j, end='\t')
    print()
'''