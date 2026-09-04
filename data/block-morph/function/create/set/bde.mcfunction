function block-morph:create/cal/offset

data modify storage block-morph:tmp set.bde set value {transformation:{translation:[0,0,0]}}

execute store result storage block-morph:tmp set.bde.transformation.translation[0] double 0.1 run scoreboard players get @s block-morph.offset.x
execute store result storage block-morph:tmp set.bde.transformation.translation[1] double 0.1 run scoreboard players get @s block-morph.offset.y
execute store result storage block-morph:tmp set.bde.transformation.translation[2] double 0.1 run scoreboard players get @s block-morph.offset.z

data modify entity @s {} merge from storage block-morph:tmp set.bde

#tellraw @a ["tr: ",{entity:"@s",nbt:"transformation.translation"}]
#tellraw @a ["pos: ",{score:{name:"@s",objective:"block-morph.pos.x"}}," ",{score:{name:"@s",objective:"block-morph.pos.y"}}," ",{score:{name:"@s",objective:"block-morph.pos.z"}}," ",]

tag @s remove block-morph.init
ride @s mount @n[type=text_display,tag=block-morph.init,tag=block-morph.root]