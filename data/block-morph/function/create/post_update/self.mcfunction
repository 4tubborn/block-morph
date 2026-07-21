execute if score #max_block_count block-morph.structure matches 0 run return fail
#如果是single就只实体化一个方块
execute if score #single block-morph.structure matches 1 run return run function block-morph:create/data/
execute unless block ~ ~ ~ #block-morph:structure_disallowed run return run function block-morph:create/post_update/_
return fail