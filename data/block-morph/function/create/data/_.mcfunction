tag @s add block-morph.init
tag @s add block-morph.visual

setblock ~ ~ ~ air strict

#summon shulker ^ ^ ^ {Tags:["phys.init","phys.en"],Glowing:true,active_effects:[{id:"invisibility",amplifier:1b,duration:-1,show_particles:0b}],AttachFace:0b,Invulnerable:1b,NoAI:1b,NoGravity:1b,PersistenceRequired:1b,Silent:1b}
#ride @n[type=shulker,distance=..1,tag=phys.init] mount @s
#execute on passengers run tag @s remove phys.init

#tellraw @a ["pos: ",{entity:"@s",nbt:"Pos"}]
#
#实际pos: x,z,y不偏移
execute store result score @s block-morph.pos.x run data get entity @s Pos[0] 10
execute store result score @s block-morph.pos.y run data get entity @s Pos[1] 10
execute store result score @s block-morph.pos.z run data get entity @s Pos[2] 10

#scoreboard players operation #total.x block-morph.structure += @s block-morph.pos.x
#scoreboard players operation #total.y block-morph.structure += @s block-morph.pos.y
#scoreboard players operation #total.z block-morph.structure += @s block-morph.pos.z
#execute if score @s block-morph.pos.y < #center.y block-morph.structure run scoreboard players operation #center.y block-morph.structure = @s block-morph.pos.y

#tellraw @a ["score_pos: ",{score:{name:"@s",objective:"phys.pos.x"}},", ",{score:{name:"@s",objective:"phys.pos.y"}},", ",{score:{name:"@s",objective:"phys.pos.z"}},", "]
#不偏移到底面中心
#scoreboard players operation @s block-morph.pos.x += #5 block-morph.util.const
#scoreboard players operation @s block-morph.pos.y += #5 block-morph.util.const
#scoreboard players operation @s block-morph.pos.z += #5 block-morph.util.const

#更新min/max
# --- X 轴 ---
execute if score @s block-morph.pos.x < #min.x block-morph.structure run scoreboard players operation #min.x block-morph.structure = @s block-morph.pos.x
execute if score @s block-morph.pos.x > #max.x block-morph.structure run scoreboard players operation #max.x block-morph.structure = @s block-morph.pos.x
# --- Y 轴 ---
execute if score @s block-morph.pos.y < #min.y block-morph.structure run scoreboard players operation #min.y block-morph.structure = @s block-morph.pos.y
execute if score @s block-morph.pos.y > #max.y block-morph.structure run scoreboard players operation #max.y block-morph.structure = @s block-morph.pos.y
# --- Z 轴 ---
execute if score @s block-morph.pos.z < #min.z block-morph.structure run scoreboard players operation #min.z block-morph.structure = @s block-morph.pos.z
execute if score @s block-morph.pos.z > #max.z block-morph.structure run scoreboard players operation #max.z block-morph.structure = @s block-morph.pos.z