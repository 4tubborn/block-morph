advancement revoke @s only block-morph:structure/create

scoreboard players set #single block-morph.structure 0

function #bs.view:at_aimed_block {run:"function #block-morph:start",with:{}}