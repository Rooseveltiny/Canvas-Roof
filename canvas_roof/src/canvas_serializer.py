import json
from canvas_roof.src.custom_errors import SerializeError

'''
    this module allows to prepare Canvas Objects to be json serailized
'''


class CanvasSlopeDataSerializer:

    def __init__(self, input_object):
        self.input_object = input_object
        self.output_data = None
        self._perform_prepear()

    def _perform_prepear(self):

        serialized_objects = self.collect_objects(
            self.input_object)

        data = {
            # "heights": self.input_object.sheets_heights,
            # "quantity": self.input_object.sheets_quantity,
            "all_objects": [serialized_objects],
        }

        self.output_data = data

    @property
    def data(self):
        if self.output_data:
            try:
                return json.dumps(self.output_data)
            except:
                pass
        raise SerializeError

    def serialize_coordinates(self, coordinates):
        return coordinates

    def collect_objects(self, canvas_object):

        data = {
            "all_coordinates": None,
            "all_objects": [],
            "strokeColor": None,
            "lineWidth": None,
            "text_blocks": []
        }

        if hasattr(canvas_object, "strokeColor"):
            data['strokeColor'] = canvas_object.strokeColor

        if hasattr(canvas_object, "lineWidth"):
            data['lineWidth'] = canvas_object.lineWidth

        if hasattr(canvas_object, "all_coordinates"):
            data['all_coordinates'] = self.serialize_coordinates(
                canvas_object.all_coordinates)

        if hasattr(canvas_object, "all_objects"):
            for obj in canvas_object.all_objects:
                data['all_objects'].append(self.collect_objects(obj))

        if hasattr(canvas_object, "text_blocks"):
            for text_block in canvas_object.text_blocks:
                data['text_blocks'].append(self.collect_text_blocks(text_block))

        return data

    def collect_text_blocks(self, text_block):
        text_block_serialialized = {
            "text": text_block.text,
            "all_coordinates": text_block.canvas_point.coordinates,
            "font_size": text_block.text_font
        }
        return text_block_serialialized
