import math
import tkinter


class ParallelLineCanvas:
    def __init__(self, canvas):
        self.canvas = canvas
        self.start_x = tkinter.IntVar()
        self.start_x_str = tkinter.StringVar()
        self.start_y = tkinter.IntVar()
        self.stop_x = tkinter.IntVar()
        self.stop_y = tkinter.IntVar()
        self.distance = tkinter.IntVar()
        self.motion_bind_id = tkinter.IntVar()
        self.end = True
        self.second_line = False
        self.line = []
        # 直線の式保持用 ax + by + c
        self.a = 0
        self.b = 0
        self.c = 0
        # 直線を伸ばすための値
        self.times = 1000
        self.slope = 0

    def button_press(self, event):
        # 2本目モード
        if self.second_line:
            self.end = True
            self.second_line = False
            self.line.append(self.draw_second_line(event))
            self.canvas.unbind('<Motion>', self.motion_bind_id)
            return

        # 1本目モード
        self.end = not self.end
        if self.end is not True:
            self.start_x.set(event.x)
            self.start_x_str.set(str(event.x))
            self.start_y.set(event.y)
            self.motion_bind_id = self.canvas.bind(
                '<Motion>', self.button_move)
            self.drawing_line = self.draw_first_line(event)
        else:
            self.line.append(self.draw_first_line(event))
            self.second_line = True

    def button_move(self, event):
        if not self.second_line:
            self.canvas.delete(self.drawing_line)
            # 傾きを出して視点と終端を決める
            self.slope = (event.y - self.start_y.get()) / \
                (event.x - self.start_x.get())
            self.drawing_line = self.draw_first_line(event)
        else:
            self.canvas.delete(self.drawing_line)
            self.drawing_line = self.draw_second_line(event)

    def get_distance(self, x1, y1, x2, y2):
        d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 1)
        return d

    def draw_first_line(self, event):
        return self.draw_line(self.start_x.get() - self.times,
                              self.start_y.get() - self.slope * self.times, event.x + self.times, event.y + self.slope * self.times, "black")

    def draw_second_line(self, event):
        return self.draw_line(event.x - self.times,
                              event.y - self.slope * self.times, event.x + self.times, event.y + self.slope * self.times, "black")

    def draw_line(self, x1, y1, x2, y2, color):
        return self.canvas.create_line(
            x1, y1, x2, y2, fill=color)
