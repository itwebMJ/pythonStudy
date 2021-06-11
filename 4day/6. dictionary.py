'''
딕셔너리
키와 값을 묶어서 저장
키는 중복허용 안함.갑은 중복되도 됨
키의 타입은 변경불가능한 값. 값의 타입은 제약 없음
요소 추가, 변경, 삭제 가능
'''
'''
d1 = {'name':'aaa', 'age':12, 'flag' : False}
print(d1)
print(type(d1))

d2 = {1:'aaa', 2:'bbb', 3:'ccc'}
print(d2)
print(type(d2))
print('-----------------------')

#요소접근
print(d1['name'])
print(d1['flag'])
print(d2[2])
print('-----------tel추가------------')
#요소 추가
print(d1)
d1['tel'] = '1234'
print(d1)

print('-----------name수정------------')
#수정
d1['name'] = 'bbb'
print(d1)

'''
d1 = {'name':'aaa', 'age':12, 'flag' : False}
#전체 항목 불러오기
items = d1.items()
print(items)
print('-----------items 출력------------')
for i in items:
    print(i)

print('-----------name키 삭제------------')
#요소 삭제
del d1['name']
print(d1)

#딕셔녀리 함수
print('-----------get()------------')
d1['name'] = 'aaa'
print(d1.get('name')) #get(키):키로 검색된 값을 반환

print('-----------keys()------------')
keys = d1.keys()
print(keys)

print('-----------values()------------')
vals = d1.values()
print(vals)

for k in keys :
    vals = d1[k]
    print(k, ':',vals)
print('-----------clear()------------')
d1.clear()
print(d1)


