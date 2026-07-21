effect give @s invisibility infinite 255 true
tag @s add block-morph.in_morph

scoreboard players operation @s block-morph.id = #global_id block-morph.id

attribute @s scale modifier add block-morph:scaling -0.5 add_multiplied_total