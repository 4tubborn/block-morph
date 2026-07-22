import json
import os

def generate_vine_child_model(direction: str) -> dict:
    face_config = {
        "uv": [16, 0, 0, 16],
        "texture": "#vine",
        "tintindex": 0
    }

    element = {
        "from": [0, 0, 0.8],
        "to": [16, 16, 0.8],
        "shade": False,
        "faces": {
            "north": face_config,
            "south": face_config
        }
    }

    # 根据方向给 Element 加上 3D 空间旋转
    if direction == "vine_west":
        element["rotation"] = {"origin": [8, 8, 8], "axis": "y", "angle": 90}
    elif direction == "vine_north":
        element["rotation"] = {"origin": [8, 8, 8], "axis": "y", "angle": 180}
    elif direction == "vine_east":
        element["rotation"] = {"origin": [8, 8, 8], "axis": "y", "angle": 270}
    elif direction == "vine_up":
        element["rotation"] = {"origin": [8, 8, 8], "axis": "x", "angle": -90}
    # vine_south 保持 0 度不加 rotation

    return {
        "parent": "minecraft:block/vine",
        "elements": [element]
    }

if __name__ == "__main__":
    models_dir = "../assets/minecraft/models/block"
    os.makedirs(models_dir, exist_ok=True)

    directions = ["vine_north", "vine_east", "vine_south", "vine_west", "vine_up"]
    for name in directions:
        model_data = generate_vine_child_model(name)
        with open(os.path.join(models_dir, f"{name}.json"), "w", encoding="utf-8") as f:
            json.dump(model_data, f, separators=(',', ':'), ensure_ascii=False)

    print("已使用 Element rotation 修正 5 个朝向模型！")

#实际上有些朝向相反了，手动修正