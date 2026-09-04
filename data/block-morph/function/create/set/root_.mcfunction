
data modify entity @s {} merge value {teleport_duration:3}

tag @s add block-morph.root

scoreboard players operation @s block-morph.id = #global_id block-morph.id
scoreboard players operation @s block-morph.tint = #tint block-morph.tint

tag @s add block-morph.init