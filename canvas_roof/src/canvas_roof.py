from canvas_roof.src.canvas_covered_slopes import (
    CoveredFlatSlope,
    CoveredTrapezSlope,
    CoveredIsoscelesTriangleSlope,
    CanvasPoint,
    CorrugatedSheetParams,
    CanvasResizer,
)

from canvas_roof.src.canvas_resizer import CanvasResizer
from canvas_roof.src.canvas_serializer import CanvasSlopeDataSerializer


def to_mm(input):
    return input*1000


def prepare_data(sheets, max_x, max_y, can_x, can_y):

    CanvasResizer(sheets, max_x, max_y, can_x, can_y)
    sheets_data = CanvasSlopeDataSerializer(sheets)
    slope_data = CanvasSlopeDataSerializer(sheets.slope)
    return dict(slope=slope_data.output_data, sheets=sheets_data.output_data)


def count_flat_slope(sheet_params: CorrugatedSheetParams, canvas_size: dict, size_width: int, size_height: int) -> dict:

    size_width = to_mm(size_width)
    size_height = to_mm(size_height)
    covered_slope = CoveredFlatSlope(CanvasPoint(
        15, 15), sheet_params, slope_width=size_width, slope_height=size_height)
    return prepare_data(covered_slope, size_width, size_height, canvas_size['x'], canvas_size['y'])


def count_trapez_slope(sheet_params: CorrugatedSheetParams, canvas_size: dict, size_bottom_width: int, size_top_width: int, size_height: int) -> dict:

    size_bottom_width = to_mm(size_bottom_width)
    size_top_width = to_mm(size_top_width)
    size_height = to_mm(size_height)
    covered_slope = CoveredTrapezSlope(CanvasPoint(
        15, 15), sheet_params, up_side=size_top_width, down_side=size_bottom_width, slope_height=size_height)
    return prepare_data(covered_slope, size_bottom_width, size_height, canvas_size['x'], canvas_size['y'])


def count_isosceles_triangle_slope(sheet_params: CorrugatedSheetParams, canvas_size: dict, size_width: int, size_height: int) -> dict:

    size_width = to_mm(size_width)
    size_height = to_mm(size_height)
    covered_slope = CoveredIsoscelesTriangleSlope(CanvasPoint(
        15, 15), sheet_params, height=size_height, width=size_width)
    return prepare_data(covered_slope, size_width, size_height, canvas_size['x'], canvas_size['y'])


if __name__=="__main__":

    result = count_flat_slope(CorrugatedSheetParams(1200, 1150), dict(x=1500, y=600), 6, 3)
    print(result)