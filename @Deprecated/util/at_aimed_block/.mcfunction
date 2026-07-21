#input: run:<string>
$data modify storage block-morph:util at_aimed_block.run set value "$(run)"

execute store result score #max_step block-morph.util run attribute @s block_interaction_range get 16
scoreboard players set #step block-morph.util 0

function block-morph:util/at_aimed_block/loop