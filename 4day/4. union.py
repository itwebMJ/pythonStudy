#합집합
s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1 | s2
print(s3)

s4 = s1.union(s2)
print(s4)

#교집합
s3 = s1 & s2
print('교집합', s3)

#차집합
s3 = s1 - s2
print('차집합', s3)

s4 = s2 - s1
print(s4)

s5 = s1.difference(s2)
print(s5)