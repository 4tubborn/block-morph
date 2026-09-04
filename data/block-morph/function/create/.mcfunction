#scoreboard players reset #total.x block-morph.structure
#scoreboard players reset #total.y block-morph.structure
#scoreboard players reset #total.z block-morph.structure
function #block-morph:api/create/start

scoreboard players set #min.x block-morph.structure 2147483647
scoreboard players set #max.x block-morph.structure -2147483648
scoreboard players set #min.y block-morph.structure 2147483647
scoreboard players set #max.y block-morph.structure -2147483648
scoreboard players set #min.z block-morph.structure 2147483647
scoreboard players set #max.z block-morph.structure -2147483648

scoreboard players set #block_count block-morph.structure 0
scoreboard players set #tint block-morph.tint 0
#scoreboard players set #center.y block-morph.structure 2048

#如果对准的不是可以实体化的方块，或者max_block_count为0就return
execute unless function block-morph:create/post_update/self run return fail

#原本计算重心的逻辑
#function block-morph:create/cal/center

#data remove storage block-morph:tmp root

#execute store result storage block-morph:tmp root.x double 0.1 run scoreboard players get #center.x block-morph.structure
#execute store result storage block-morph:tmp root.y double 0.1 run scoreboard players get #center.y block-morph.structure
#execute store result storage block-morph:tmp root.z double 0.1 run scoreboard players get #center.z block-morph.structure

#tellraw @a ["total: ",{score:{name:"#total.x",objective:"block-morph.structure"}}," ",{score:{name:"#total.y",objective:"block-morph.structure"}}," ",{score:{name:"#total.z",objective:"block-morph.structure"}}," ",]

#tellraw @a ["center: ",{score:{name:"#center.x",objective:"block-morph.structure"}}," ",{score:{name:"#center.y",objective:"block-morph.structure"}}," ",{score:{name:"#center.z",objective:"block-morph.structure"}}," ",]

function block-morph:create/cal/max_extent
#center依赖extent
function block-morph:create/cal/center

#tellraw @a ["extent: ",{score:{name:"#extent.x",objective:"block-morph.structure"}}," ",{score:{name:"#extent.y",objective:"block-morph.structure"}}," ",{score:{name:"#extent.z",objective:"block-morph.structure"}}," ",]
#tellraw @a ["half extent: ",{score:{name:"#half_extent.x",objective:"block-morph.structure"}}," ",{score:{name:"#half_extent.y",objective:"block-morph.structure"}}," ",{score:{name:"#half_extent.z",objective:"block-morph.structure"}}," ",]


#center
#execute store result storage block-morph:tmp root.x double 0.1 run scoreboard players get #center.x block-morph.structure
#execute store result storage block-morph:tmp root.y double 0.1 run scoreboard players get #center.y block-morph.structure
#execute store result storage block-morph:tmp root.z double 0.1 run scoreboard players get #center.z block-morph.structure
#root & bde/ide
function block-morph:create/set/root

#align模式
function block-morph:create/cal/align
#玩家处理

execute store result storage block-morph:tmp player.camera_distance int 0.3 run scoreboard players get #max_extent block-morph.structure
function block-morph:player/modify/camera_distance with storage block-morph:tmp player

function block-morph:player/start

#tellraw @a ["count: ",{score:{name:"#block_count",objective:"block-morph.structure"}}]

scoreboard players add #global_id block-morph.id 1

function #block-morph:api/create/finish