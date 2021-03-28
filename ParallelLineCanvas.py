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
        self.end = False
        self.second_line = False
        self.line = []
        # 直線を伸ばすための値
        self.times = 1000

    def mouse_click(self, event):
        # 2本目モード
        if self.second_line:
            self.end = True
            self.second_line = False
            self.line.append(self.draw_second_line(event))
            self.canvas.unbind('<Motion>', self.motion_bind_id)
            return event.x, event.y

        # 1本目モード
        self.start_x = event.x
        self.start_y = event.y
        self.line.append(self.draw_first_line(event))
        self.drawing_line = self.draw_first_line(event)
        self.drawing_horizontal_line = self.draw_horizontal_line(event)
        self.enter_bind_id = self.canvas.bind(
            '<Motion>', self.mouse_move)
        self.second_line = True
        return self.start_x, self.start_y

    def mouse_move(self, event):
        # 1本目
        if not self.second_line:
            self.canvas.delete(self.drawing_line)
            self.drawing_line = self.draw_first_line(event)
        # 2本目
        else:
            self.canvas.delete(self.drawing_line)
            self.drawing_line = self.draw_second_line(event)
            self.canvas.delete(self.drawing_horizontal_line)
            self.drawing_horizontal_line = self.draw_horizontal_line(event)

    def get_distance(self, event):
        d = abs(event.y - self.start_y)
        return d

    def draw_first_line(self, event):
        return self.draw_line(event.x,
                              event.y - self.times, event.x, event.y + self.times, "black")

    def draw_second_line(self, event):
        return self.draw_line(event.x,
                              event.y - self.times, event.x, event.y + self.times, "black")

    def draw_horizontal_line(self, event):
        return self.draw_line(event.x,
                              event.y, self.start_x, event.y, "black")

    def calc_slope(self, event):
        return 0

    def draw_line(self, x1, y1, x2, y2, color):
        return self.canvas.create_line(
            x1, y1, x2, y2, fill=color)
