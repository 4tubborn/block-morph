#scoreboard players operation #step.y block-morph.util = #extent.y block-morph.util

#function block-morph:util/iterate_blocks/loop/y
execute store result storage block-morph:util iterate_blocks.step_x int 1 run scoreboard players get #step.x block-morph.util
execute store result storage block-morph:util iterate_blocks.step_y int 1 run scoreboard players get #step.y block-morph.util
execute store result storage block-morph:util iterate_blocks.step_z int 1 run scoreboard players get #step.z block-morph.util

function block-morph:util/iterate_blocks/loop/run with storage block-morph:util iterate_blocks

execute if score #step.z block-morph.util matches 0 run return 1
function block-morph:util/iterate_blocks/loop/sz
function block-morph:util/iterate_blocks/loop/z