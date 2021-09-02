from abc import ABCMeta, abstractmethod
from canvas_core import CanvasRectangle, CanvasPoint, CanvasIsoscelesTrapezoid, CanvasTriangle
from custom_errors import ItIsNotCoordinate
from statistics import mean
from canvas_core import CanvasTextBlock

class CanvasBaseObject:

    strokeColor = "#000000"
    lineWidth = 1

    def __init__(self, start_point, *args, **kwargs):
        self.start_point = start_point
        self.coordinates = []
        self.figures = []
        self.text_blocks = []
        self.perform_object__init(*args, **kwargs)
        self._build()
        self._set_all_coordinates()
        self._add_text_blocks()

    def set_figure(self, figure):
        self.figures.append(figure)

    def _set_all_coordinates(self):
        all_coordinates = []
        for figure in self.figures:
            all_coordinates.append(
                [point.coordinates for point in figure.canvas_points])
        self.all_coordinates = all_coordinates

    @abstractmethod
    def perform_object__init(self, *args, **kwargs):
        pass

    @abstractmethod
    def _build(self):
        pass

    @abstractmethod
    def _add_text_blocks(self):
        pass


    @staticmethod
    def find_center_of_coordinates(*args):

        all_x = []
        all_y = []
        for coordinate in args:
            if not type(coordinate) == list:
                raise ItIsNotCoordinate
            x, y = coordinate
            all_x.append(x); all_y.append(y)
        return [mean(all_x), mean(all_y)]


class CanvasStyleSlope:

    strokeColor = "rgba(255, 0, 0, 0.5)"
    lineWidth = 2


class CorrugatedSheetParams:

    def __init__(self, width, work_width):
        self.work_width = work_width
        self.width = width


class CorrugatedSheet(CanvasBaseObject):

    strokeColor = "green"
    lineWidth = 2

    def perform_object__init(self, height, *args, **kwargs):
        self.height = height
        self.corrugated_params = kwargs['corrugated_params']

    def _build(self):
        rect = CanvasRectangle(
            self.start_point, self.height, self.corrugated_params.width)
        rect.draw()
        self.set_figure(rect)

    def _add_text_blocks(self):

        text_placement = CanvasBaseObject.find_center_of_coordinates(*self.all_coordinates[0][0:4])
        text_object = CanvasTextBlock(str(self.height), CanvasPoint(*text_placement))
        self.text_blocks.append(text_object)


class FlatSlope(CanvasStyleSlope, CanvasBaseObject):

    def perform_object__init(self, *args, **kwargs):
        self.width = kwargs['width']
        self.height = kwargs['height']

    def _build(self):
        rect = CanvasRectangle(self.start_point, self.height, self.width)
        rect.draw()
        self.set_figure(rect)


class EvenTrapeziaSlope(CanvasStyleSlope, CanvasBaseObject):

    def perform_object__init(self, *args, **kwargs):
        self.up_side = kwargs['up_side']
        self.down_side = kwargs['down_side']
        self.height = kwargs['height']

    def _build(self):
        trapez = CanvasIsoscelesTrapezoid(
            self.start_point, self.up_side, self.down_side, self.height)
        trapez.draw()
        self.set_figure(trapez)


class TriangleSlope(CanvasStyleSlope, CanvasBaseObject):

    def perform_object__init(self, *args, **kwargs):
        self.height = kwargs['height']
        self.width = kwargs['width']

    def _build(self):
        triangle = CanvasTriangle(
            self.start_point, self.width/2, self.width/2, self.height)
        triangle.draw()
        self.set_figure(triangle)


if __name__ == "__main__":

    sheet_params = CorrugatedSheetParams(1205, 1150)
    sheet = CorrugatedSheet(CanvasPoint(
        15, 15), 3000, corrugated_params=sheet_params)
    print(sheet.all_coordinates)
    flat_slope = FlatSlope(CanvasPoint(15, 15), width=4000, height=3000)
    print(flat_slope.all_coordinates)
    trapez_slope = EvenTrapeziaSlope(CanvasPoint(
        15, 15), up_side=3000, down_side=6000, height=2500)
    print(trapez_slope.all_coordinates)
    triangle_slope = TriangleSlope(
        CanvasPoint(15, 15), height=3000, width=1500)
    print(triangle_slope.all_coordinates)


    print(CanvasBaseObject.find_center_of_coordinates([15,15], [15,100]))