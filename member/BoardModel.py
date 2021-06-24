import pymysql
import member.MemModel as mem

class BoardVo:
    def __init__(self, num=None, writer=None, w_date=None, title=None, content=None):
        self.num = num
        self.writer = writer
        self.w_date = w_date
        self.title = title
        self.content = content

    def __str__(self):
        return 'num : '+str(self.num)+' / writer : '+self.writer+' / date : '+str(self.w_date)+\
                                    ' / title : '+self.title+' / content : '+self.content

class BoardDao:
    def __init__(self):
        self.conn = None

    # db연결 함수
    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')

    # db닫는 함수
    def disconnect(self):
        self.conn.close()

    def insert(self, vo):
        self.connect()  #db 연결
        cur = self.conn.cursor()    #사용할 커서 객체 생성
        sql = 'insert into board(writer, w_date, title, content) values(%s, now(), %s, %s)'   #변수가 들어갈 위치에 %s와 같은 문자포맷 지정
        vals = (vo.writer, vo.title, vo.content)
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectAll(self):
        boards = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from board'
        try:
            cur.execute(sql)
            for row in cur:
                boards.append(BoardVo(row[0], row[1], row[2], row[3], row[4]))
            return boards
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByNum(self, num):
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from board where num=%s'
        vals = (num,)    #튜플
        try:
            cur.execute(sql, vals)
            row = cur.fetchone()
            if row != None:
                vo = BoardVo(row[0], row[1], row[2], row[3], row[4])
                return vo
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByWriter(self, writer):
        boards = []
        self.connect()
        cur = self.conn.cursor()
        sql = 'select * from board where writer=%s'
        vals = (writer,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                boards.append(BoardVo(row[0], row[1], row[2], row[3], row[4]))
            return boards
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByTitle(self, title):
        boards = []
        self.connect()
        cur = self.conn.cursor()
        title = '%' +title+'%'
        sql = 'select * from board where title like %s'
        vals = (title,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                boards.append(BoardVo(row[0], row[1], row[2], row[3], row[4]))
            return boards
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def selectByContent(self, content):
        boards = []
        self.connect()
        cur = self.conn.cursor()
        content = '%' + content + '%'
        sql = 'select * from board where content like %s'
        vals = (content,)
        try:
            cur.execute(sql, vals)
            for row in cur:
                boards.append(BoardVo(row[0], row[1], row[2], row[3], row[4]))
            return boards
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def editBoard(self, vo):
        self.connect()
        cur = self.conn.cursor()
        sql = 'update board set title=%s, content=%s where num=%s'
        vals = (vo.writer, vo.title, vo.content)  # 튜플
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

    def delBoard(self, num):
        self.connect()
        cur = self.conn.cursor()
        sql = 'delete from board where num=%s'
        vals = (num,)  # 튜플
        try:
            cur.execute(sql, vals)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.disconnect()

class BoardService:
    def __init__(self):
        self.dao = BoardDao()

    def addBoard(self):
        print('글작성')
        title = input('title : ')
        content = input('content : ')
        writer = mem.MemService.login_id    #작성자 : 로그인 아이디
        try:
            self.dao.insert(BoardVo(writer=writer, title=title, content=content)) # db에 id, pwd, name, email 저장
        except Exception as e:
            print(e)
        else:
            print('작성 완료')

    def getAll(self):
        print('글목록')
        boards = self.dao.selectAll()
        for b in boards:
            print(b)

    def getByNum(self):
        print('글 번호로 검색')
        num = int(input('글 번호 : '))
        vo = self.dao.selectByNum(num)
        if vo == None:
            print('없는 글')
        else:
            print(vo)

    def printList(self, vo_list):
        if vo_list ==None or len(vo_list) ==0:
            print('검색 결과 없음')
        else:
            for b in vo_list:
                print(b)

    def getByWriter(self):
        print('작성자로로 검색')
        writer = input('글 번호 : ')
        vo_list = self.dao.selectByWriter(writer)
        self.printList(vo_list)

    def getByTitle(self):
        print('제목으로 검색')
        title = input('글 제목 : ')
        vo_list = self.dao.selectByTitle(title)
        self.printList(vo_list)

    def getByContent(self):
        print('내용으로 검색')
        content = input('내용 : ')
        vo_list = self.dao.selectByContent(content)
        self.printList(vo_list)

    def editBoard(self):
        print('글 수정')
        num = input('수정할 글 번호:')
        vo = self.dao.selectByNum(num)
        if vo==None:
            print('없는 글번호')
        else:
            if mem.MemService.login_id == vo.writer:
                title = input('new title:')
                content = input('new content:')
                line = self.dao.editBoard(BoardVo(num=num, title=title, content=content))
                print(line, '줄이 수정됨')
            else:
                print('남의 글은 수정할 수 없음')

    def delBoard(self):
        print('글 삭제')
        num = input('삭제할 글 번호:')
        vo = self.dao.selectByNum(num)
        if vo == None:
            print('없는 글번호')
        else:
            if mem.MemService.login_id == vo.writer:
                line = self.dao.delBoard(num)
                print(line, '줄이 삭제됨')
            else:
                print('남의 글은 삭제할 수 없음')