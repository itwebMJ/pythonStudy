#VO
class Monitor:
    def __init__(self, model='', price=0, amount=0, size=0):
        self.model = model
        self.price = price
        self.amount = amount
        self.size = size

    def __str__(self):
        return 'model:'+self.model+' / price:'+str(self.price)+' / amount:'+str(self.amount)+' / size:'+str(self.size)

#dao+service
#기능 및 저장 작업
#등록: 모니터 정보를 입력받는다 -> Monitor 객체 생성 -> 리스트에 추가함
#검색: 검색할 제품의 모델명을 입력받는다 -> 리스트의 객체들을 하나씩 꺼내서 비교 -> 찾은 결과 반환
#전체출력: 리스트의 모든 객체 출력
#멤버변수:
class MonitorService:
    def __init__(self):
        self.monitors = []  #이 객체의 다수 메서드가 사용하는 값. 멤버 변수는 클래스안에서 전역으로 사용하는 변수

    def addMonitor(self):  #새 모니터 등록. 모니터 데이터를 입력.
        #모니터의 모델명, 가격, 수량, 크기를 키보드로 입력받아 Monitor 객체 생성
        #생성한 객체를 리스트에 추가
        m = input('model:')        #새 모니터 모델 입력
        p = int(input('price:'))   #새 모니터 가격 입력
        a = int(input('amount:'))  #새 모니터 수량 입력
        s = int(input('size:'))   #새 모니터 크기 입력
        mo = Monitor(m, p, a, s)    #방금 입력받은 데이터를 묶어서 Monitor 객체 생성
        self.monitors.append(mo)    #생성한 객체를 리스트에 추가

    #모델명을 파라메터로 받아서 검색하여 검색된 객체 반환
    def getMonitor(self, model):
        #리스트 요소 하나씩 꺼내서 모델명 파라메터와 같은 제품 있으면 반환. 없으면 None 반환
        for i in self.monitors:
            if i.model == model:
                return i    #검색된 객체 반환

    def printMonitor(self):#모델명 입력받아서 똑같은 모니터 객체 찾아서 출력
        # 모델명 입력받아 지역변수에 저장
        name = input('검색할 모델명:')
        mo = self.getMonitor(name)
        if mo==None:
            print('없는 모델명')
        else:
            print(mo)

    def editMonitor(self):
        #수정할 제품 모델명입력받아서 지역변수에 저장
        #제품 검색해서 그 객체를 지역변수에 저장/ 검색했는데 없으면 여기서 종료
        #새 가격과 새 수량을 입력받아서 이 새정보로 객체를 변경
        name = input('수정할 모델명:')
        mo = self.getMonitor(name)
        if mo == None:
            print('없는 모델명. 수정 취소')
        else:
            mo.price = int(input('new price:'))
            mo.amount = int(input('new amount:'))

    def delMonitor(self):
        name = input('삭제할 모델명:')
        mo = self.getMonitor(name)
        if mo == None:
            print('없는 모델명. 삭제 취소')
        else:
            self.monitors.remove(mo)

    def printAll(self):
        for i in self.monitors:
            print(i)

#메뉴 클래스는 메뉴 돌려줄 메서드 하나만 있으면 됨.
#메뉴에서 기능을 선택해서 실행하려면 기능을 제공해주는 서비스 객체 필요. MonitorService를 멤버변수로 생성
class Menu:
    def __init__(self):
        self.service = MonitorService()

    def run(self):
        while True:
            m = int(input('1.모니터등록 2.검색 3.수정 4.삭제 5.전체출력 6.종료'))
            if m==1:
                self.service.addMonitor()
            elif m==2:
                self.service.printMonitor()
            elif m==3:
                self.service.editMonitor()
            elif m==4:
                self.service.delMonitor()
            elif m==5:
                self.service.printAll()
            elif m==6:
                break

def main():
    m = Menu()
    m.run()

main()