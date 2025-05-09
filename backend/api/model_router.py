from fastapi import APIRouter, UploadFile, File
from PIL import Image
import io
from ai_models.tile_map_generator.model import TileMapGenerator
from ai_models.texture_synthesizer.model import TextureSynthesizer
from ai_models.attribute_predictor.model import AttributePredictor

router = APIRouter(prefix="/models", tags=["AI Models"])

tile_map_generator = TileMapGenerator()
texture_synthesizer = TextureSynthesizer()
attribute_predictor = AttributePredictor()

@router.post("/generate-tile-map")
async def generate_tile_map(
    image: UploadFile = File(...),
    rows: int = 10,
    cols: int = 10
):
    """生成瓦片地图API"""
    image_data = await image.read()
    img = Image.open(io.BytesIO(image_data))
    result = tile_map_generator.generate(img, (rows, cols))
    return result

@router.post("/synthesize-texture")
async def synthesize_texture(
    tile_type: str,
    context_image: UploadFile = File(None)
):
    """生成纹理贴图API"""
    context = None
    if context_image:
        context_data = await context_image.read()
        context = Image.open(io.BytesIO(context_data))
    result = texture_synthesizer.synthesize(tile_type, context)
    return {"texture": result}

@router.post("/predict-attributes")
async def predict_attributes(
    tile_image: UploadFile = File(...),
    context_image: UploadFile = File(None)
):
    """预测瓦片属性API"""
    tile_img_data = await tile_image.read()
    tile_img = Image.open(io.BytesIO(tile_img_data))
    
    context = None
    if context_image:
        context_data = await context_image.read()
        context = Image.open(io.BytesIO(context_data))
    
    result = attribute_predictor.predict(tile_img, context)
    return result