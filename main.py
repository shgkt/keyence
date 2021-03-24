import tkinter
import tkinter.ttk
from PIL import Image, ImageTk
import DragToDrawCanvas
import ParallelLineCanvas


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('tkinter canvas trial')
        self.pack()
        self.create_widgets()
        self.init_canvas()
        self.init_label()

    def create_widgets(self):
        global im

        self.start_x_str = tkinter.StringVar()
        self.start_y_str = tkinter.StringVar()
        self.stop_x_str = tkinter.StringVar()
        self.stop_y_str = tkinter.StringVar()
        self.distance_str = tkinter.StringVar()

        # 画像読み込み
        read_image = Image.open('src/leaf.jpg')
        im = ImageTk.PhotoImage(image=read_image)

    def init_canvas(self):
        self.canvas = tkinter.Canvas(
            self, bg='lightblue', width=300, height=300, highlightthickness=0)
        # self.canvas_obj = DragToDrawCanvas.DragToDrawCanvas(self.canvas)
        self.canvas_obj = ParallelLineCanvas.ParallelLineCanvas(self.canvas)
        self.start_x = self.canvas_obj.start_x
        self.start_y = self.canvas_obj.start_y
        self.stop_x = self.canvas_obj.stop_x
        self.stop_y = self.canvas_obj.stop_y
        self.distance = self.canvas_obj.distance
        self.canvas.create_image(0, 0, anchor='nw', image=im)
        self.canvas.grid(row=0, column=0, rowspan=7)
        self.canvas.bind('<ButtonPress-1>', self.canvas_obj.button_press)

    def init_label(self):
        # 説明ラベル
        self.label_description = tkinter.ttk.Label(self, text='Mouse position')
        self.label_description.grid(row=0, column=1)
        # スタートXラベル
        self.label_start_x = tkinter.ttk.Label(
            self, textvariable='x: ' + self.start_x_str.get())
        self.label_start_x.grid(row=1, column=1)
        # スタートYラベル
        self.label_start_y = tkinter.ttk.Label(
            self, textvariable='y: ' + str(self.start_y))
        self.label_start_y.grid(row=2, column=1)
        # ストップXラベル
        self.label_stop_x = tkinter.ttk.Label(
            self, textvariable='x: ' + str(self.stop_x))
        self.label_stop_x.grid(row=3, column=1)
        # ストップYラベル
        self.label_stop_y = tkinter.ttk.Label(
            self, textvariable='y: ' + str(self.stop_y))
        self.label_stop_y.grid(row=4, column=1)
        # 距離ラベル
        self.label_distance = tkinter.ttk.Label(
            self, textvariable=str(self.distance_str))
        self.label_distance.grid(row=5, column=1)


global im

root = tkinter.Tk()
app = Application(master=root)
app.mainloop()
