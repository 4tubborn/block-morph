advancement revoke @s only block-morph:structure/create_single

scoreboard players set #single block-morph.structure 1

function #bs.view:at_aimed_block {run:"function #block-morph:start",with:{}}