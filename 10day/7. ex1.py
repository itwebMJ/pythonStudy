'''
정보
제품번호:자동할당
제품명
가격
수량
'''

class Product: #VO
    '''
    def __init__(self, num=0, name='', price=0, amount=0):
        self.num = num
        self.name = name
        self.price = price
        self.amount = amount
    '''
    cnt = 0  #클래스변수. 이 클래스로 만든 모든 객체가 공유
    def __init__(self, name='', price=0, amount=0):
        Product.cnt += 1    #이 객체 생성될때마다 cnt 1씩 증가
        self.num = Product.cnt #번호 자동 할당
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return 'num:'+str(self.num)+' / name:'+self.name+' / price:' + str(self.price)\
               +' / amount:' + str(self.amount)

#저장소에 추가, 수정, 검색, 삭제
class Dao:
    def __init__(self):
        self.prods = []

    def insert(self, p):
        self.prods.append(p)

    def select(self, num):
        for i in self.prods:
            if i.num == num:
                return i

    def selectAll(self):
        return self.prods

    def delete(self, num):
        p = self.select(num)
        if p!=None:
            self.prods.remove(p)
            return True
        return False

class Service:#사용자에 제공할 기능 구현
    def __init__(self):
        self.dao = Dao()

    def addProduct(self):
        print('제품등록')
        name = input('name:')
        price = int(input('price:'))
        amount = int(input('amount:'))
        p = Product(name, price, amount)
        self.dao.insert(p)


    def printProduct(self):
        print('제품검색')
        num = int(input('검색할 제품 번호:'))
        p = self.dao.select(num)
        if p==None:
            print('없는 제품')
        else:
            print(p)

    def printAll(self):
        print('제품목록')
        ps = self.dao.selectAll()
        for i in ps:
            print(i)

    def editProduct(self):
        print('제품수정')
        num = int(input('수정할 제품 번호:'))
        p = self.dao.select(num)
        if p == None:
            print('없는 제품. 수정 취소')
        else:
            p.price = int(input('new price:'))
            p.amount = int(input('new amount:'))

    def delProduct(self):
        print('제품삭제')
        num = int(input('삭제할 제품 번호:'))
        flag = self.dao.delete(num)
        if flag:
            print('삭제완료')
        else:
            print('없는 제품번호. 삭제 취소')

class Menu:
    def __init__(self):
        self.service = Service()

    def run(self):
        while True:
            m = input('1.추가 2.검색 3.수정 4.삭제 5.전체목록 6.종료')
            if m=='1':
                self.service.addProduct()
            elif m=='2':
                self.service.printProduct()
            elif m=='3':
                self.service.editProduct()
            elif m=='4':
                self.service.delProduct()
            elif m=='5':
                self.service.printAll()
            elif m=='6':
                break

def main():
    m = Menu()
    m.run()

main()