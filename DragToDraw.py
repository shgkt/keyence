class DragToDraw:
    def __init__(self):
        self

    def button_move(self, event):
        # 座標の文字列
        self.stop_x_str.set('x : ' + str(event.x))
        self.stop_y_str.set('y : ' + str(event.y))
        # 距離の文字列
        self.distance_str.set(str(self.get_distance(
            event.x, event.y, self.start_x.get(), self.start_y.get())))
        self.canvas.delete(self.drawing_line)
        self.draw_line(self.start_x.get(),
                       self.start_y.get(), event.x, event.y, "black")

    def get_distance(self, x1, y1, x2, y2):
        d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 1)
        return d

    def draw_line(self, x1, y1, x2, y2, color):
        self.drawing_line = self.canvas.create_line(x1, y1, x2, y2, fill=color)
