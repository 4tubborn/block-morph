# Develop

## APIs

These APIs are function tags.

### `#block-morph:api/create/start`

Execute when start to create the structure.

Execution Context:

|Type|Value|
|---|---|
|Executor|The player who creates the structure|
|Dimension|Where the player is in|
|Position|The position of player|
|Rotation|The rotation of player|
|Anchor|The feet of the player|

### `#block-morph:api/create/loop`

Execute when post update to blocks that are legal in the structure, before removing the blocks.

Execution Context:

|Type|Value|
|---|---|
|Executor|The player who creates the structure/The block entity or the the item entity[^1]|
|Dimension|Where the player is in|
|Position|The position of block|
|Rotation|The rotation of player|
|Anchor|The feet of the player|

[^1]: The first time is the player and all other updates are block/item entities.

### `#block-morph:api/create/finish`

Execute when finish to create the structure.

Execution Context:

|Type|Value|
|---|---|
|Executor|The player who creates the structure|
|Dimension|Where the player is in|
|Position|The position of player|
|Rotation|The rotation of player|
|Anchor|The feet of the player|

