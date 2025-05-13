from typing import Optional
from PIL import Image

class AttributePredictor:
    def __init__(self):
        pass
        
    def predict(self, tile_image: Image.Image, context: Optional[Image.Image] = None) -> dict:
        """
        预测瓦片属性
        :param tile_image: 瓦片图像
        :param context: 可选上下文图像
        :return: {
            'height': float,
            'rotation': float,
            'variant': str
        }
        """
        raise NotImplementedError("AttributePredictor.predict() not implemented")