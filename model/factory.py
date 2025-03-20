from model.rectangle_object import RectangleObject
# Import other object classes

class ObjectFactory:
    def create_object(self, type, id, **kwargs):
        if type == "rectangle":
            return RectangleObject(id, kwargs.get("x", 0), kwargs.get("y", 0),
                                 kwargs.get("width", 100), kwargs.get("height", 100),
                                 kwargs.get("z_order", 0))
        # Add cases for line, ellipse, text, image
        raise ValueError(f"Unknown object type: {type}")