import json
import re
import os
import shutil

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

grass_colors = {}
foliage_colors = {}
dry_foliage_colors = {}

for line in raw_csv_data.strip().split('\n'):
    if not line or '|' not in line:
        continue
    parts = line.split('|')
    biomes, grass_hex, foliage_hex, dry_hex = [p.strip() for p in parts]
    
    g_val, f_val, d_val = hex_to_int(grass_hex), hex_to_int(foliage_hex), hex_to_int(dry_hex)
    
    for b in biomes.split(','):
        b_id = name_to_id(b)
        grass_colors[b_id] = g_val
        foliage_colors[b_id] = f_val
        dry_foliage_colors[b_id] = d_val

def create_tints(color_val: int = None, is_grass_fallback: bool = False) -> list:
    if is_grass_fallback:
        return [{
            "type": "minecraft:grass",
            "downfall": 1.0,
            "temperature": 0.5
        }]
    elif color_val is not None:
        return [{"type": "minecraft:constant", "value": color_val}]
    return []

def create_model_node(model_path: str, color_val: int = None, is_grass_fallback: bool = False) -> dict:
    node = {
        "type": "minecraft:model",
        "model": model_path
    }
    tints = create_tints(color_val, is_grass_fallback)
    if tints:
        node["tints"] = tints
    return node

def create_block_state_select_node(base_model_path: str, color_val: int = None, is_grass_fallback: bool = False) -> dict:
    # 针对高草丛/大型蕨构建 select block_state (half) 节点
    tints = create_tints(color_val, is_grass_fallback)
    
    upper_model = {
        "type": "minecraft:model",
        "model": f"{base_model_path}_top"
    }
    lower_model = {
        "type": "minecraft:model",
        "model": f"{base_model_path}_bottom"
    }
    fallback_model = {
        "type": "minecraft:model",
        "model": f"{base_model_path}_top"
    }
    
    if tints:
        upper_model["tints"] = tints
        lower_model["tints"] = tints
        fallback_model["tints"] = tints

    return {
        "type": "minecraft:select",
        "property": "minecraft:block_state",
        "block_state_property": "half",
        "cases": [
            {
                "when": "upper",
                "model": upper_model
            },
            {
                "when": "lower",
                "model": lower_model
            }
        ],
        "fallback": fallback_model
    }

def build_condition_tree(
    items: list, 
    block_model: str, 
    fallback_model: str = None, 
    fallback_color: int = None, 
    is_grass_fallback: bool = False, 
    has_half_property: bool = False,
    index: int = 0
) -> dict:
    target_fallback_model = fallback_model if fallback_model else block_model

    # 递归终止：到达链条末端，使用 fallback 模型的配置
    if index >= len(items):
        return create_model_node(
            target_fallback_model, 
            color_val=fallback_color, 
            is_grass_fallback=is_grass_fallback
        )

    biome_id, color_val = items[index]

    # 根据是否拥有 half 属性选择构建普通的 model 节点还是 select 节点
    if has_half_property:
        on_true_node = create_block_state_select_node(block_model, color_val=color_val)
    else:
        on_true_node = create_model_node(block_model, color_val=color_val)

    # 条件匹配成功：统一使用 block/ 下的模型
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
        "on_true": on_true_node,
        "on_false": build_condition_tree(
            items, 
            block_model=block_model, 
            fallback_model=fallback_model, 
            fallback_color=fallback_color, 
            is_grass_fallback=is_grass_fallback, 
            has_half_property=has_half_property,
            index=index + 1
        )
    }

# 常量定义
INV_DEFAULT = -12012264
INV_MANGROVE = hex_to_int("#92c648")


