advancement revoke @s only block-morph:tick/move

scoreboard players operation #tmp_id block-morph.id = @s block-morph.id
execute as @e[type=text_display,tag=block-morph.root] if score @s block-morph.id = #tmp_id block-morph.id run function block-morph:tick/root

execute if predicate block-morph:is_sneaking if predicate block-morph:is_motionless unless predicate block-morph:is_flying align xyz run function block-morph:player/modify/align