tag @s add block-morph.root
tag @s add block-morph.init

function block-morph:create/set/root/interp

data modify entity @s {} merge from storage block-morph:tmp set.root

scoreboard players operation @s block-morph.id = #global_id block-morph.id
scoreboard players operation @s block-morph.tint = #tint block-morph.tint

#block list
execute store result storage block-morph:tmp macro.id int 1 run scoreboard players get #global_id block-morph.id
function block-morph:create/set/root/store_list with storage block-morph:tmp macro

execute as @e[type=#block-morph:display,tag=block-morph.init,tag=block-morph.visual] run function block-morph:create/set/bde

tag @s remove block-morph.init