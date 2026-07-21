scoreboard players set @s block-morph.align 0

scoreboard players operation #align.x block-morph.structure = #center.x block-morph.structure
scoreboard players operation #align.x block-morph.structure %= #10 block-morph.util.const

scoreboard players operation #align.z block-morph.structure = #center.z block-morph.structure
scoreboard players operation #align.z block-morph.structure %= #10 block-morph.util.const

tellraw @a ["align: ",{score:{name:"#align.x",objective:"block-morph.structure"}}," ",{score:{name:"#align.z",objective:"block-morph.structure"}}," ",]

execute if score #align.x block-morph.structure matches 0 run scoreboard players add @s block-morph.align 1
execute if score #align.z block-morph.structure matches 0 run scoreboard players add @s block-morph.align 2