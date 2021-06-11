'''
피카츄
hp(에너지 상태) 0이면 죽음. 30
exp(경험치) 0
lv(경험치 20마다 레벨 1 증가) 1
'''

hp = 30
exp = 0
lv = 1
while True :
    menu = int(input('메뉴입력(1. 밥먹기, 2: 잠자기, 3: 놀기, 4: 운동하기, 5: 종료) : '))
    if menu == 1 :
        print('밥 먹는다')  #hp 5증가
        hp+=5
    elif menu ==2 :
        print('잠잔다')    #hp 10증가
        hp += 10
    elif menu == 3:
        #hp 5감소, exp 7증가 hp감소(죽었나?), exp(레벨업)
        hp -= 5
        if hp <= 0:
            print('죽음')
            break
        print('논다')
        exp += 7
        if exp > 20:
            lv +=1
            exp-=20
            print('lv 업!')
    elif menu == 4:   #hp 15감소, exp 15증가
        hp -= 15
        if hp <= 0:
            print('죽음')
            break
        print('운동한다')
        exp += 15
        if exp > 20:
            lv += 1
            exp -= 20
            print('lv 업!')
    elif menu == 6:
        print('레벨 : ', lv, ', hp : ', hp, ', exp : ',exp)
    else :
        print('종료')
        break #루프 빠져나감
print('계임 종료')
