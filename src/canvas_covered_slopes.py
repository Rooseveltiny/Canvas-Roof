from abc import ABCMeta, abstractmethod
from canvas_core import CanvasPoint, CanvasPointer
from math import ceil
from count_sheets import (
    CountTrapezSlope,
    CountRectangleSlope,
    CountIsoscelesTriangleSlope
)

from custom_errors import (
    UpSideIsGreaterThanDownSide,
    UpSideShouldBeMoreThan600mm
)

from canvas_objects import (
    FlatSlope,
    TriangleSlope,
    CorrugatedSheet,
    EvenTrapeziaSlope,
    CorrugatedSheetParams,
)


class CanvasCoveredBase:
    __metaclass__ = ABCMeta

    def __init__(self, start_point, corrugated_params, *args, **kwargs):
        self.corrugated_params = corrugated_params
        self.start_point = start_point
        self.sheets_quantity = 0
        self.sheets_heights = []
        self.all_sheets = []
        self.slope = None
        self.perform_init(*args, **kwargs)
        self.build_slope()
        self.count_quantity()
        self.collect_heights()
        self.cover_with_sheets()

    def cover_sheet(self, start_point, height):
        self.all_sheets.append(CorrugatedSheet(
            start_point, height, corrugated_params=self.corrugated_params))

    @abstractmethod
    def perform_init(self, *args, **kwargs):
        '''
        set input params
        '''
        pass

    @abstractmethod
    def collect_heights(self, *args, **kwargs):
        '''
        collect all heights of sheets according order
        '''
        pass

    @abstractmethod
    def count_quantity(self, *args, **kwargs):
        '''
        getting quantity of needed sheets to cover
        '''
        pass

    @abstractmethod
    def build_slope(self, *args, **kwargs):
        '''
        making slope for canvas
        '''
        pass

    def cover_with_sheets(self):
        '''
        creating sheets one by one
        '''
        pointer = CanvasPointer(self.start_point)
        for sheet_height in self.sheets_heights:
            self.cover_sheet(pointer.take_point(), sheet_height)
            pointer.move_right(self.corrugated_params.work_width)


class CoveredFlatSlope(CanvasCoveredBase):

    def perform_init(self, *args, **kwargs):
        self.slope_width = kwargs['slope_width']
        self.slope_height = kwargs['slope_height']

    def build_slope(self):
        self.slope = FlatSlope(
            self.start_point, width=self.slope_width, height=self.slope_height)

    def count_quantity(self, *args, **kwargs):
        self.sheets_quantity = ceil(
            self.slope_width / self.corrugated_params.work_width)

    def collect_heights(self, *args, **kwargs):
        self.sheets_heights = CountRectangleSlope(
            self.slope, self.corrugated_params, self.sheets_quantity).heights


class CoveredTrapezSlope(CanvasCoveredBase):

    def perform_init(self, *args, **kwargs):
        self.up_side = kwargs['up_side']
        self.down_side = kwargs['down_side']
        self.slope_height = kwargs['slope_height']

    def build_slope(self):
        self.slope = EvenTrapeziaSlope(
            self.start_point, up_side=self.up_side, down_side=self.down_side, height=self.slope_height)

    def count_quantity(self, *args, **kwargs):
        self.sheets_quantity = ceil(
            self.down_side / self.corrugated_params.work_width)

    def collect_heights(self, *args, **kwargs):
        self.sheets_heights = CountTrapezSlope(
            self.slope, self.corrugated_params, self.sheets_quantity).heights


class CoveredIsoscelesTriangleSlope(CanvasCoveredBase):

    def perform_init(self, *args, **kwargs):
        self.height = kwargs['height']
        self.width = kwargs['width']

    def build_slope(self):
        self.slope = TriangleSlope(
            self.start_point, height=self.height, width=self.width)

    def count_quantity(self, *args, **kwargs):
        self.sheets_quantity = ceil(
            self.width / self.corrugated_params.work_width)

    def collect_heights(self, *args, **kwargs):
        self.sheets_heights = CountIsoscelesTriangleSlope(
            self.slope, self.corrugated_params, self.sheets_quantity).heights


if __name__ == "__main__":

    curragated_params = CorrugatedSheetParams(1205, 1150)
    covered_slope = CoveredFlatSlope(CanvasPoint(
        15, 15), curragated_params, slope_width=6000, slope_height=3000)

    curragated_params = CorrugatedSheetParams(1205, 1150)
    covered_trapez = CoveredTrapezSlope(CanvasPoint(
        15, 15), curragated_params, up_side=0, down_side=8000, slope_height=6000)

    curragated_params = CorrugatedSheetParams(1205, 1150)
    isosceles_triangle = CoveredIsoscelesTriangleSlope(
        CanvasPoint(15, 15), curragated_params, height=5000, width=10000)
