# Quick Start Guide

Get playing games in 2 minutes!

## ✅ Setup Already Complete

The conda environment `language_and_experience` has been created with all necessary dependencies.

## 🎮 Play Now!

### Step 1: Activate Environment
```bash
conda activate language_and_experience
```

### Step 2: Choose a Game
```bash
# Bee collection game (good starter)
python play_human.py --game beesAndBirds

# Space shooter
python play_human.py --game aliens

# Tower defense shooter
python play_human.py --game plaqueAttack

# Sokoban puzzle (turn-based)
python play_human.py --game pushBoulders --step-by-step
```

### Step 3: Play!
- **Arrow keys**: Move/Aim
- **Space**: Shoot/Action
- **Q or ESC**: Quit

## 📚 More Information

- **All games & descriptions**: `GAME_DESCRIPTIONS.md`
- **Full play guide**: `PLAY_AS_HUMAN.md`
- **Installation details**: `INSTALLATION.md`
- **Setup status**: `SETUP_COMPLETE.md`

## 🎯 Game Recommendations

**First-time players**:
- `beesAndBirds` - Learn the basic mechanics
- `aliens` - Classic space shooter

**Puzzle fans**:
- `pushBoulders` - Sokoban-style (use `--step-by-step`)
- `portals` - Teleportation mechanics

**Action fans**:
- `plaqueAttack` - Tower defense
- `missile_command` - Defend cities
- `jaws` - Survival

## 🔧 Troubleshooting

**Game doesn't start?**
- Make sure you activated the environment: `conda activate language_and_experience`
- Check you're in the repo directory: `cd /path/to/language_and_experience`

**No display?**
- Check: `echo $DISPLAY` (should show ":0" or similar)
- If remote: use `ssh -X` for X11 forwarding

**See warnings?**
- Gym/NumPy warnings are normal and safe to ignore

## 🚀 Advanced

### Change game speed
```bash
python play_human.py --game beesAndBirds --fps 30  # Faster
python play_human.py --game beesAndBirds --fps 10  # Slower
```

### Try different levels
```bash
python play_human.py --game beesAndBirds --level 1
python play_human.py --game beesAndBirds --level 2
```

### Save your gameplay
```bash
python play_human.py --game beesAndBirds --save my_game.pkl
```

---

**Have fun playing! 🎮**

For running the original EMPA model experiments, see the main `README.md`.
