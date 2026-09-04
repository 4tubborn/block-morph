#scoreboard players reset #re_count block-morph.structure

#say block

#data remove storage block-morph:tmp test
execute store result storage block-morph:tmp macro.id int 1 run scoreboard players get @s block-morph.id
function block-morph:blockify/get_list with storage block-morph:tmp macro

execute on passengers run function block-morph:blockify/bde/

data remove storage block-morph:tmp blocks

#execute store result score #s block-morph.structure run data get storage block-morph:tmp test

#tellraw @a ["recount: ",{score:{name:"#s",objective:"block-morph.structure"}}]
#tellraw @a ["recount: ",{score:{name:"#re_count",objective:"block-morph.structure"}}]
kill @s