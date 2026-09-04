function block-morph:create/cal/offset

execute store result entity @s transformation.translation[0] double 0.1 run scoreboard players get @s block-morph.offset.x
execute store result entity @s transformation.translation[1] double 0.1 run scoreboard players get @s block-morph.offset.y
execute store result entity @s transformation.translation[2] double 0.1 run scoreboard players get @s block-morph.offset.z

#tellraw @a ["tr: ",{entity:"@s",nbt:"transformation.translation"}]
#tellraw @a ["pos: ",{score:{name:"@s",objective:"block-morph.pos.x"}}," ",{score:{name:"@s",objective:"block-morph.pos.y"}}," ",{score:{name:"@s",objective:"block-morph.pos.z"}}," ",]

tag @s remove block-morph.init
ride @s mount @n[type=text_display,tag=block-morph.init,tag=block-morph.root]