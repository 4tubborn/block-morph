#multiplayer: interp=3 for accurate positions, singleplayer=1 for better visual effects
function block-morph:util/player_count
execute if score #player_count block-morph.util.const matches 1 run return run data modify storage block-morph:tmp set.root.interpolation_duration set value 1
data modify storage block-morph:tmp set.root.interpolation_duration set value 3