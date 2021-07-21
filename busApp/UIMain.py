import AppWindow as a
import tkinter as tk

def main():
    win = tk.Tk()
    app = a.AppWin(win, '500x600+100+100')
    app.mainloop()

main()
