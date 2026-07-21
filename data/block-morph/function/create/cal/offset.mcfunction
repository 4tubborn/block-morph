scoreboard players operation @s block-morph.offset.x = @s block-morph.pos.x
scoreboard players operation @s block-morph.offset.x -= #center.x block-morph.structure

scoreboard players operation @s block-morph.offset.y = @s block-morph.pos.y
scoreboard players operation @s block-morph.offset.y -= #center.y block-morph.structure

scoreboard players operation @s block-morph.offset.z = @s block-morph.pos.z
scoreboard players operation @s block-morph.offset.z -= #center.z block-morph.structure

execute as @s[type=item_display] run function block-morph:create/cal/offset_ide