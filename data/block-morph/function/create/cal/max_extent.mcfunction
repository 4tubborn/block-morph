scoreboard players set #extent.x block-morph.structure 10
scoreboard players operation #extent.x block-morph.structure += #max.x block-morph.structure
scoreboard players operation #extent.x block-morph.structure -= #min.x block-morph.structure

scoreboard players set #extent.y block-morph.structure 10
scoreboard players operation #extent.y block-morph.structure += #max.y block-morph.structure
scoreboard players operation #extent.y block-morph.structure -= #min.y block-morph.structure

scoreboard players set #extent.z block-morph.structure 10
scoreboard players operation #extent.z block-morph.structure += #max.z block-morph.structure
scoreboard players operation #extent.z block-morph.structure -= #min.z block-morph.structure

scoreboard players operation #max_extent block-morph.structure = #extent.x block-morph.structure
execute if score #extent.y block-morph.structure > #max_extent block-morph.structure run scoreboard players operation #max_extent block-morph.structure = #extent.y block-morph.structure
execute if score #extent.z block-morph.structure > #max_extent block-morph.structure run scoreboard players operation #max_extent block-morph.structure = #extent.z block-morph.structure