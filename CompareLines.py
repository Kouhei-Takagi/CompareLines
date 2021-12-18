import tkinter
from tkinter import messagebox
from tkinter import scrolledtext
import difflib

class UI(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        def btn_click():
            text1 = txtA.get('1.0', 'end -1c')
            text2 = txtB.get('1.0', 'end -1c')
            if text1 == text2:
                messagebox.showinfo("Result", "True")
            else:
                res = difflib.ndiff(text1.split(), text2.split())
                finalRes = '\n'.join(res)
                #print(finalRes)
                messagebox.showinfo("Result", f"{finalRes}")

        master.geometry('500x300')
        master.title('A or A\'')

        txtA = scrolledtext.ScrolledText(height=15, width=20)
        txtA.place(x=5, y=5)

        txtB = scrolledtext.ScrolledText(height=15, width=20)
        txtB.place(x=300, y=5)

        btn = tkinter.Button(text='Compare', command=btn_click)
        btn.place(x=200, y=120)


def main():
    window = tkinter.Tk()
    app = UI(master=window)
    app.mainloop()

if __name__ == '__main__':
    main()
