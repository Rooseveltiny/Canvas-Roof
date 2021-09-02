from abc import ABCMeta, abstractmethod


class CanvasPoint:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_point_upper(self, value):
        self.y += value

    def get_point_down(self, value):
        self.y -= value

    def get_point_left(self, value):
        self.x -= value

    def get_point_right(self, value):
        self.x += value

    @property
    def coordinates(self):
        return [self.x, self.y]


class BaseCanvas:

    def __init__(self, start_point):
        self.canvas_points = []
        self.start_point = start_point
        self.set_point(start_point)

    def set_point(self, point):
        self.canvas_points.append(point)


class CanvasPointer(BaseCanvas):

    def __init__(self, start_point):
        super().__init__(start_point)
        self.current_point = start_point

    def move_up(self, value):
        self.current_point.get_point_upper(value)

    def move_down(self, value):
        self.current_point.get_point_down(value)

    def move_left(self, value):
        self.current_point.get_point_left(value)

    def move_right(self, value):
        self.current_point.get_point_right(value)

    def take_point(self):
        return CanvasPoint(self.current_point.x, self.current_point.y)


class CanvasBaseFigure(BaseCanvas):
    __metaclass__ = ABCMeta

    def __init__(self, start_point):
        self.canvas_pointer = CanvasPointer(start_point)

    def save_point(self):
        self.set_point(self.canvas_pointer.take_point())

    def close_figure(self):
        self.set_point(self.start_point)


    @abstractmethod
    def draw(self):
        pass


class CanvasRectangle(CanvasBaseFigure):

    def __init__(self, start_point, height, width):
        BaseCanvas.__init__(self, CanvasPoint(start_point.x, start_point.y))
        CanvasBaseFigure.__init__(
            self, CanvasPoint(start_point.x, start_point.y))
        self.height = height
        self.width = width

    def draw(self):

        self.canvas_pointer.move_right(self.width)
        self.save_point()
        self.canvas_pointer.move_up(self.height)
        self.save_point()
        self.canvas_pointer.move_left(self.width)
        self.save_point()
        self.canvas_pointer.move_down(self.height)
        self.close_figure()


class CanvasTriangle(CanvasBaseFigure):

    def __init__(self, start_point, side_a, side_b, height):
        BaseCanvas.__init__(self, CanvasPoint(start_point.x, start_point.y))
        CanvasBaseFigure.__init__(
            self, CanvasPoint(start_point.x, start_point.y))
        self.side_a = side_a
        self.side_b = side_b
        self.height = height

    def draw(self):
        self.canvas_pointer.move_right(self.side_a+self.side_b)
        self.save_point()
        self.canvas_pointer.move_left(self.side_b)
        self.canvas_pointer.move_up(self.height)
        self.save_point()
        self.close_figure()


class CanvasStraightTriangle(CanvasBaseFigure):

    def __init__(self, start_point, side_x, side_y):
        BaseCanvas.__init__(self, CanvasPoint(start_point.x, start_point.y))
        CanvasBaseFigure.__init__(
            self, CanvasPoint(start_point.x, start_point.y))
        self.side_x = side_x
        self.side_y = side_y

    def draw(self):
        self.canvas_pointer.move_right(self.side_x)
        self.save_point()
        self.canvas_pointer.move_left(self.side_x)
        self.canvas_pointer.move_up(self.side_y)
        self.save_point()
        self.close_figure()


class CanvasIsoscelesTrapezoid(CanvasBaseFigure):

    def __init__(self, start_point, up_side, down_side, height):
        BaseCanvas.__init__(self, CanvasPoint(start_point.x, start_point.y))
        CanvasBaseFigure.__init__(
            self, CanvasPoint(start_point.x, start_point.y))
        self.up_side = up_side
        self.down_side = down_side
        self.height = height
        self.side_difference = self._get_side_difference()

    def _get_side_difference(self):
        return abs((self.up_side-self.down_side)/2)

    def draw(self):

        self.canvas_pointer.move_right(self.down_side)
        self.save_point()
        self.canvas_pointer.move_left(self.side_difference)
        self.canvas_pointer.move_up(self.height)
        self.save_point()
        self.canvas_pointer.move_left(self.up_side)
        self.save_point()
        self.close_figure()


class CanvasTextBlock:

    def __init__(self, text, canvas_point):

        self.text = text
        self.canvas_point = canvas_point


if __name__ == "__main__":

    new_rect = CanvasRectangle(CanvasPoint(15, 15), 50, 100)
    new_rect.draw()

    new_triangle = CanvasStraightTriangle(CanvasPoint(15, 15), 100, 50)
    new_triangle.draw()

    isosceles_trapez = CanvasIsoscelesTrapezoid(
        CanvasPoint(15, 15), 100, 200, 50)
    isosceles_trapez.draw()
    
    triangle = CanvasTriangle(CanvasPoint(15,15), 15, 100, 150)
    triangle.draw()