data remove storage block-morph:tmp init.bde

data modify storage block-morph:tmp init.bde.block_state.Name set from storage bs:out block.type
data modify storage block-morph:tmp init.bde.block_state.Properties set from storage bs:out block.properties
#方块化时用到
data modify storage block-morph:tmp init.bde.data.block-morph.block_string set from storage bs:out block.block

#tellraw @a ["max count: ",{score:{name:"#max_block_count",objective:"block-morph.structure"}}]

#tellraw @a ["block count: ",{score:{name:"#block_count",objective:"block-morph.structure"}}]


data modify storage block-morph:tmp init.bde.interpolation_duration set value 1

data modify entity @s {} merge from storage block-morph:tmp init.bde

function block-morph:create/data/_
return 1