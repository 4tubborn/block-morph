import json
import os
import re

import config

def name_to_id(name: str) -> str:
    snake = re.sub(r"[\s\-]+", "_", name.strip()).lower()
    return f"minecraft:{snake}"


def hex_to_int(hex_str: str) -> int:
    val = int(hex_str.strip().lstrip("#"), 16)
    if val & (1 << 23):
        val |= -16777216
    return val


# 2. 解析 CSV 第一列颜色（草色 Grass Color）
grass_colors = {}
for line in config.raw_csv_data.strip().split("\n"):
    if not line or "|" not in line:
        continue
    parts = line.split("|")
    biomes = parts[0].strip()
    grass_hex = parts[1].strip()  # 第一列草色
    g_val = hex_to_int(grass_hex)

    for b in biomes.split(","):
        grass_colors[name_to_id(b)] = g_val


def create_model_node(
    model_path: str,
    color_val: int = None,
    is_grass_fallback: bool = False,
) -> dict:
    node = {"type": "minecraft:model", "model": model_path}
    if is_grass_fallback:
        node["tints"] = [
            {"type": "minecraft:grass", "downfall": 1.0, "temperature": 0.5}
        ]
    elif color_val is not None:
        node["tints"] = [{"type": "minecraft:constant", "value": color_val}]
    return node


def build_condition_tree(
    items: list, block_model: str, index: int = 0
) -> dict:
    """递归构建生物群系 Condition 匹配树"""
    # 递归终点：走到链条末端，使用 minecraft:grass 动态采样 fallback
    if index >= len(items):
        return create_model_node(block_model, is_grass_fallback=True)

    biome_id, color_val = items[index]
    return {
        "type": "condition",
        "property": "component",
        "predicate": "custom_data",
        "value": {"block-morph": {"data": {"biome": biome_id}}},
        "on_true": create_model_node(block_model, color_val=color_val),
        "on_false": build_condition_tree(items, block_model, index + 1),
    }


def generate_grass_block_json() -> dict:
    """生成草方块完整逻辑"""
    grass_items = list(grass_colors.items())

    # 1. 未下雪时的生物群系染色树 (snowy=false / fallback)
    normal_tinted_tree = build_condition_tree(
        items=grass_items, block_model="minecraft:block/grass_block"
    )

    # 2. 下雪时的静态雪顶模型 (snowy=true)，无染色
    snowy_node = create_model_node(
        model_path="minecraft:block/grass_block_snow"
    )

    # 3. 最外层 select：优先截断 snowy
    return {
        "model": {
            "type": "minecraft:select",
            "property": "minecraft:block_state",
            "block_state_property": "snowy",
            "cases": [{"when": "true", "model": snowy_node}],
            "fallback": normal_tinted_tree,
        }
    }


if __name__ == "__main__":
    
    os.makedirs(config.output_dir, exist_ok=True)

    json_data = generate_grass_block_json()
    output_path = os.path.join(config.output_dir, "grass_block.json")

    with open(output_path, "w", encoding="utf-8") as f:
        # 紧凑化输出 (压缩体积)
        json.dump(json_data, f, separators=(",", ":"), ensure_ascii=False)

    print(f"已成功在 '{output_path}' 生成草方块专属 item_model JSON！")