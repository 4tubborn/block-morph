advancement revoke @s only block-morph:structure/remove

function #block-morph:api/blockify/start

scoreboard players operation #tmp_id block-morph.id = @s block-morph.id
execute as @e[type=text_display,tag=block-morph.root,distance=..1] if score @s block-morph.id = #tmp_id block-morph.id at @s align xyz run function block-morph:blockify/root

function #block-morph:api/blockify/finish

function block-morph:player/stop