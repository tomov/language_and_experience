# DBP Setup - Language and Experience

This repository has been set up for the DBP project with human-playable game modes and comprehensive documentation.

## 🚀 Quick Links

### Getting Started
- **[QUICKSTART.md](QUICKSTART.md)** ← **START HERE!** Get playing in 2 minutes
- **[INSTALLATION.md](INSTALLATION.md)** - Detailed setup instructions and troubleshooting

### Playing Games
- **[PLAY_AS_HUMAN.md](PLAY_AS_HUMAN.md)** - Complete guide to playing games yourself
- **[GAME_DESCRIPTIONS.md](GAME_DESCRIPTIONS.md)** - Objectives and mechanics for all 10 games

### Reference
- **[SETUP_COMPLETE.md](SETUP_COMPLETE.md)** - Setup status and what's been configured
- **[README.md](README.md)** - Original repository documentation (model experiments)

## 📋 What's New

### Human Play Mode ✨
You can now play the games yourself instead of having the model play them!

**Quick Start:**
```bash
conda activate language_and_experience
python play_human.py --game beesAndBirds
```

### Conda Environment
A dedicated conda environment `language_and_experience` has been created with all dependencies:
- pygame, gym, scikit-learn, scipy, matplotlib, pandas, Pillow, numpy

### Automated Setup
Run the setup script to recreate the environment:
```bash
./setup_env.sh
```

## 🎮 Available Games

All 10 games from the paper are playable:

1. **beesAndBirds** - Collection with helper creatures
2. **plaqueAttack** - Tower defense shooter
3. **aliens** - Space shooter (Asteroids-style)
4. **avoidGeorge** - Enemy avoidance
5. **preconditions** - Resource management puzzle
6. **portals** - Teleportation puzzle
7. **pushBoulders** - Sokoban puzzle
8. **relational** - Object relationship puzzle
9. **missile_command** - City defense
10. **jaws** - Shark survival

See [GAME_DESCRIPTIONS.md](GAME_DESCRIPTIONS.md) for detailed information on each game.

## 🎯 Game Controls

- **Arrow Keys**: Move/Aim (UP, DOWN, LEFT, RIGHT)
- **Space**: Shoot/Use/Action
- **Q or ESC**: Quit game

## 📁 Repository Structure

```
language_and_experience/
├── DBP_README.md           # ← You are here
├── QUICKSTART.md           # Quick start guide
├── INSTALLATION.md         # Setup instructions
├── PLAY_AS_HUMAN.md        # Playing guide
├── GAME_DESCRIPTIONS.md    # Game details
├── SETUP_COMPLETE.md       # Setup status
│
├── play_human.py           # Human play script
├── setup_env.sh            # Environment setup script
├── run_experiment.py       # Model experiment script
├── README.md               # Original documentation
│
├── src/                    # Source code
│   ├── agent/              # Model agent
│   ├── game/               # Game wrapper
│   └── vgdl/               # Game engine
│
├── games/                  # 10 game definitions
│   ├── beesAndBirds_v0/
│   ├── aliens_v0/
│   └── ...
│
└── data_input/             # Descriptions & prompts
    └── descriptions/
        ├── human_no_feedback/
        └── machine_no_feedback/
```

## 🔧 Setup Overview

### Environment Status
✅ Conda environment created: `language_and_experience`  
✅ Python 3.10.20 installed  
✅ Core dependencies installed  
✅ Games verified and working  
✅ Human play mode functional  

### Git Status
- **Fork**: git@github.com:tomov/language_and_experience.git
- **Branch**: `dbp`
- **Status**: All changes committed and pushed

## 📖 Documentation Guide

### If you want to...

**Play games immediately**
→ [QUICKSTART.md](QUICKSTART.md)

**Understand the setup process**
→ [INSTALLATION.md](INSTALLATION.md)

**Learn how to play games**
→ [PLAY_AS_HUMAN.md](PLAY_AS_HUMAN.md)

**Know what each game does**
→ [GAME_DESCRIPTIONS.md](GAME_DESCRIPTIONS.md)

**See setup status**
→ [SETUP_COMPLETE.md](SETUP_COMPLETE.md)

**Run model experiments**
→ [README.md](README.md)

**Troubleshoot issues**
→ [INSTALLATION.md](INSTALLATION.md#troubleshooting)

## 💡 Examples

### Play Different Games
```bash
conda activate language_and_experience

# Action games
python play_human.py --game beesAndBirds
python play_human.py --game aliens
python play_human.py --game plaqueAttack

# Puzzle games (turn-based)
python play_human.py --game pushBoulders --step-by-step
python play_human.py --game preconditions --step-by-step
```

### Adjust Game Speed
```bash
# Slower (easier)
python play_human.py --game beesAndBirds --fps 10

# Faster (harder)
python play_human.py --game beesAndBirds --fps 30
```

### Try Different Levels
```bash
python play_human.py --game beesAndBirds --level 0
python play_human.py --game beesAndBirds --level 1
python play_human.py --game beesAndBirds --level 2
```

### Save Your Gameplay
```bash
python play_human.py --game beesAndBirds --save my_trajectory.pkl
```

## 🔬 Original Research

This repository contains code for the paper:

**"Language and Experience: A Computational Model of Social Learning in Complex Tasks"**  
*Cédric Colas, Tracey Mills, Ben Prytawski, Michael Henry Tessler, Noah Goodman, Jacob Andreas, Joshua Tenenbaum*

- **Paper**: [arXiv:2509.00074](https://arxiv.org/abs/2509.00074)
- **Demo**: [cedriccolas.com/demos/language_and_experience/](https://cedriccolas.com/demos/language_and_experience/)
- **Published**: CogSci 2025 and ICLR 2026

The original model experiments can still be run - see [README.md](README.md) for details.

## 🆘 Help

### Quick Troubleshooting

**Environment not found?**
```bash
conda env list  # Check if language_and_experience exists
./setup_env.sh  # Recreate if needed
```

**Game won't start?**
```bash
conda activate language_and_experience  # Activate first
echo $DISPLAY  # Check display is available
```

**Import errors?**
```bash
# Make sure you're in the repo root
cd /home/momchil.tomov/Documents/projects/DBP/language_and_experience
conda activate language_and_experience
```

For more help, see [INSTALLATION.md](INSTALLATION.md#troubleshooting).

## 📝 Notes

- The conda environment is isolated and won't affect your system Python
- Gym deprecation warnings are expected and safe to ignore
- All games are VGDL-based (Video Game Description Language)
- Turn-based games need the `--step-by-step` flag
- Real-time games run continuously at specified FPS

---

**Ready to play?** → Start with [QUICKSTART.md](QUICKSTART.md)

**Need setup help?** → See [INSTALLATION.md](INSTALLATION.md)

**Want game details?** → Check [GAME_DESCRIPTIONS.md](GAME_DESCRIPTIONS.md)
