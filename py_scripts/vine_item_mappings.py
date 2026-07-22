import json
import re
import os

import config

def name_to_id(name: str) -> str:
    snake = re.sub(r'[\s\-]+', '_', name.strip()).lower()
    return f"minecraft:{snake}"

def hex_to_int(hex_str: str) -> int:
    val = int(hex_str.strip().lstrip('#'), 16)
    if val & (1 << 23):
        val |= -16777216
    return val

foliage_colors = {}
for line in config.raw_csv_data.strip().split('\n'):
    if not line or '|' not in line:
        continue
    parts = line.split('|')
    biomes, grass_hex, foliage_hex, dry_hex = [p.strip() for p in parts]
    f_val = hex_to_int(foliage_hex)
    for b in biomes.split(','):
        foliage_colors[name_to_id(b)] = f_val

INV_DEFAULT = -12012264

def create_model_node(model_path: str, color_val: int = None) -> dict:
    node = {
        "type": "minecraft:model",
        "model": model_path
    }
    if color_val is not None:
        node["tints"] = [{"type": "minecraft:constant", "value": color_val}]
    return node

def build_condition_tree(items: list, block_model: str, fallback_model: str, fallback_color: int, index: int = 0) -> dict:
    if index >= len(items):
        return create_model_node(fallback_model, color_val=fallback_color)

    biome_id, color_val = items[index]
    return {
        "type": "condition",
        "property": "component",
        "predicate": "custom_data",
        "value": {
            "block-morph": {
                "data": {
                    "biome": biome_id
                }
            }
        },
        "on_true": create_model_node(block_model, color_val=color_val),
        "on_false": build_condition_tree(items, block_model, fallback_model, fallback_color, index + 1)
    }

def generate_vine_item_model(foliage_items: list) -> dict:
    directions = ["north", "east", "south", "west", "up"]
    composite_models = []

    # 2D 手持物品形态的 condition 染色树
    fallback_2d_tree = build_condition_tree(
        items=foliage_items,
        block_model="minecraft:item/vine",
        fallback_model="minecraft:item/vine",
        fallback_color=INV_DEFAULT
    )

    # 空模型
    air_node = {
        "type": "minecraft:model",
        "model": "minecraft:item/air"
    }

    for idx, dir_name in enumerate(directions):
        block_model = f"minecraft:block/vine_{dir_name}"

        # 3D 方向模型的 condition 树
        dir_condition_tree = build_condition_tree(
            items=foliage_items,
            block_model=block_model,
            fallback_model=block_model,
            fallback_color=INV_DEFAULT
        )

        if idx == 0:
            # 第 1 个 select (north)：true 为 3D 模型，false 为 air，fallback 为 2D 手持模型
            select_node = {
                "type": "minecraft:select",
                "property": "minecraft:block_state",
                "block_state_property": dir_name,
                "cases": [
                    {
                        "when": "true",
                        "model": dir_condition_tree
                    },
                    {
                        "when": "false",
                        "model": air_node
                    }
                ],
                "fallback": fallback_2d_tree
            }
        else:
            # 后续 select (east, south, west, up)：true 为 3D 模型，false 与 fallback 均为 air
            select_node = {
                "type": "minecraft:select",
                "property": "minecraft:block_state",
                "block_state_property": dir_name,
                "cases": [
                    {
                        "when": "true",
                        "model": dir_condition_tree
                    }
                ],
                "fallback": air_node
            }

        composite_models.append(select_node)

    return {
        "model": {
            "type": "minecraft:composite",
            "models": composite_models
        }
    }

if __name__ == "__main__":
    models_dir = "../assets/minecraft/models/item"
    os.makedirs(config.output_dir, exist_ok=True)
    os.makedirs(models_dir, exist_ok=True)

    # 1. 生成 2D 手持模型 assets/minecraft/models/item/vine.json
    fallback_item_model = {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": "minecraft:block/vine"
        }
    }
    with open(os.path.join(models_dir, "vine.json"), "w", encoding="utf-8") as f:
        json.dump(fallback_item_model, f, indent=2, ensure_ascii=False)

    # 2. 生成 items/vine.json 核心逻辑定义
    foliage_items = list(foliage_colors.items())
    vine_data = generate_vine_item_model(foliage_items)
    with open(os.path.join(config.output_dir, "vine.json"), "w", encoding="utf-8") as f:
        json.dump(vine_data, f, separators=(',', ':'), ensure_ascii=False)

    print("导出成功！已将第 1 个 select 配置为：true -> 3D模型, false -> air, fallback -> 2D物品模型。")