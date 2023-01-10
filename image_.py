from tkinter import Tk
from tkinter.ttk import Button, Label

from PIL import ImageTk, Image


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("form")
        self.geometry("400x300")

        # create button, link it to receive()
        exit_button = Button(self, text="Exit", command=self.receive)
        # place button at (0,0)
        exit_button.place(x=50, y=250)
        # show a label
        self.label = Label(self,
                      text='This is a label',
                      font=('arial', 30, 'bold'))
        self.label.place(x=50, y=10)

    def receive(self):
        img = Image.open("1.jpg")
        # zoom = 2
        # pixels_x, pixels_y = img.size
        # img = img.resize((round(pixels_x/zoom), round(pixels_y/zoom)))
        img = img.resize((300, 200))
        photo = ImageTk.PhotoImage(img)
        self.label.configure(image=photo)
        self.label.image = photo


if __name__ == "__main__":
    app = Window()
    app.mainloop()