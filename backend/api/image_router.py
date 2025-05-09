from fastapi import APIRouter, UploadFile
from typing import Optional
from ..utils.image_processing import (
    read_image,
    grid_iter,
    crop_tile,
    predict_tile
)

router = APIRouter()

@router.post("/analyze")
async def analyze_image(
    file: UploadFile,
    grid_x: int,
    grid_y: int,
    z: int = 0
):
    """分析上传的图片并返回网格化预测结果
    
    Args:
        file: 上传的图片文件
        grid_x: X轴网格数
        grid_y: Y轴网格数
        z: Z轴位置(默认0)
    """
    image = await read_image(file)
    tiles = []
    
    for x, y in grid_iter(grid_x, grid_y):
        block = crop_tile(image, x, y)
        tile = predict_tile(block)
        tile.update({"x": x, "y": z, "z": y})
        tiles.append(tile)
        
    return {"tiles": tiles}