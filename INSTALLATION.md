# Installation Guide

Complete setup instructions for the Language and Experience repository.

## Prerequisites

- **Conda** (Miniconda or Anaconda)
- **Python 3.10+**
- **Display server** (X11) for playing games with GUI

## Quick Setup (Automated)

The easiest way to set up the environment:

```bash
./setup_env.sh
```

This script will:
1. Create a conda environment named `language_and_experience`
2. Install Python 3.10
3. Install all core dependencies needed to play games

## Manual Setup

If you prefer to set up manually or the script doesn't work:

### 1. Create Conda Environment

```bash
conda create -n language_and_experience python=3.10
conda activate language_and_experience
```

### 2. Install Core Dependencies (for Human Play)

```bash
pip install pygame gym==0.26.2 scikit-learn scipy matplotlib pandas Pillow numpy
```

### 3. Test the Installation

```bash
python play_human.py --help
```

You should see the help message with all available games.

## Playing Games

Once the environment is set up:

```bash
# Always activate the environment first
conda activate language_and_experience

# Play a game
python play_human.py --game beesAndBirds
```

See `PLAY_AS_HUMAN.md` for detailed instructions on playing games.

## Full Installation (for Model Experiments)

If you want to run the full EMPA model experiments (not just play games):

### 1. Install Additional Dependencies

```bash
conda activate language_and_experience
pip install -r requirements.txt
```

This includes:
- `torch`, `transformers` (for LLM inference)
- `vllm` (for LLM serving)
- `opencv-python` (for video generation)

### 2. Install MPI (for Parallel Processing)

```bash
conda install -c conda-forge mpi4py openmpi
```

### 3. Set up LLM Models

For language-based conditions, you need to download LLM models:

```bash
export MODELS_PATH=/path/to/your/models
```

See `docs/DATA_SETUP.md` for details on obtaining models.

### 4. Run Model Experiments

```bash
# Individual learning (experience only)
python run_experiment.py --game beesAndBirds --condition individual --n-lives 15

# Social learning with human descriptions
python run_experiment.py --game beesAndBirds --condition social --msg-source human --n-lives 15
```

## Environment Management

### Activate Environment
```bash
conda activate language_and_experience
```

### Deactivate Environment
```bash
conda deactivate
```

### Delete Environment (if needed)
```bash
conda env remove -n language_and_experience
```

### List All Conda Environments
```bash
conda env list
```

## Troubleshooting

### pygame window doesn't appear
Make sure you have a display server:
```bash
echo $DISPLAY  # Should show ":0" or ":1"
```

If on a remote server, you may need X11 forwarding:
```bash
ssh -X user@server
```

### Gym deprecation warnings
These warnings are expected and safe to ignore:
```
Gym has been unmaintained since 2022...
```
The code works fine with gym 0.26.2.

### NumPy 2.0 warnings
These warnings are expected and safe to ignore. The functionality still works.

### Import errors
Make sure you're in the repository root directory when running scripts:
```bash
cd /home/momchil.tomov/Documents/projects/DBP/language_and_experience
python play_human.py --game beesAndBirds
```

### Conda not found
Install Miniconda:
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

## Verification

To verify everything is working:

```bash
conda activate language_and_experience
python -c "
import sys
sys.path.insert(0, '.')
from src.utils import register_game
game_id = register_game('beesAndBirds', level=0, fast=False)
print('✅ Setup verified!')
"
```

## What's Installed

### Core Dependencies (Always)
- **pygame** - Game rendering
- **gym==0.26.2** - Game environment framework
- **numpy** - Numerical computing
- **scipy** - Scientific computing
- **scikit-learn** - Machine learning utilities
- **matplotlib** - Plotting
- **pandas** - Data manipulation
- **Pillow** - Image processing

### Additional Dependencies (Full Install Only)
- **torch** - Deep learning framework
- **transformers** - LLM library
- **vllm** - LLM inference server
- **mpi4py** - Parallel processing
- **opencv-python** - Video generation

## Next Steps

After installation:

1. **Play games**: See `PLAY_AS_HUMAN.md`
2. **Game descriptions**: See `GAME_DESCRIPTIONS.md`
3. **Run experiments**: See `README.md`
4. **Setup status**: See `SETUP_COMPLETE.md`
