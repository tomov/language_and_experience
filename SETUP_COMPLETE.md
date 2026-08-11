# Setup Complete! ✓

## Repository Setup Status

✅ **Repository cloned and ready**
✅ **Conda environment created** (`language_and_experience`)
✅ **Core dependencies installed** (pygame, gym, scikit-learn, scipy, pandas, matplotlib, Pillow)
✅ **Python 3.10.20 in conda environment**
✅ **Games verified** (10 games available in `/games/` directory)
✅ **Human play mode created** (`play_human.py`)

## What's Working

### 1. Model/Agent Mode (Original Experiment)
The original experiment code for running EMPA (the model) is ready:

```bash
# Individual learning (experience only)
python run_experiment.py --game beesAndBirds --condition individual --n-lives 15

# Social learning with human descriptions
python run_experiment.py --game beesAndBirds --condition social --msg-source human --n-lives 15
```

**Note**: For LLM-based conditions, you need to set up the model path:
```bash
export MODELS_PATH=/path/to/your/models
```

### 2. Human Play Mode (NEW!) ✨
**You can now play the games yourself instead of the model!**

```bash
python play_human.py --game beesAndBirds
```

See `PLAY_AS_HUMAN.md` for full instructions.

## Quick Start - Play a Game Now!

**First, activate the conda environment**:
```bash
conda activate language_and_experience
```

Then try any of these:

```bash
# Bee collection game (real-time action)
python play_human.py --game beesAndBirds

# Shooting game
python play_human.py --game plaqueAttack

# Space invaders
python play_human.py --game aliens

# Puzzle game (turn-based)
python play_human.py --game pushBoulders --step-by-step
```

**Controls**: Arrow keys to move, Space for action, Q/ESC to quit

## What's Missing (Optional)

For the full model experiments (not needed for human play):

- ❌ **LLM models** - Required for social learning conditions with language
  - If you want to run the model with language descriptions, download LLM models
  - Set `MODELS_PATH` environment variable
  - See `docs/DATA_SETUP.md` for details

- ❌ **MPI** - Required for parallel inference (only for model experiments)
  ```bash
  conda install -c conda-forge mpi4py openmpi
  ```

- ⚠️ **Other dependencies** - Some advanced features may require:
  - torch, transformers (for LLM inference)
  - vllm (for LLM serving)
  - opencv-python (for video generation)

## Directory Structure

```
language_and_experience/
├── play_human.py           # NEW! Play games as human
├── PLAY_AS_HUMAN.md        # NEW! Human play instructions
├── run_experiment.py       # Run model experiments
├── requirements.txt        # Full dependency list
├── src/                    # Source code
│   ├── agent/             # Model agent implementation
│   ├── game/              # Game environment wrapper
│   └── vgdl/              # VGDL game engine
├── games/                  # 10 game definitions
│   ├── beesAndBirds_v0/
│   ├── plaqueAttack_v0/
│   ├── aliens_v0/
│   └── ...
└── data_input/            # Input data (descriptions, prompts)
```

## Next Steps

### To play games yourself:
1. Activate the environment: `conda activate language_and_experience`
2. Read `PLAY_AS_HUMAN.md`
3. Run `python play_human.py --game beesAndBirds`
4. Have fun! 🎮

### To run model experiments:
1. (Optional) Install remaining dependencies: `pip install -r requirements.txt`
2. (Optional) Set up LLM models if needed
3. Run experiments with `run_experiment.py`

## Known Issues

- ⚠️ Gym deprecation warning (safe to ignore - the code works with gym 0.26.2)
- ⚠️ NumPy 2.0 compatibility warning (safe to ignore - functionality still works)

## Help & Support

- For issues with the model experiments, see the original `README.md`
- For playing games as human, see `PLAY_AS_HUMAN.md`
- For game descriptions and objectives, check `data_input/descriptions/`

---

**Status**: ✅ Ready to play! The games are playable and the model code is functional.
