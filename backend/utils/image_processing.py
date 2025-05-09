from PIL import Image
import numpy as np
from typing import Iterator, Tuple, Dict, Any

def read_image(file) -> Image.Image:
    """读取上传的图片文件"""
    return Image.open(file.file)

def grid_iter(grid_x: int, grid_y: int) -> Iterator[Tuple[int, int]]:
    """生成网格坐标迭代器"""
    for x in range(grid_x):
        for y in range(grid_y):
            yield x, y

def crop_tile(image: Image.Image, x: int, y: int, tile_size: int = 32) -> Image.Image:
    """裁剪指定位置的图块"""
    left = x * tile_size
    upper = y * tile_size
    right = left + tile_size
    lower = upper + tile_size
    return image.crop((left, upper, right, lower))

def predict_tile(tile: Image.Image) -> Dict[str, Any]:
    """预测单个图块的属性"""
    # TODO: 集成实际预测模型
    return {
        "color": get_dominant_color(tile),
        "material": "stone",  # 示例值
        "height": 1           # 示例值
    }

def get_dominant_color(image: Image.Image) -> str:
    """获取图片主色调(HEX格式)"""
    np_image = np.array(image)
    colors, count = np.unique(np_image.reshape(-1, 3), axis=0, return_counts=True)
    dominant = colors[count.argmax()]
    return f"#{dominant[0]:02x}{dominant[1]:02x}{dominant[2]:02x}"