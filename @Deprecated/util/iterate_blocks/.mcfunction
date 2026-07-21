#get extent
$summon marker $(from) {Tags:["block-morph.util.ce1","block-morph.util"]}
$summon marker $(to) {Tags:["block-morph.util.ce2","block-morph.util"]}

execute store result score #extent.x block-morph.util run data get entity @n[type=marker,tag=block-morph.util.ce1] Pos[0]
execute store result score #extent.y block-morph.util run data get entity @n[type=marker,tag=block-morph.util.ce1] Pos[1]
execute store result score #extent.z block-morph.util run data get entity @n[type=marker,tag=block-morph.util.ce1] Pos[2]

execute store result score #end.x block-morph.util run data get entity @n[type=marker,tag=block-morph.util.ce2] Pos[0]
execute store result score #end.y block-morph.util run data get entity @n[type=marker,tag=block-morph.util.ce2] Pos[1]
execute store result score #end.z block-morph.util run data get entity @n[type=marker,tag=block-morph.util.ce2] Pos[2]

scoreboard players operation #extent.x block-morph.util -= #end.x block-morph.util
scoreboard players operation #extent.y block-morph.util -= #end.y block-morph.util
scoreboard players operation #extent.z block-morph.util -= #end.z block-morph.util

#execute if score #extent.x block-morph.util matches ..-1 run scoreboard players operation #extent.x block-morph.util *= #-1 block-morph.util.const
#execute if score #extent.y block-morph.util matches ..-1 run scoreboard players operation #extent.y block-morph.util *= #-1 block-morph.util.const
#execute if score #extent.z block-morph.util matches ..-1 run scoreboard players operation #extent.z block-morph.util *= #-1 block-morph.util.const

say 1

kill @e[type=marker,limit=2,tag=block-morph.util]

$data modify storage block-morph:util iterate_blocks.run set value "$(run)"
#loop
$execute positioned $(from) run function block-morph:util/iterate_blocks/loop/