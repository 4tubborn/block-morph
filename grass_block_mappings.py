import json
import os
import re

# 1. 原始生物群系与颜色数据 (CSV)
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
    snake = re.sub(r"[\s\-]+", "_", name.strip()).lower()
    return f"minecraft:{snake}"


def hex_to_int(hex_str: str) -> int:
    val = int(hex_str.strip().lstrip("#"), 16)
    if val & (1 << 23):
        val |= -16777216
    return val


# 2. 解析 CSV 第一列颜色（草色 Grass Color）
grass_colors = {}
for line in raw_csv_data.strip().split("\n"):
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
    output_dir = "assets/minecraft/items"
    os.makedirs(output_dir, exist_ok=True)

    json_data = generate_grass_block_json()
    output_path = os.path.join(output_dir, "grass_block.json")

    with open(output_path, "w", encoding="utf-8") as f:
        # 紧凑化输出 (压缩体积)
        json.dump(json_data, f, separators=(",", ":"), ensure_ascii=False)

    print(f"已成功在 '{output_path}' 生成草方块专属 item_model JSON！")