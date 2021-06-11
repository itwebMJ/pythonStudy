#copy 패키지 불러옴
import copy
a= [1,2,3]
b = a

a[2] = 30
print(a)
print(b)
print('--------')
a= [1,2,3 ]
b = copy.copy(a)
a[2] = 30
print(a)
print(b)
print('--------')
################
a = [1,2,[4,5,6]]
b= copy.copy(a)
a[2][0] =40
print(a)
print(b)
print('--------')
################
a = [1,2,[4,5,6]]
b= copy.deepcopy(a)
a[2][0] =40
print(a)
print(b)
