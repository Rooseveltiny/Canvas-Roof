from canvas_resizer import CanvasResizer
from canvas_covered_slopes import CoveredFlatSlope
from canvas_objects import CorrugatedSheetParams
from canvas_serializer import CanvasSlopeDataSerializer
from canvas_core import CanvasPointer, CanvasPoint, CanvasIsoscelesTrapezoid
import unittest
import json
import sys
sys.path.insert(1, '../')


class TestCanvasPointAndPointer(unittest.TestCase):

    def test_canvas_point(self):

        canvas_point = CanvasPoint(15, 100)
        self.assertEqual(canvas_point.coordinates, [15, 100])
        points = [999, 999]
        canvas_point = CanvasPoint(*points)
        self.assertEqual(canvas_point.coordinates, points)

    def test_canvas_pointer(self):

        canvas_point = CanvasPoint(15, 15)
        canvas_pointer = CanvasPointer(canvas_point)
        self.assertEqual(type(canvas_pointer.take_point()), CanvasPoint)
        canvas_pointer.move_right(100)
        canvas_pointer.move_down(750)
        current_position = canvas_pointer.take_point()
        self.assertEqual(current_position.x, 115)
        self.assertEqual(current_position.y, -735)

    def test_canvas_trapezoid(self):

        trapezoid = CanvasIsoscelesTrapezoid(
            CanvasPoint(15, 15), 3000, 9000, 2750)
        self.assertEqual(trapezoid.side_difference, 3000)
        trapezoid.draw()
        self.assertEqual(len(trapezoid.canvas_points), 5)
        self.assertEqual(type(trapezoid.canvas_points[0]), CanvasPoint)


class TestCoveredSlopes(unittest.TestCase):

    def setUp(self):

        self.curragated_params = CorrugatedSheetParams(1205, 1150)
        self.covered_slope = CoveredFlatSlope(CanvasPoint(
            15, 15), self.curragated_params, slope_width=6000, slope_height=2990)

    def test_covered_flat_slope(self):

        qnt = self.covered_slope.sheets_quantity
        height = self.covered_slope.slope_height
        width = self.covered_slope.slope_width
        all_objects_len = len(self.covered_slope.all_objects)
        self.assertEqual(qnt, 6)
        self.assertEqual(height, 2990)
        self.assertEqual(width, 6000)
        self.assertEqual(all_objects_len, 6)

    def test_canvas_resizer(self):

        first_point_was = self.covered_slope.all_objects[0].all_coordinates[0][0][0]
        self.assertEqual(first_point_was, 15)
        CanvasResizer(self.covered_slope, 6000, 2990, 800, 600)
        first_point_became = int(self.covered_slope.all_objects[0].all_coordinates[0][0])
        self.assertEqual(first_point_became, 798)

    def test_serializer(self):

        self.test_canvas_resizer()
        prepeared_sheets_data = CanvasSlopeDataSerializer(self.covered_slope).data
        prepeared_slope_data = CanvasSlopeDataSerializer(self.covered_slope.slope).data
        deserialized_sheets_data = json.loads(prepeared_sheets_data)
        deserialized_slope_data = json.loads(prepeared_slope_data)
        self.assertTrue("all_objects" in deserialized_sheets_data)
        self.assertTrue("all_objects" in deserialized_slope_data)