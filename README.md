# Block Morph

Turn into any block in Minecraft! A datapack that lets you transform into customized block structures or individual blocks.

> **Important:** This data pack **requires** the resource pack to render block models properly. Make sure to download it alongside the data pack!

## Features

Browse Screenshots in the [**Gallery**](https://modrinth.com/datapack/block-morph-datapack/gallery).

* **Become Any Block**: Seamlessly morph into block structures in the world.
* **Biome-Aware Plant Color**: Dynamic biome tinting for plants (grass, short grass, leaves, etc.).
* **Multiplayer Compatibility**: Have fun sneaking around as a block with your friends!

## Dependencies

To use this data pack, make sure you have installed the following required dependencies:

### Data Packs

Choose EITHER way to install Bookshelf:

* **Separate Modules**:
  * [Bookshelf View](https://modrinth.com/datapack/bookshelf-view)
  * [Bookshelf Block](https://modrinth.com/datapack/bookshelf-block)
  * [Bookshelf Environment](https://modrinth.com/datapack/bookshelf-environment)

* **All-in-One Bundle**:
  * [Bookshelf Suite Bundle](https://modrinth.com/datapack/bookshelf-suite)

### Resource Packs

* [Block Morph Resource Pack](https://modrinth.com/datapack/block-morph-datapack/version/0.3) (Included under "Supplementary resources")

## Usage

### Obtain Item

* **Crafting Recipe**:  
  Combine *1x Amethyst Shard*, *1x Echo Shard*, and *1x Chorus Fruit* (shaped).
* **Command**:

  ```mcfunction
  /function block-morph:give/selection_stick
  ```

### Transform

* Main Hand (Structure Mode):
Hold the selection stick in your main hand, look at a block, and use it (Right-Click) WITHOUT holding Srpint Key (`ctrl`) .

  * If valid, a connected block structure will be created and move to your position.

* Off Hand (Single-Block Force Mode):
Hold the selection stick in your off hand, look at a block, and use it (Right-Click) WITHOUT holding Srpint Key (`ctrl`) .

  * Forces a single-block structure to be created and move to your position, regardless of structure validity.

### Untransform

* Hold Srpint Key (`ctrl`) while using (Right-Clicking) the selection stick in either hand to restore your human form and place the blocks back.

### Align

* Sneak (`Shift`) while morphed to instantly snap your position to the block grid.

## Config

* Run command `/function block-morph:config/panel` to open the config panel.
* Run command `/function block-morph:config/debug` to open the debug panel for troubleshooting.

## Important Notes

* Collision: Transformed block structures are purely visual and have no collision.

* Visibility: Your armor and mainhand/offhand held items remain visible while morphed.

## Development

Check out the [Wiki](https://github.com/4tubborn/block-morph/wiki) for developer guides and tutorials.
