#scoreboard players add #re_count block-morph.structure 1
$setblock ~$(x) ~$(y) ~$(z) air destroy
$setblock ~$(x) ~$(y) ~$(z) $(block) strict

#$say ~$(x) ~$(y) ~$(z) $(block)
#$data modify storage block-morph:tmp test append value [$(x),$(y),$(z)]s