# Block Morph

Turn into any block in Minecraft! A datapack that lets you transform into customized block structures or individual blocks.

---

## Features

* **Become Any Block**: Seamlessly morph into block structures in the world.
* **Biome-Aware Plant Color**: Dynamic biome tinting for plants (grass, short grass, leaves, etc.).
* **Multiplayer Compatibility**: Have fun with your friends!

---

## Dependencies

To use this data pack, make sure you have installed the following required dependencies:

### Data Packs

* [Bookshelf View]()
* [Bookshelf Block]()
* [Bookshelf Environment]()

### Resource Packs

* [Block Morph Resource Pack]()

---

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
Hold the selection stick in your main hand, look at a block, and use it (Right-Click) WITHOUT holding `Ctrl`.

  * If valid, a connected block structure will be created and move to your position.

* Off Hand (Single-Block Force Mode):
Hold the selection stick in your off hand, look at a block, and use it (Right-Click) WITHOUT holding `Ctrl`.

  * Forces a single-block structure to be created and move to your position, regardless of structure validity.

### Untransform

* Hold `Ctrl` while using (Right-Clicking) the selection stick in either hand to restore your human form and place the blocks back.

### Align

* Sneak (`Shift`) while morphed to instantly snap your position to the block grid.

---

## Config

* Run command `/function block-morph:config/panel` to open the config panel.
* Run command `/function block-morph:config/debug` to open the debug panel for help if you encounter issues.

---

## Important Notes

* Collision: Transformed block structures are purely visual and have no collision.

* Equipment Visibility: Your armor and mainhand/offhand held items remain visible while morphed.

---

## Development

Check out the [Wiki](https://) for developer guides and tutorials.
