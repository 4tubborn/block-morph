data remove storage block-morph:tmp init.bde

data modify storage block-morph:tmp init.bde.item.id set from storage bs:out block.item
data modify storage block-morph:tmp init.bde.item.components."minecraft:block_state" set from storage bs:out block.properties
#方块化时用到
data modify storage block-morph:tmp init.bde.data.block-morph.block_string set from storage bs:out block.block

#tellraw @a ["max count: ",{score:{name:"#max_block_count",objective:"block-morph.structure"}}]
#tellraw @a ["block count: ",{score:{name:"#block_count",objective:"block-morph.structure"}}]

#data modify storage block-morph:tmp init.bde.interpolation_duration set value 1

data modify entity @s {} merge from storage block-morph:tmp init.bde
#标记需要着色
scoreboard players set #tint block-morph.tint 1

function block-morph:create/data/_
return 1