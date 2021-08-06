import tkinter as tk
import cv2
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import numpy as np

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
        self.pic_src = None         #카메라로 찍은 영상 원본
        self.src = None             #저장할 이미지
        self.create_widgets()

    def read_img(self, src):
        self.src = src
        src = cv2.resize(src, (640, 400))#이미지 가로,세로 크기 조절
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB) #opencv[b, g, r] => tkinter:[r, g, b]
        img = Image.fromarray(img)  #opencv용 이미지배열값을 필로우용 이미지로 변환
        self.img_src = ImageTk.PhotoImage(image=img) #tkinter용 이미지 변환
        self.img_label['image'] = self.img_src

    def btn1_handler(self):
        cap = cv2.VideoCapture(0)
        ret, src = cap.read()
        if ret:
            self.read_img(src)
            self.pic_src = src
        cap.release()

    def btn2_handler(self):
        fname = self.fileName_ent.get()  # 엔트리에 입력한 파일명
        if fname == '' or fname == None:
            tk.messagebox.showinfo(title='오류', message='파일명 누락')
            return
        cv2.imwrite('pic/' + fname + '.jpg', self.src)
        self.fileName_ent.delete(0, tk.END)

    def btn3_handler(self):
        kernel = np.array([-1,-1,0,-1,0,1,0,1,1]).reshape((3,3))
        filter_dst = cv2.filter2D(self.pic_src, -1, kernel, None, (-1,-1), 128)
        self.read_img(filter_dst)

    def btn4_handler(self):
        size = 5
        kernel = np.zeros((size, size))
        kernel[int((size - 1) / 2), :] = np.ones(size)
        kernel = kernel / size
        filter_dst = cv2.filter2D(self.pic_src, -1, kernel)
        self.read_img(filter_dst)

    def btn5_handler(self):
        filter_dst = cv2.GaussianBlur(self.pic_src, (5,5), 5)
        self.read_img(filter_dst)

    def btn6_handler(self):
        blur = cv2.GaussianBlur(self.pic_src, (5,5), 5)
        filter_dst = np.clip(2.0*self.pic_src - blur, 0, 255).astype('uint8')
        self.read_img(filter_dst)

    def btn7_handler(self):
        x = self.pic_src.copy().astype('int8')
        cv2.randn(x, 0, 0.2)
        x = x.astype('uint8')
        filter_dst = cv2.add(self.pic_src, x)
        self.read_img(filter_dst)

    def btn8_handler(self):
        filter_dst = cv2.medianBlur(self.pic_src, 5)
        self.read_img(filter_dst)

    def btn9_handler(self):
        fname = self.fileName_ent.get()  # 엔트리에 입력한 파일명
        if fname == '' or fname == None:
            tk.messagebox.showinfo(title='오류', message='파일명 누락')
            return
        self.pic_src = cv2.imread('pic/'+fname+'.jpg')
        self.read_img(self.pic_src)

    def create_widgets(self):  # 원하는 구성요소 부착
        self.img_label = tk.Label(self, image=self.img_src)
        self.img_label.pack()
        self.ent_title = tk.Label(self, text='파일명:')
        self.ent_title.pack()
        self.fileName_ent = tk.Entry(self, width=60)
        self.fileName_ent.pack()
        self.sub_fr = tk.Frame(self)
        self.sub_fr.pack()
        src = cv2.imread('start.jpg')  # 이미지 파일에서 영상 읽음
        self.read_img(src)

        self.btn1 = tk.Button(self.sub_fr, text='사진촬영')
        self.btn2 = tk.Button(self.sub_fr, text='저장')
        self.btn3 = tk.Button(self.sub_fr, text='엠보싱')
        self.btn4 = tk.Button(self.sub_fr, text='모션블러')
        self.btn5 = tk.Button(self.sub_fr, text='블러')
        self.btn6 = tk.Button(self.sub_fr, text='샤프닝')
        self.btn7 = tk.Button(self.sub_fr, text='잡티추가')
        self.btn8 = tk.Button(self.sub_fr, text='잡티제거')
        self.btn9 = tk.Button(self.sub_fr, text='사진보기')

        #버튼 그리드 배치
        self.btn1.grid(row=0, column=0)
        self.btn2.grid(row=0, column=1)
        self.btn3.grid(row=0, column=2)
        self.btn4.grid(row=0, column=3)
        self.btn5.grid(row=1, column=0)
        self.btn6.grid(row=1, column=1)
        self.btn7.grid(row=1, column=2)
        self.btn8.grid(row=1, column=3)
        self.btn9.grid(row=2, column=0)

        #버튼에 핸들러 등록
        self.btn1['command'] = self.btn1_handler
        self.btn2['command'] = self.btn2_handler
        self.btn3['command'] = self.btn3_handler
        self.btn4['command'] = self.btn4_handler
        self.btn5['command'] = self.btn5_handler
        self.btn6['command'] = self.btn6_handler
        self.btn7['command'] = self.btn7_handler
        self.btn8['command'] = self.btn8_handler
        self.btn9['command'] = self.btn9_handler