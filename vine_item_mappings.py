import json
import re
import os

raw_csv_data = """
Warm Ocean, Lukewarm Ocean, Deep Lukewarm Ocean, Ocean, Deep Ocean, Cold Ocean, Deep Cold Ocean, River, Deep Frozen Ocean, The Void, Lush Caves | #8eb971 | #71a74d | #a17448
Plains, Beach, Sunflower Plains, Deep Dark | #91bd59 | #77ab2f | #a37546
Dripstone Caves | #8db58a | #70a26c | #a36546
Frozen River, Frozen Ocean, Deep Frozen Ocean, Snowy Plains, Ice Spikes, Grove, Frozen Peaks, Jagged Peaks, Snowy Slopes, Snowy Taiga | #80b497 | #60a17b | #8f7a5a
Snowy Beach | #83b593 | #64a278 | #917958
Meadow, Cherry Grove | #83bb6d | #63a948 | #a17448
Desert, Savanna, Savanna Plateau, Windswept Savanna, Badlands, Wooded Badlands, Eroded Badlands | #bfb755 | #aea42a | #a38046
Windswept Savanna | #82c245 | #64b216 | #a37146
Forest, Flower Forest | #79c05a | #59ae30 | #a36d46
Dark Forest | #507a32 | #59ae30 | #7b5334
Birch Forest, Old Growth Birch Forest | #88bb67 | #6ba941 | #a37246
Old Growth Pine Taiga | #86b87f | #68a55f | #9c754d
Old Growth Spruce Taiga, Taiga | #86b783 | #68a464 | #9a764f
Windswept Gravelly Hills, Windswept Forest, Windswept Hills, Stony Shore | #8ab689 | #6da36b | #967753
Jungle, Bamboo Jungle | #59c93c | #30bb0b | #a36346
Sparse Jungle | #64c73f | #3eb80f | #a36646
Mushroom Fields | #55c93f | #2bbb0f | #a36246
Stony Peaks | #9abe4b | #82ac1e | #927957
Mangrove Swamp | #6a7039 | #6a7039 | #7b5334
Swamp | #6a7039 | #8db127 | #7b5334
Pale Garden | #778272 | #878D76 | #a0a69c
"""

def name_to_id(name: str) -> str:
    snake = re.sub(r'[\s\-]+', '_', name.strip()).lower()
    return f"minecraft:{snake}"

def hex_to_int(hex_str: str) -> int:
    val = int(hex_str.strip().lstrip('#'), 16)
    if val & (1 << 23):
        val |= -16777216
    return val

foliage_colors = {}
for line in raw_csv_data.strip().split('\n'):
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
                    },
                    {
                        "when": "false",
                        "model": air_node
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
    items_dir = "assets/minecraft/items"
    models_dir = "assets/minecraft/models/item"
    os.makedirs(items_dir, exist_ok=True)
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
    with open(os.path.join(items_dir, "vine.json"), "w", encoding="utf-8") as f:
        json.dump(vine_data, f, separators=(',', ':'), ensure_ascii=False)

    print("导出成功！已将第 1 个 select 配置为：true -> 3D模型, false -> air, fallback -> 2D物品模型。")