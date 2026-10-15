tellraw @s [\
    {color:yellow,translate:"panel.block-morph.set_rules"},{text:"",color:"green",extra:[\
        {translate:"panel.block-morph.set_rules.reset",click_event:{action:"run_command",command:"/function block-morph:config/rule/reset"}},{text:", "},\
        {translate:"panel.block-morph.set_rules.max_block_count",click_event:{action:"suggest_command",command:"/scoreboard players set #max_block_count block-morph.structure "}},{text:", "},\
        {translate:"panel.block-morph.set_rules.center",click_event:{action:"suggest_command",command:"/scoreboard players set #center block-morph.structure "}},\
    ]},\
]