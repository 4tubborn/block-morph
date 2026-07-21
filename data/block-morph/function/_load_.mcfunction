forceload add 0 0

scoreboard objectives add block-morph.util.const dummy
scoreboard objectives add block-morph.structure dummy

scoreboard objectives add block-morph.pos.x dummy
scoreboard objectives add block-morph.pos.y dummy
scoreboard objectives add block-morph.pos.z dummy

scoreboard objectives add block-morph.offset.x dummy
scoreboard objectives add block-morph.offset.y dummy
scoreboard objectives add block-morph.offset.z dummy

scoreboard objectives add block-morph.id dummy

scoreboard objectives add block-morph.align dummy
#是否要着色
scoreboard objectives add block-morph.tint dummy

scoreboard players set #-1 block-morph.util.const -1
scoreboard players set #2 block-morph.util.const 2
scoreboard players set #5 block-morph.util.const 5
scoreboard players set #10 block-morph.util.const 10
scoreboard players set #100 block-morph.util.const 100
scoreboard players set #1000 block-morph.util.const 1000

execute unless score #global_id block-morph.id matches 0.. run scoreboard players set #global_id block-morph.id 0
execute unless score #max_block_count block-morph.structure matches 0.. run scoreboard players set #max_block_count block-morph.structure 100