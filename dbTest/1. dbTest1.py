import pymysql

def select():
    conn, cur = None, None

    conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')
    cur = conn.cursor()
    sql = 'select * from departments'
    cur.execute(sql)
    for row in cur:     #커서 객체에서 한줄씩
        print('dept_id : ', row[0], ' / dept_name : ', row[1], ' / manager_id : ', row[2], ' / location_ic : ', row[3])

    conn.close()

def insert():
    conn, cur = None, None

    conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')
    cur = conn.cursor()
    sql = 'insert into departments values(280, "dept test1", null, 1700)'
    cur.execute(sql)
    conn.commit()
    conn.close()

def update():
    conn, cur = None, None

    conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')
    cur = conn.cursor()
    sql = 'update departments set department_name="가나다라", manager_id=100 where department_id=280'
    cur.execute(sql)
    conn.commit()
    conn.close()

def selectById(id):
    conn, cur = None, None
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')
    cur = conn.cursor()
    sql = 'select * from departments where department_id='+str(id)
    cur.execute(sql)
    row = cur.fetchone()
    if row == None:
        print('없는 부서 번호')
    else:
        print('dept_id : ', row[0], ' / dept_name : ', row[1], ' / manager_id : ', row[2], ' / location_ic : ', row[3])
    conn.close()

def delete(id):
    conn, cur = None, None

    conn = pymysql.connect(host='localhost', user='root', password='1234', db='encore', charset='utf8')
    cur = conn.cursor()
    sql = 'delete from departments where department_id='+str(id)
    cur.execute(sql)
    conn.commit()
    conn.close()

def main():
    #insert()
    #select()
    selectById(280)
    delete(280)
    selectById(280)
main()