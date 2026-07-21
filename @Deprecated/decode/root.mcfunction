#execute summon text_display
summon text_display ~ ~ ~ {Tags:["block-morph.root","block-morph.init_root"],teleport_duration:1}

function block-morph:decode/loop/

execute as @e[x=0,y=-100,z=0,distance=..1,tag=block-morph.init] run ride @s mount @n[type=text_display,tag=block-morph.init_root,distance=..1]

execute as @n[type=text_display,tag=block-morph.init_root,distance=..1] run function block-morph:decode/_