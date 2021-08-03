import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk

class AppWin(tk.Frame):#AppWin은 Frame(위젯을 배치하는 판)
    def __init__(self, root=None, geo=None): #root:Tk()객체 geo=창크기위치
        #fr = tk.Frame(self.root)
        super().__init__(root)      # 부모 생성자에 기본 윈도우 전달
        self.root = root            # 기본 윈도우를 멤버변수로 저장
        self.root.geometry(geo)     # 윈도우의 크기 및 위치 설정
        self.root.resizable(True, True)  # 윈도우의 가로, 세로 크기 재조정 가능으로 설정
        self.pack()
        self.sub_fr = None          #버튼 배치할 하위 프레임
        self.img_src = None         #레이블에 출력할 이미지 값
        self.img_label = None       #이미지 출력할 레이블
        self.ent_title = None
        self.fileName_ent = None    #이미지 저장시 파일명 입력받을 엔트리
        self.service = None         #카메라 앱 기능이 구현된 서비스 객체 생성
        self.flag = None
        self.create_widgets()

    def read_img(self, path):#path:읽을 이미지 경로
        src = cv2.imread(path)
        src = cv2.resize(src, (640, 400))#이미지 가로,세로 크기 조절
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB) #opencv[b, g, r] => tkinter:[r, g, b]
        img = Image.fromarray(img)  #opencv용 이미지배열값을 필로우용 이미지로 변환
        self.img_src = ImageTk.PhotoImage(image=img) #tkinter용 이미지 변환

    def read_cam(self, path):  # path:읽을 이미지 경로
        pass
    def create_widgets(self):  # 원하는 구성요소 부착
        self.read_img('start.jpg')
        self.img_label = tk.Label(self, image=self.img_src)
        self.img_label.pack()
        self.ent_title = tk.Label(self, text='파일명:')
        self.ent_title.pack()
        self.fileName_ent = tk.Entry(self, width=60)
        self.fileName_ent.pack()
        self.sub_fr = tk.Frame(self)
        self.sub_fr.pack()

        self.btn1 = tk.Button(self.sub_fr, text='사진촬영')
        self.btn2 = tk.Button(self.sub_fr, text='저장')
        self.btn3 = tk.Button(self.sub_fr, text='동영상시작')
        self.btn4 = tk.Button(self.sub_fr, text='동영상종료')

        self.btn1.grid(row=0, column=0)
        self.btn2.grid(row=0, column=1)
        self.btn3.grid(row=0, column=2)
        self.btn4.grid(row=0, column=3)


