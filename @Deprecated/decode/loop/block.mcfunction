summon block_display 0 -100 0 {Tags:["block-morph.init","block-morph.un","block-morph.visual"]}
data modify entity @n[type=block_display,x=0,y=-100,z=0,distance=..1,tag=block-morph.un] {} merge from storage block-morph:decode cur_term
tag @n[type=block_display,x=0,y=-100,z=0,distance=..1,tag=block-morph.un] remove block-morph.un