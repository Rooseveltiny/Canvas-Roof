import numpy as np
from abc import ABCMeta, abstractmethod

x = [0, 6000, 12000, 18000]
y = [0, 3000, 3000, 0]
print(np.interp(1150, x, y))


class CountHeightSlopeBase:

    def __init__(self, slope, curragated_sheet_param, count_of_sheets):
        self.slope = slope
        self.curragated_sheet = curragated_sheet_param
        self.count_of_sheets = count_of_sheets
        self.x_dots = []
        self.y_dots = []
        self.heights = []
        self.count()

    def count(self):
        self._get_coordinates_of_slope()
        self._perform_count()

    def _perform_count(self):

        current_width_right = self.curragated_sheet.work_width
        current_width_left = 0

        transition = True
        for i in range(0, self.count_of_sheets):
            right_height = np.interp(
                current_width_right, self.x_dots, self.y_dots)
            left_height = np.interp(
                current_width_left, self.x_dots, self.y_dots)
            if right_height > left_height:
                self.heights.append(right_height)
            elif right_height <= left_height:
                if transition:
                    self.heights.append(max(self.y_dots))
                    transition = False
                else:
                    self.heights.append(left_height)
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
