'''
module for adjusting resolution of canvas objects them to be proper input at canvas
'''

class CanvasResizer:

    def __init__(self, canvas_object, max_x, max_y, canvas_x, canvas_y):

        self.canvas_object = canvas_object
        self.max_x = max_x
        self.max_y = max_y
        self.canvas_x, self.canvas_y = canvas_x, canvas_y
        self.set_relation(max_x, max_y, canvas_x, canvas_y)
        self.resize_object(canvas_object)
        self.resize_object(canvas_object.slope)

    def set_relation(self, max_x, max_y, canvas_x, canvas_y):

        x_relation = max_x / canvas_x
        y_relation = max_y / canvas_y
        relation = x_relation if x_relation >= y_relation else y_relation
        self.relation = relation * 1.05
        self.resized_x = canvas_x * self.relation
        self.resized_y = canvas_y * self.relation

    def bend_x(self, x):
        pass

    def bend_y(self, y):
        pass

    def resize_object(self, input_object):

        if hasattr(input_object, "all_coordinates"):
            input_object.all_coordinates = self.resize_coordinates(
                input_object.all_coordinates)

        if hasattr(input_object, "all_objects"):
            for obj in input_object.all_objects:
                self.resize_object(obj)

        if hasattr(input_object, "text_blocks"):
            for text_block in input_object.text_blocks:
                x = self.resized_x - text_block.canvas_point.x
                y = self.resized_y - text_block.canvas_point.y
                x = x / self.relation
                y = y / self.relation
                text_block.canvas_point.set_x(x)
                text_block.canvas_point.set_y(y)

    def resize_coordinates(self, input_coordinates):

        result_coordinates = []
        for coordinate in input_coordinates:
            if type(coordinate) == list:
                for el in coordinate:
                    result_coordinates.append(self.resize_coordinates(el))
            else:
                result_coordinates.append(coordinate)

        if len(result_coordinates) > 1:
            if not type(result_coordinates[0]) == list:
                x, y = result_coordinates
                x = (self.resized_x - x) / self.relation
                y = (self.resized_y - y) / self.relation
                result_coordinates = [x, y]

        return result_coordinates
