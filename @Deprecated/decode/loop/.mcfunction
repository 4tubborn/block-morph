data remove storage block-morph:decode cur_term
data modify storage block-morph:decode cur_term set from storage block-morph:in root[0]
execute unless data storage block-morph:decode cur_term run return 1
data remove storage block-morph:in root[0]

execute if data storage block-morph:decode {cur_term:{type:"item"}} run return run function block-morph:decode/loop/item
return run function block-morph:decode/loop/block