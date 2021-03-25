import math
import tkinter


class ParallelLineCanvas:
    def __init__(self, canvas):
        self.canvas = canvas
        self.start_x = 0
        self.start_y = 0
        self.stop_x = 0
        self.stop_y = 0
        self.distance = 0
        self.motion_bind_id = 0
        self.end = True
        self.second_line = False
        self.line = []
        # 直線の式保持用 ax + by + c
        self.a = 0
        self.b = -1
        self.c = 0
        # 直線を伸ばすための値
        self.times = 1000
        self.slope = 0

    def mouse_click(self, event):
        # 2本目モード
        if self.second_line:
            self.end = True
            self.second_line = False
            self.line.append(self.draw_second_line(event))
            self.canvas.unbind('<Motion>', self.motion_bind_id)
            return self.start_x, self.start_y

        # 1本目モード
        self.end = not self.end
        if self.end is not True:
            self.start_x = event.x
            self.start_y = event.y
            self.motion_bind_id = self.canvas.bind(
                '<Motion>', self.mouse_move)
            self.drawing_line = self.draw_first_line(event)
        else:
            self.line.append(self.draw_first_line(event))
            self.second_line = True
            self.calc_lenear_func()
            self.drawing_vertical_line = self.draw_vertical_line(event)

        return self.start_x, self.start_y

    def mouse_move(self, event):
        # 1本目
        if not self.second_line:
            self.canvas.delete(self.drawing_line)
            # 傾きを出して視点と終端を決める
            self.slope = self.calc_slope(event)
            self.drawing_line = self.draw_first_line(event)
        # 2本目
        else:
            self.canvas.delete(self.drawing_line)
            self.drawing_line = self.draw_second_line(event)
            self.canvas.delete(self.drawing_vertical_line)
            self.drawing_vertical_line = self.draw_vertical_line(event)

    def get_distance(self, event):
        numerator = abs(self.a * event.x + self.b * event.y + self.c)
        denominator = math.sqrt(self.a**2 + self.b**2)
        d = numerator / denominator
        return d

    def draw_first_line(self, event):
        return self.draw_line(self.start_x - self.times,
                              self.start_y - self.slope * self.times, event.x + self.times, event.y + self.slope * self.times, "black")

    def draw_second_line(self, event):
        return self.draw_line(event.x - self.times,
                              event.y - self.slope * self.times, event.x + self.times, event.y + self.slope * self.times, "black")

    def draw_vertical_line(self, event):
        d = self.get_distance(event)
        vs = - 1 / self.slope  # vertical slope
        dx = d / math.sqrt(vs**2 + 1)
        dy = d * vs / math.sqrt(vs**2 + 1)
        print(dx)
        print(dy)
        return self.draw_line(event.x,
                              event.y, event.x - dx, event.y - dy, "black")

    def calc_slope(self, event):
        if event.x - self.start_x == 0:
            return 0

        return (event.y - self.start_y) / (event.x - self.start_x)

    def draw_line(self, x1, y1, x2, y2, color):
        return self.canvas.create_line(
            x1, y1, x2, y2, fill=color)

    def calc_lenear_func(self):
        self.c = - self.slope * self.start_x + self.start_y
        self.a = self.slope
