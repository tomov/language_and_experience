# Playing the Games as a Human

This guide shows you how to play the games yourself instead of having the model/agent play them.

## Quick Start

**First, activate the conda environment**:
```bash
conda activate language_and_experience
```

Then play any game using the `play_human.py` script:

```bash
python play_human.py --game beesAndBirds
```

## Available Games

- `avoidGeorge` - Avoid enemies
- `beesAndBirds` - Collect items, avoid hazards
- `preconditions` - Resource management (turn-based)
- `portals` - Teleportation mechanics
- `pushBoulders` - Sokoban-style puzzle (turn-based)
- `relational` - Object relationships (turn-based)
- `plaqueAttack` - Shooting game
- `aliens` - Space invaders variant
- `missile_command` - Defend cities
- `jaws` - Survive shark attacks

## Controls

- **Arrow Keys**: Move in the corresponding direction (UP, DOWN, LEFT, RIGHT)
- **Space**: Use/Action key (for shooting in games like plaqueAttack)
- **Q or ESC**: Quit the game

## Options

### Play a specific level
```bash
python play_human.py --game beesAndBirds --level 1
```

### Change game speed
```bash
python play_human.py --game plaqueAttack --fps 30
```
Default is 20 FPS.

### Step-by-step mode (turn-based)
For turn-based games like puzzles:
```bash
python play_human.py --game pushBoulders --step-by-step
```

### Save your gameplay
To save your trajectory for analysis:
```bash
python play_human.py --game beesAndBirds --save my_trajectory.pkl
```

## Examples

### Play the bee game (real-time):
```bash
python play_human.py --game beesAndBirds
```

### Play a puzzle (turn-based):
```bash
python play_human.py --game pushBoulders --step-by-step
```

### Play a shooting game:
```bash
python play_human.py --game plaqueAttack
```

### Play space invaders:
```bash
python play_human.py --game aliens
```

## Notes

- **Real-time games** (beesAndBirds, plaqueAttack, aliens, etc.): The game continues running and you need to react in real-time
- **Turn-based games** (pushBoulders, preconditions, relational): The game waits for your input before advancing
- Some games have multiple levels (use `--level 0`, `--level 1`, etc.)
- If the game window doesn't appear, make sure you have a display available (X server running)

## Troubleshooting

If you get an error about missing dependencies, install them:
```bash
pip install pygame gym==0.26.2 scikit-learn scipy matplotlib pandas Pillow
```

If pygame doesn't display a window, make sure you have a display:
```bash
echo $DISPLAY  # Should show something like ":0" or ":1"
```