TARGET_BLOCKS = {
    # 动态树叶：(block_model, fallback_model, fallback_color, is_grass_fallback, has_half_property)
    "dynamic_leaves": {
        "oak_leaves": ("minecraft:block/oak_leaves", "minecraft:block/oak_leaves", INV_DEFAULT, False, False),
        "dark_oak_leaves": ("minecraft:block/dark_oak_leaves", "minecraft:block/dark_oak_leaves", INV_DEFAULT, False, False),
        "acacia_leaves": ("minecraft:block/acacia_leaves", "minecraft:block/acacia_leaves", INV_DEFAULT, False, False),
        "jungle_leaves": ("minecraft:block/jungle_leaves", "minecraft:block/jungle_leaves", INV_DEFAULT, False, False),
        "mangrove_leaves": ("minecraft:block/mangrove_leaves", "minecraft:block/mangrove_leaves", INV_MANGROVE, False, False),
        "vine": ("minecraft:block/vine", "minecraft:item/vine", INV_DEFAULT, False, False),
    },
    # 草地类：(block_model_base, fallback_model, fallback_color, is_grass_fallback, has_half_property)
    "grass_blocks": {
        #"grass_block": ("minecraft:block/grass_block", "minecraft:block/grass_block", None, True, False),
        "short_grass": ("minecraft:block/short_grass", "minecraft:item/short_grass", None, True, False),
        "tall_grass": ("minecraft:block/tall_grass", "minecraft:item/tall_grass", None, True, True),
        "fern": ("minecraft:block/fern", "minecraft:item/fern", None, True, False),
        "large_fern": ("minecraft:block/large_fern", "minecraft:item/large_fern", None, True, True),
        "bush": ("minecraft:block/bush", "minecraft:item/bush", None, True, False),
        "sugar_cane": ("minecraft:block/sugar_cane", "minecraft:item/sugar_cane", None, False, False)
    },
    # 枯叶类
    "dry_leaves_blocks": {
        "leaf_litter": ("minecraft:item/leaf_litter", "minecraft:item/leaf_litter", None, False, False)
    }
}

if __name__ == "__main__":
    output_dir = "assets/minecraft/items"

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    foliage_items = list(foliage_colors.items())
    grass_items = list(grass_colors.items())
    dry_items = list(dry_foliage_colors.items())

    # 1. 动态树叶
    for name, (b_model, fb_model, fb_color, is_grass_fb, has_half) in TARGET_BLOCKS["dynamic_leaves"].items():
        result = {"model": build_condition_tree(foliage_items, b_model, fb_model, fallback_color=fb_color, is_grass_fallback=is_grass_fb, has_half_property=has_half)}
        json_str = json.dumps(result, separators=(',', ':'), ensure_ascii=False)
        with open(os.path.join(output_dir, f"{name}.json"), "w", encoding="utf-8") as f:
            f.write(json_str)

    # 2. 草地类
    for name, (b_model, fb_model, fb_color, is_grass_fb, has_half) in TARGET_BLOCKS["grass_blocks"].items():
        result = {"model": build_condition_tree(grass_items, b_model, fb_model, fallback_color=fb_color, is_grass_fallback=is_grass_fb, has_half_property=has_half)}
        json_str = json.dumps(result, separators=(',', ':'), ensure_ascii=False)
        with open(os.path.join(output_dir, f"{name}.json"), "w", encoding="utf-8") as f:
            f.write(json_str)

    '''
    # 3. 枯叶类
    for name, (b_model, fb_model, fb_color, is_grass_fb) in TARGET_BLOCKS["dry_leaves_blocks"].items():
        result = {"model": build_condition_tree(dry_items, b_model, fb_model, fallback_color=fb_color, is_grass_fallback=is_grass_fb)}
        json_str = json.dumps(result, separators=(',', ':'), ensure_ascii=False)
        with open(os.path.join(output_dir, f"{name}.json"), "w", encoding="utf-8") as f:
            f.write(json_str)
    '''

    print("修复完成：Condition 判断内统一使用 block/ 模型，仅 fallback 使用 item/ 模型！并且给高草和大型蕨加入了 half block_state 判断。")