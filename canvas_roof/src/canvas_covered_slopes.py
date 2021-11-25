from canvas_roof.src.canvas_objects import (
    FlatSlope,
    TriangleSlope,
    CanvasTextBlock,
    CorrugatedSheet,
    EvenTrapeziaSlope,
    CorrugatedSheetParams,
)
from canvas_roof.src.custom_errors import (
    UpSideIsGreaterThanDownSide,
    UpSideShouldBeMoreThan600mm
)
from canvas_roof.src.count_sheets import (
    CountTrapezSlope,
    CountRectangleSlope,
    CountIsoscelesTriangleSlope
)
from canvas_roof.src.canvas_resizer import CanvasResizer
from canvas_roof.src.canvas_serializer import CanvasSlopeDataSerializer
from math import ceil
from canvas_roof.src.canvas_core import CanvasPoint, CanvasPointer
from abc import ABCMeta, abstractmethod



class CanvasCoveredBase:
    __metaclass__ = ABCMeta

    def __init__(self, start_point: CanvasPoint, corrugated_params: CorrugatedSheetParams, sheets_start_point: CanvasPoint = None, minimal_height: int = 0, *args, **kwargs):
        self.corrugated_params = corrugated_params
        self.start_point = start_point
        self.sheets_start_point = sheets_start_point if sheets_start_point else start_point
        self.minimal_height = minimal_height
        self.sheets_quantity = 0
        self.sheets_heights = []
        self.all_objects = []
        self.slope = None
        self.perform_init(*args, **kwargs)
        self.build_slope()
        self.count_quantity()
        self.collect_heights()
        self.cover_with_sheets()

    def cover_sheet(self, start_point, height):
        # here we make not possible to add too small heights
        if (height >= self.minimal_height):  # <----
            find_text_pt = CanvasTextBlock.get_text_font(
                self.sheets_quantity * self.corrugated_params.work_width)
            self.all_objects.append(CorrugatedSheet(
                start_point, height, find_text_pt, corrugated_params=self.corrugated_params))

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
        pointer = CanvasPointer(self.sheets_start_point)
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
            self.slope, self.corrugated_params, self.sheets_quantity, self.sheets_start_point).heights


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
            self.slope, self.corrugated_params, self.sheets_quantity, self.sheets_start_point).heights


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
            self.slope, self.corrugated_params, self.sheets_quantity, self.sheets_start_point).heights


def _get_test_data(sheets, max_x, max_y, can_x, can_y):

    CanvasResizer(sheets, max_x, max_y, can_x, can_y)
    prepeared_data = CanvasSlopeDataSerializer(sheets)
    prepeared_slope_data = CanvasSlopeDataSerializer(sheets.slope)
    print(prepeared_data.data)
    print('----- ----- ----- ----- ------ ------')
    print(prepeared_slope_data.data)


if __name__ == "__main__":

    curragated_params = CorrugatedSheetParams(1205, 1150)
    covered_slope = CoveredFlatSlope(CanvasPoint(
        150, 150), curragated_params, CanvasPoint(150,100),slope_width=6000, slope_height=2990)

    curragated_params = CorrugatedSheetParams(1205, 1150)
    covered_trapez = CoveredTrapezSlope(CanvasPoint(
        150, 150), curragated_params, CanvasPoint(150,100), up_side=22150, down_side=25000, slope_height=5400)

    curragated_params = CorrugatedSheetParams(1205, 1150)
    isosceles_triangle = CoveredIsoscelesTriangleSlope(
        CanvasPoint(150, 150), curragated_params, CanvasPoint(150,100), height=6000, width=6000)

    _get_test_data(covered_trapez, 25000, 5400, 1500, 600)
