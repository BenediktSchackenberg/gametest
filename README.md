# gametest

A small demo game using Pygame. It draws a pixel forest and some helicopters
that fly back and forth. A simple player character can now run through the
forest while dropping quips in the style of Christoph Gröner.

Optionally, you can add a sprite named `Pixel-Art Geschäftsmann im Anzug.png`
in the game directory. If present, it will be used as the player's image. The
file itself is not included in this repository. You can download a suitable
image from an external source (for example:
`https://example.com/pixel-art-businessman.png`) and place it next to
`main.py`.

## Requirements

- Python 3.11+
- Pygame

## Running the game

Install Pygame if it is not already installed:

```bash
pip install pygame
```

Then run the main file:

```bash
python3 main.py
```

Move the player left and right with the arrow keys. Listen for the occasional
Gröner-esque Spruch while you run.

Use the window's close button to exit the game.
