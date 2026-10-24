# Tic-Tac-Toe

A two-player command-line Tic-Tac-Toe game written in Python. Players take turns placing **X** and **O** on a 3×3 board until someone wins or the board is full.

In-game prompts are in Hebrew.

## Requirements

- Python 3

No extra packages are needed.

## How to run

From the project folder:

```bash
python tictac.py
```

On some systems you may need `python3` instead of `python`.

## How to play

1. The board is printed after every turn.
2. When it is your turn, enter a **row** (`0`–`2`), then a **column** (`0`–`2`).
3. You cannot place a mark on a cell that is already taken.
4. A player wins by filling a full row, column, or diagonal.
5. If every cell is filled and nobody has three in a row, the game is a draw.

Example board:

```
  |   |
---------
  |   |
---------
  |   |
```

## Project files

- `tictac.py` — game loop, board display, win and draw checks
