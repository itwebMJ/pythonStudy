'''
set : 집합
요소 : 중복  허용 안됨
순서 없음
요소 변경 불가.
셋 자체는 변경 가능(요소 추가/삭제 가능)

'''
'''
s= {1,2,3}
print(s)
print(type(s))

s= {}
print(type(s))
s = set()
print(type(s))

s= {1,2,3}
for i in s :
    print(i)
'''
s= {'aaa',1,False}
print(s)

#s= {1,2,[3,4,5]}  #에러. 변경 가능한 요소를 가질 수 없음

# set 에 요소 추가
s.add('bbb') #요소 한개 추가
print(s)

a = [5, 6, 7]
s.update(a) #요소 여러개 추가
print(s)
'''
'''
#요소 삭제
s.remove('aaa')
s.discard(1) #없는 요소 삭제시 무시.
print(s)

x = s.pop()
print(x, '가 삭제됨')
print(s)

s.clear() #모든 요소 삭제. list에서도 동일
print(s)
##################################

