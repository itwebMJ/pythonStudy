import tkinter as tk
import businfo.BusService as b_info

class AppWin(tk.Frame):
    def __init__(self, root=None, geo=None):
        super().__init__(root)  # 부모 생성자에 기본 윈도우 전달
        self.root = root  # 기본 윈도우를 멤버변수로 저장
        self.root.geometry(geo)  # 윈도우의 크기 및 위치 설정
        self.root.resizable(True, True)  # 윈도우의 가로, 세로 크기 재조정 가능으로 설정
        self.pack()
        self.service = b_info.BusService()
        self.create_widgets()

    def create_widgets(self):  # 원하는 구성요소 부착
        self.title = tk.Label(self, text='버스 정보 앱')
        self.title.pack()

        self.inputData = tk.Entry(self)
        self.inputData.pack()
        self.btn1 = tk.Button(self, text='노선ID로 검색', command=self.handle1)
        self.btn1.pack()
        self.btn2 = tk.Button(self, text='노선ID로 경로 검색', command=self.handle2)
        self.btn2.pack()
        self.btn3 = tk.Button(self, text='버스명 검색', command=self.handle3)
        self.btn3.pack()
        self.btn4 = tk.Button(self, text='노선ID로 정거장 검색', command=self.handle4)
        self.btn4.pack()

        self.content = tk.Label(self, text='')
        self.content.pack()

    def handle1(self):
        busId = self.inputData.get()
        res = self.service.getRouteInfoItem(busId)
        self.content.config(text=res)
        self.inputData.delete(0, tk.END)

    def handle2(self):
        res =''
        busId = self.inputData.get()
        res_list = self.service.getRoutePathList(busId)
        if str(type(res_list)) == "<class 'str'>":
            res = res_list
        else :
            for i in res_list:
                res += i.__str__() + '\n'

        self.content.config(text=res)
        self.inputData.delete(0, tk.END)

    def handle3(self):
        res = ''
        strSrch = self.inputData.get()
        res_list = self.service.getBusRouteList(strSrch)
        if str(type(res_list)) == "<class 'str'>":
            res = res_list
        else :
            for i in res_list:
                res += i.__str__() + '\n'

        self.content.config(text=res)
        self.inputData.delete(0, tk.END)

    def handle4(self):
        res = ''
        busId = self.inputData.get()
        res_list = self.service.getStaionsByRouteList(busId)
        if str(type(res_list)) == "<class 'str'>":
            res = res_list
        else :
            for i in res_list:
                res += i.__str__() + '\n'

        self.content.config(text=res)
        self.inputData.delete(0, tk.END)

