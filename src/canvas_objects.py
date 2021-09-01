from abc import ABCMeta, abstractmethod
from canvas_core import CanvasRectangle, CanvasPoint, CanvasIsoscelesTrapezoid, CanvasTriangle


class CanvasBaseObject:

    def __init__(self, start_point, *args, **kwargs):
        self.start_point = start_point
        self.coordinates = []
        self.figures = []
        self.perform_object__init(*args, **kwargs)
        self._build()

    def set_figure(self, figure):
        self.figures.append(figure)

    @property
    def all_coordinates(self):
        all_coordinates = []
        for figure in self.figures:
            all_coordinates.append(
                [point.coordinates for point in figure.canvas_points])
        return all_coordinates

    @abstractmethod
    def perform_object__init(self, *args, **kwargs):
        pass

    @abstractmethod
    def _build(self):
        pass


class CorrugatedSheetParams:

    def __init__(self, width, work_width):
        self.work_width = work_width
        self.width = width


class CorrugatedSheet(CanvasBaseObject):

    def perform_object__init(self, height, *args, **kwargs):
        self.height = height
        self.corrugated_params = kwargs['corrugated_params']

    def _build(self):
        rect = CanvasRectangle(
            self.start_point, self.height, self.corrugated_params.width)
        rect.draw()
        self.set_figure(rect)


class FlatSlope(CanvasBaseObject):

    def perform_object__init(self, *args, **kwargs):
        self.width = kwargs['width']
        self.height = kwargs['height']

    def _build(self):
        rect = CanvasRectangle(self.start_point, self.height, self.width)
        rect.draw()
        self.set_figure(rect)


class EvenTrapeziaSlope(CanvasBaseObject):

    def perform_object__init(self, *args, **kwargs):
        self.up_side = kwargs['up_side']
        self.down_side = kwargs['down_side']
        self.height = kwargs['height']

    def _build(self):
        trapez = CanvasIsoscelesTrapezoid(
            self.start_point, self.up_side, self.down_side, self.height)
        trapez.draw()
        self.set_figure(trapez)


class TriangleSlope(CanvasBaseObject):

    def perform_object__init(self, *args, **kwargs):
        self.height = kwargs['height']
        self.width = kwargs['width']

    def _build(self):
        triangle = CanvasTriangle(
            self.start_point, self.width/2, self.width/2, self.height)
        triangle.draw()
        self.set_figure(triangle)


if __name__ == "__main__":

    sheet_params = CorrugatedSheetParams(1205, 4000, 1150)
    sheet = CorrugatedSheet(CanvasPoint(
        15, 15), corrugated_params=sheet_params)
    print(sheet.all_coordinates)
    flat_slope = FlatSlope(CanvasPoint(15, 15), width=4000, height=3000)
    print(flat_slope.all_coordinates)
    trapez_slope = EvenTrapeziaSlope(CanvasPoint(
        15, 15), up_side=3000, down_side=6000, height=2500)
    print(trapez_slope.all_coordinates)
    triangle_slope = TriangleSlope(
        CanvasPoint(15, 15), height=3000, down_side=1500)
    print(triangle_slope.all_coordinates)
