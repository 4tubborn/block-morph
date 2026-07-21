scoreboard players operation #p block-morph.offset.x = @s block-morph.offset.x
scoreboard players operation #p block-morph.offset.y = @s block-morph.offset.y
scoreboard players operation #p block-morph.offset.z = @s block-morph.offset.z

function block-morph:blockify/bde/_

execute store result storage block-morph:tmp block.x double 0.1 run scoreboard players get #p block-morph.offset.x
execute store result storage block-morph:tmp block.y double 0.1 run scoreboard players get #p block-morph.offset.y
execute store result storage block-morph:tmp block.z double 0.1 run scoreboard players get #p block-morph.offset.z
data modify storage block-morph:tmp block.block set from entity @s data.block-morph.block_string

#tellraw @a ["scores: ",{score:{name:"@s",objective:"block-morph.offset.x"}}," ",{score:{name:"@s",objective:"block-morph.offset.y"}}," ",{score:{name:"@s",objective:"block-morph.offset.z"}}," ",]

function block-morph:blockify/bde/place with storage block-morph:tmp block

function #block-morph:api/blockify/loop

kill @s