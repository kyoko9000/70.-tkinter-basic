from tkinter import Tk
from tkinter.ttk import Button


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("form")
        self.geometry("320x200")

        # create button, link it to clickExitButton()
        exit_button = Button(self, text="Exit", command=self.clickExitButton)

        # place button at (0,0)
        exit_button.place(x=50, y=60)

    def clickExitButton(self):
        print("exit")
        self.destroy()


if __name__ == "__main__":
    app = Window()
    app.mainloop()