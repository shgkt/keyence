import tkinter
import tkinter.ttk
from PIL import Image, ImageTk
import math


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('tkinter canvas trial')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        global im

        self.start_x = tkinter.IntVar()
        self.start_y = tkinter.IntVar()
        self.start_x_str = tkinter.StringVar()
        self.start_y_str = tkinter.StringVar()
        self.stop_x_str = tkinter.StringVar()
        self.stop_y_str = tkinter.StringVar()
        self.distance_str = tkinter.StringVar()
        self.end = tkinter.BooleanVar()
        self.motion_bind_id = tkinter.IntVar()

        # 説明ラベル
        self.label_description = tkinter.ttk.Label(self, text='Mouse position')
        self.label_description.grid(row=0, column=1)
        # スタートXラベル
        self.label_start_x = tkinter.ttk.Label(
            self, textvariable=self.start_x_str)
        self.label_start_x.grid(row=1, column=1)
        # スタートYラベル
        self.label_start_y = tkinter.ttk.Label(
            self, textvariable=self.start_y_str)
        self.label_start_y.grid(row=2, column=1)
        # ストップXラベル
        self.label_stop_x = tkinter.ttk.Label(
            self, textvariable=self.stop_x_str)
        self.label_stop_x.grid(row=3, column=1)
        # ストップYラベル
        self.label_stop_y = tkinter.ttk.Label(
            self, textvariable=self.stop_y_str)
        self.label_stop_y.grid(row=4, column=1)
        # 距離ラベル
        self.label_distance = tkinter.ttk.Label(
            self, textvariable=self.distance_str)
        self.label_distance.grid(row=5, column=1)

        # 画像読み込み
        read_image = Image.open('src/leaf.jpg')
        im = ImageTk.PhotoImage(image=read_image)
        self.canvas = tkinter.Canvas(
            self, bg='lightblue', width=300, height=300, highlightthickness=0)
        self.canvas.create_image(0, 0, anchor='nw', image=im)
        self.canvas.grid(row=0, column=0, rowspan=7)
        self.canvas.bind('<ButtonPress-1>', self.button_press)

    def button_press(self, event):
        self.end = not self.end
        if self.end is not True:
            self.start_x.set(event.x)
            self.start_y.set(event.y)
            self.start_x_str.set('x : ' + str(event.x))
            self.start_y_str.set('y : ' + str(event.y))
            self.stop_x_str.set('')
            self.stop_y_str.set('')
            self.distance_str.set('')
            self.motion_bind_id = self.canvas.bind(
                '<Motion>', self.button_move)
        else:
            self.stop_x_str.set('x : ' + str(event.x))
            self.stop_y_str.set('y : ' + str(event.y))
            self.draw_line(self.start_x.get(),
                           self.start_y.get(), event.x, event.y, "black")
            self.canvas.unbind('<Motion>', self.motion_bind_id)

    def button_move(self, event):
        self.stop_x_str.set('x : ' + str(event.x))
        self.stop_y_str.set('y : ' + str(event.y))
        self.distance_str.set(str(self.get_distance(
            event.x, event.y, self.start_x.get(), self.start_y.get())))

    def get_distance(self, x1, y1, x2, y2):
        d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 1)
        return d

    def draw_line(self, x1, y1, x2, y2, color):
        self.canvas.create_line(x1, y1, x2, y2, fill=color)


global im

root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
