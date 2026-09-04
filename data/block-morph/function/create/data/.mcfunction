scoreboard players add #block_count block-morph.structure 1

function #bs.block:get_block

execute unless block ~ ~ ~ #block-morph:tinted summon block_display run return run function block-morph:create/data/bde
return run execute summon item_display run function block-morph:create/data/ide