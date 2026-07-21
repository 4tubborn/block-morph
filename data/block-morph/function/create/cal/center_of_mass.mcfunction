#center.x/z,1e1;center.y,1e1
scoreboard players operation #center.x block-morph.structure = #total.x block-morph.structure
#scoreboard players operation #center.x block-morph.structure *= #100 block-morph.util.const
scoreboard players operation #center.x block-morph.structure /= #block_count block-morph.structure

scoreboard players operation #center.x block-morph.structure += #5 block-morph.util.const

scoreboard players operation #center.z block-morph.structure = #total.z block-morph.structure
#scoreboard players operation #center.z block-morph.structure *= #100 block-morph.util.const
scoreboard players operation #center.z block-morph.structure /= #block_count block-morph.structure

scoreboard players operation #center.z block-morph.structure += #5 block-morph.util.const