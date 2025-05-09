# PixRise
像素图 → 自动 3D
| 模型编号 | 模型名                  | 输入                  | 输出                                             |
| ---- | -------------------- | ------------------- | ---------------------------------------------- |
| 模型1  | `TileMapGenerator`   | 原始图片 + 网格数          | 返回 tileMap：每个 tile 的类型、位置坐标（x, y, z）           |
| 模型2  | `TextureSynthesizer` | Tile 类型（可加 context） | 每个 tile 对应的贴图图像（dataURL / base64 PNG / tensor） |
| 模型3  | `AttributePredictor` | Tile图块或上下文图像        | 返回属性如高度、旋转角度、变种标签等（可选）                         |
 
 
        原始像素图（用户上传）
                    ↓
          [ 模型1 - Scene Parser ]
                    ↓
     tileMap: 每个格子的物体类型、位置坐标
                    ↓
     for each tile:
        → [ 模型2 - Texture Generator ]
        → [ 模型3 - Attribute Estimator ] ← 可选
                    ↓
          合并 tileMap + 贴图 + 属性 → 渲染
