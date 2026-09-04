tellraw @s [\
    {text:""},\
    {color:yellow,translate:"panel.block-morph.set_rules",with:[\
        {color:green,translate:"panel.block-morph.set_rules.reset",click_event:{action:"run_command",command:"/function block-morph:config/rule/reset"}},\
        {color:green,translate:"panel.block-morph.set_rules.max_block_count",click_event:{action:"suggest_command",command:"/scoreboard players set #max_block_count block-morph.structure "}},\
        {color:green,translate:"panel.block-morph.set_rules.interpolation",click_event:{action:"suggest_command",command:"/scoreboard players set #max_block_count block-morph.structure "}},\
    ],},\
]