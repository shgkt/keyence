import math
import tkinter


class DragToDrawCanvas:
    def __init__(self, canvas):
        self.canvas = canvas
        self.start_x = tkinter.IntVar()
        self.start_x_str = tkinter.StringVar()
        self.start_y = tkinter.IntVar()
        self.stop_x = tkinter.IntVar()
        self.stop_y = tkinter.IntVar()
        self.distance = tkinter.IntVar()
        self.end = tkinter.BooleanVar()
        self.motion_bind_id = tkinter.IntVar()

    def button_press(self, event):
        self.end = not self.end
        if self.end is not True:
            self.start_x.set(event.x)
            self.start_x_str.set(str(event.x))
            self.start_y.set(event.y)
            self.motion_bind_id = self.canvas.bind(
                '<Motion>', self.button_move)
            self.draw_line(self.start_x.get(),
                           self.start_y.get(), event.x, event.y, "black")
        else:
            self.canvas.unbind('<Motion>', self.motion_bind_id)

    def button_move(self, event):
        self.distance = self.get_distance(
            event.x, event.y, self.start_x.get(), self.start_y.get())
        self.canvas.delete(self.drawing_line)
        self.draw_line(self.start_x.get(),
                       self.start_y.get(), event.x, event.y, "black")

    def get_distance(self, x1, y1, x2, y2):
        d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 1)
        return d

    def draw_line(self, x1, y1, x2, y2, color):
        self.drawing_line = self.canvas.create_line(x1, y1, x2, y2, fill=color)
