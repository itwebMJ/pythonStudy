'''
피카츄
hp(에너지 상태) 0이면 죽음. 30
exp(경험치) 0
lv(경험치 20마다 레벨 1 증가) 1
'''
'''
#피카추 게임
def 밥먹음(hp_val):
    print('피카추 밥먹음')
    hp_val += 5
    return hp_val

def 잠잠(hp_val):
    print('피카추 잠잠')
    hp_val += 10
    return hp_val

def 놀기(hp_val, exp_val, lv_val):
    print('피카추 논다')
    hp_val -= 8
    flag = hp_val>0
    if flag:
        exp_val += 5
        if exp_val>=20:#경험치가 20 채워졌나?
            lv_val+=1 #채워졌으면 레벨 1증가
            exp_val-=20 #경험치 20감소
            print('레벨 1 증가하였음')
    return hp_val, flag, exp_val, lv_val #파이썬은 여러개의 값을 반환할 수 있음. 튜플로 반환

def 운동하기(hp_val, exp_val, lv_val):
    print('피카추 운동함')
    hp_val -= 15
    flag = hp_val > 0
    if flag:
        exp_val += 10
        if exp_val >= 20:  # 경험치가 20 채워졌나?
            lv_val += 1  # 채워졌으면 레벨 1증가
            exp_val -= 20  # 경험치 20감소
            print('레벨 1 증가하였음')
    return hp_val, flag, exp_val, lv_val  # 파이썬은 여러개의 값을 반환할 수 있음. 튜플로 반환

def printInfo(hp_val, exp_val, lv_val):
    print('캐릭터 상태')
    print('hp:', hp_val)
    print('exp:', exp_val)
    print('lv:', lv_val)

def main():
    hp = 30 #함수 안에서 선언. 지역변수
    exp = 0
    lv = 1
    flag = True
    while flag:
        menu = input('1.밥먹기 2.잠자기 3.운동하기 4.놀기 5.상태확인 6.종료')
        if menu=='1':
            hp = 밥먹음(hp)
        elif menu=='2':
            hp = 잠잠(hp)
        elif menu=='3':
            hp, flag, exp, lv = 운동하기(hp, exp, lv)       #캐릭터 죽으면 루프를 빠져나감
        elif menu == '4':
            hp, flag, exp, lv = 놀기(hp, exp, lv)           #캐릭터 죽으면 루프를 빠져나감
        elif menu == '5':
            printInfo(hp, exp, lv)
        elif menu == '6':
            print('게임 종료')
            break
        if not flag:
            print('캐릭터 사망')


main()
'''

hp = 30
exp = 0
lv = 1

def 밥먹기():
    global hp   #hp는 전역변수다.
    print('피카추 밥먹음')
    hp += 5

def 잠자기():
    global hp  # hp는 전역변수다.
    print('피카추 잠잠')
    hp += 10

def 놀기():
    global hp, exp  # hp는 전역변수다.
    print('피카추 놀기')
    hp -= 8 #에너지 소모
    flag = hp>0 #flag 살았나 죽었나 확인
    if flag:
        exp += 5
        레벨체크()
    return flag

def 운동하기():
    global hp, exp  # hp는 전역변수다.
    print('피카추 운동하기')
    hp -= 15  # 에너지 소모
    flag = hp > 0  # flag 살았나 죽었나 확인
    if flag:
        exp += 10
        레벨체크()
    return flag

def 상태확인():
    print('피카추 상태확인')
    print('hp:', hp)
    print('exp:', exp)
    print('level:', lv)

def 레벨체크():
    global exp, lv
    if exp>=20:
        lv+=1
        exp-=20
        print('레벨 1 증가함')

def main():
    flag = True
    while flag:
        menu = input('1.밥먹기 2.잠자기 3.운동하기 4.놀기 5.상태확인 6.종료')
        if menu == '1':
            밥먹기()
        elif menu == '2':
            잠자기()
        elif menu == '3':
            flag = 운동하기()  # 캐릭터 죽으면 루프를 빠져나감
        elif menu == '4':
            flag = 놀기()  # 캐릭터 죽으면 루프를 빠져나감
        elif menu == '5':
            상태확인()
        elif menu == '6':
            print('게임 종료')
            break
        if not flag:
            print('캐릭터 사망')

main()
