scoreboard players operation #step.y block-morph.util = #extent.y block-morph.util

function block-morph:util/iterate_blocks/loop/y

execute if score #step.x block-morph.util matches 0 run return 1
function block-morph:util/iterate_blocks2/loop/sx
execute as @s run function block-morph:util/iterate_blocks2/loop/x