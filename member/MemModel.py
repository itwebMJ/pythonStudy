import pymysql

class MemVo:
    def __init__(self, id=None, pwd=None, name=None, email=None):
        self.id = id
        self.pwd = pwd
        self.name = name
        self.email = email

    def __str__(self):
        return 'id : ' + self.id + ' / pwd : ' + self.pwd + ' / name : ' + self.name + ' / email : ' + self.email

class MemDao:   #db작업 구현
    def __init__(self):
        self.conn = None

    #db연결 함수
    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')

    # db닫는 함수
    def disconnect(self):
        self.conn.close()

    def insert(self, vo):
        self.connect()  #db 연결
        cur = self.conn.cursor()    #사용할 커서 객체 생성
        # sql = "insert into member values('vo.id', %s, %s, %s)"
        sql = 'insert into member values(%s, %s, %s, %s)'   #변수가 들어갈 위치에 %s와 같은 문자포맷 지정
        vals = (vo.id, vo.pwd, vo.name, vo.email)
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

    def select(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from member where id=%s'
        vals = (id,)    #튜플
        cur.execute(sql, vals)
        row = cur.fetchone()
        self.disconnect()
        if row != None:
            vo = MemVo(row[0], row[1], row[2], row[3])
            return vo

    def update(self, id, new_pwd):
        self.connect()
        cur = self.conn.cursor()
        sql = 'update member set pwd=%s where id=%s'
        vals = (new_pwd, id)    #튜플
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

    def delete(self, id):
        self.connect()
        cur = self.conn.cursor()
        sql = 'delete from member where id=%s'
        vals = (id,)  # 튜플
        cur.execute(sql, vals)
        self.conn.commit()
        self.disconnect()

class MemService:
    login_id = None     #로그인 여부. 로그인 유지

    def __init__(self):
        self.dao = MemDao()

    def join(self):
        print('회원가입')
        id = input('id : ')
        pwd = input('pwd : ')
        name = input('name : ')
        email = input('email : ')
        try:
            self.dao.insert(MemVo(id, pwd, name, email)) # db에 id, pwd, name, email 저장
        except Exception as e:
            print(e)
        else:
            print('회원가입 완료')

    def login(self):
        print('로그인')
        if MemService.login_id != None:
            print('이미 로그인 중')
            return

        id = input('id : ')
        pwd = input('pwd : ')
        vo = self.dao.select(id)
        if vo == None:
            print('없는 아이디')
        else:
            if pwd == vo.pwd:
                print('로그인 성공')
                MemService.login_id = id
            else:
                print('패스워드 불일치')

    def logout(self):
        print('로그아웃')
        if MemService.login_id ==None:
            print('로그인을 먼저 하시오')
            return
        MemService.login_id = None

    def printMyInfo(self):
        print('내 정보 확인')
        if MemService.login_id == None:
            print('로그인을 먼저 하시오')
            return
        vo = self.dao.select(MemService.login_id)
        print(vo)

    def editMyInfo(self):
        print('내 정보 수정')
        if MemService.login_id == None:
            print('로그인을 먼저 하시오')
            return
        pwd = input('pwd : ')
        try:
            self.dao.update(MemService.login_id, pwd)
        except Exception as e:
            print(e)
        else:
            print('수정 완료')

    def delMyInfo(self):
        print('탈퇴')
        if MemService.login_id == None:
            print('로그인을 먼저 하시오')
            return
        self.dao.delete(MemService.login_id)
        MemService.login_id = None

