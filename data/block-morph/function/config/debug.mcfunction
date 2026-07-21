tellraw @s [\
    {text:""},\
    {color:yellow,translate:"kill:\n%s, %s, %s, %s",with:[\
        {color:green,translate:"[all]",click_event:{action:"run_command",command:"/function block-morph:config/kill/all"}},\
        {color:green,translate:"[force all]",click_event:{action:"run_command",command:"/function block-morph:config/kill/force_all"},hover_event:{action:"show_text",value:{translate:"Not recommended\nMay CORRUPT the World and Other Data Packs"}}},\
        {color:green,translate:"[nearby]",click_event:{action:"run_command",command:"/function block-morph:config/kill/nearby"}},\
        {color:green,translate:"[force nearby]",click_event:{action:"run_command",command:"/function block-morph:config/kill/force_nearby"},hover_event:{action:"show_text",value:{translate:"Not recommended\nMay CORRUPT the World and Other Data Packs"}}},\
    ],},\
]