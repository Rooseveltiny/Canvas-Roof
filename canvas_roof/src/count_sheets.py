import numpy as np
from abc import ABCMeta, abstractmethod

from canvas_roof.src.canvas_core import CanvasPoint


class SlopeContourPoints:

    def __init__(self, x_dots, y_dots):

        self.x_dots = x_dots
        self.y_dots = y_dots
        self.countur_points_x = []
        self.countur_points_y = []
        self._build_countur()

    def _build_countur(self):

        first_x = min(self.x_dots)
        last_x = max(self.x_dots)
        x = first_x
        while x <= last_x:
            y = np.interp(
                x, self.x_dots, self.y_dots)
            self.countur_points_x.append(x)
            self.countur_points_y.append(y)
            x += 10

    def get_highest_point(self, start_x, end_x):

        start_x = int(round(start_x, -1))
        end_x = int(round(end_x, -1))

        if start_x in self.countur_points_x:
            first_index = self.countur_points_x.index(start_x)
        else:
            first_index = 0

        if end_x in self.countur_points_x:
            last_index = self.countur_points_x.index(end_x)
        else:
            last_index = len(self.countur_points_x) - 1

        array_of_points = self.countur_points_y[first_index: last_index+1]
        return max(array_of_points)


class CountHeightSlopeBase:

    def __init__(self, slope, curragated_sheet_param, count_of_sheets, sheets_start_point: CanvasPoint):
        self.slope = slope
        self.sheets_start_point = sheets_start_point
        self.curragated_sheet = curragated_sheet_param
        self.count_of_sheets = count_of_sheets
        self.x_dots = []
        self.y_dots = []
        self.heights = []
        self.count()

    def count(self):
        self._get_coordinates_of_slope()
        self._perform_count()

    def add_new_height(self, height):
        should_add = self.slope.start_point.y - self.sheets_start_point.y
        self.heights.append(int(round((height+should_add)/5.0)*5))

    def _perform_count(self):

        current_width_right = self.curragated_sheet.work_width
        current_width_left = 0
        sloup_countur = SlopeContourPoints(self.x_dots, self.y_dots)

        for _ in range(0, self.count_of_sheets):
            height = sloup_countur.get_highest_point(
                current_width_left, current_width_right)
            self.add_new_height(height)
            current_width_right += self.curragated_sheet.work_width
            current_width_left += self.curragated_sheet.work_width

    @abstractmethod
    def _get_coordinates_of_slope(self):
        pass


class CountRectangleSlope(CountHeightSlopeBase):

    def _get_coordinates_of_slope(self):
        self.x_dots = []
        self.y_dots = []

        self.y_dots.append(0)
        self.y_dots.append(self.slope.height)
        self.y_dots.append(self.slope.height)
        self.y_dots.append(0)

        self.x_dots.append(0)
        self.x_dots.append(0)
        self.x_dots.append(self.slope.width)
        self.x_dots.append(self.slope.width)


class CountTrapezSlope(CountHeightSlopeBase):

    def _get_coordinates_of_slope(self):
        self.x_dots = []
        self.y_dots = []

        self.y_dots.append(0)
        self.y_dots.append(self.slope.height)
        self.y_dots.append(self.slope.height)
        self.y_dots.append(0)

        difference = abs((self.slope.down_side - self.slope.up_side)/2)
        first = difference
        second = difference + self.slope.up_side
        third = second + difference

        self.x_dots.append(0)
        self.x_dots.append(first)
        self.x_dots.append(second)
        self.x_dots.append(third)


class CountIsoscelesTriangleSlope(CountHeightSlopeBase):

    def _get_coordinates_of_slope(self):
        self.x_dots = []
        self.y_dots = []

        self.y_dots.append(0)
        self.y_dots.append(self.slope.height)
        self.y_dots.append(0)

        one_part = self.slope.width / 2

        self.x_dots.append(0)
        self.x_dots.append(one_part)
        self.x_dots.append(self.slope.width)
