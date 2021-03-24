import math
import tkinter


class DragToDrawCanvas:
    def __init__(self, canvas):
        self.canvas = canvas
        self.start_x = 0
        self.start_y = 0
        self.stop_x = 0
        self.stop_y = 0
        self.distance = 0
        self.end = tkinter.BooleanVar()
        self.motion_bind_id = 0

    def mouse_click(self, event):
        self.end = not self.end
        if self.end is not True:
            self.start_x = event.x
            self.start_y = event.y
            self.motion_bind_id = self.canvas.bind(
                '<Motion>', self.mouse_move)
            self.draw_line(self.start_x,
                           self.start_y, event.x, event.y, "black")
        else:
            self.canvas.unbind('<Motion>', self.motion_bind_id)
        return self.start_x, self.start_y

    def mouse_move(self, event):
        self.distance = self.get_distance(
            event.x, event.y, self.start_x, self.start_y)
        self.canvas.delete(self.drawing_line)
        self.draw_line(self.start_x,
                       self.start_y, event.x, event.y, "black")

    def get_distance(self, x1, y1, x2, y2):
        d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 1)
        return d

    def draw_line(self, x1, y1, x2, y2, color):
        self.drawing_line = self.canvas.create_line(x1, y1, x2, y2, fill=color)
