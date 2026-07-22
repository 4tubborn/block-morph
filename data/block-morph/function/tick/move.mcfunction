advancement revoke @s only block-morph:tick/move

execute if predicate block-morph:should_align align xz run function block-morph:player/modify/align

scoreboard players operation #tmp_id block-morph.id = @s block-morph.id
execute as @e[type=text_display,tag=block-morph.root,predicate=block-morph:equal_id] run return run function block-morph:tick/root

function block-morph:player/lose_root