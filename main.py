from tkinter import Tk
from tkinter.ttk import Button, Label


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("form")
        self.geometry("400x300")

        # create button, link it to clickExitButton()
        exit_button = Button(self, text="Exit", command=self.recive)
        # place button at (0,0)
        exit_button.place(x=50, y=100)
        # show a label
        self.label = Label(self,
                      text='This is a label',
                      font=('arial', 30, 'bold'))
        self.label.place(x=50, y=10)

    def recive(self):
        self.label.config(text="hi")
        # print("exit")
        # self.destroy()


if __name__ == "__main__":
    app = Window()
    app.mainloop()