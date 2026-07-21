execute if score #step block-morph.util > #max_step block-morph.util run return fail
execute unless block ~ ~ ~ #air align xyz run return run function block-morph:util/at_aimed_block/end with storage block-morph:util at_aimed_block
scoreboard players add #step block-morph.util 1
execute positioned ^ ^ ^0.0625 run function block-morph:util/at_aimed_block/loop