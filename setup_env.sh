#!/bin/bash
# Setup script for Language and Experience repository
# Creates conda environment and installs dependencies

set -e  # Exit on error

echo "========================================"
echo "Language and Experience - Environment Setup"
echo "========================================"
echo ""

# Check if conda is available
if ! command -v conda &> /dev/null; then
    echo "❌ Error: conda not found. Please install Miniconda or Anaconda first."
    exit 1
fi

# Create conda environment
echo "📦 Creating conda environment 'language_and_experience' with Python 3.10..."
conda create -n language_and_experience python=3.10 -y

# Activate environment
echo ""
echo "🔄 Activating environment..."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate language_and_experience

# Install core dependencies for human play
echo ""
echo "📥 Installing core dependencies (for human play)..."
pip install --index-url https://pypi.org/simple \
    pygame \
    gym==0.26.2 \
    scikit-learn \
    scipy \
    matplotlib \
    pandas \
    Pillow \
    numpy

echo ""
echo "✅ Core setup complete!"
echo ""
echo "To play games as a human:"
echo "  1. conda activate language_and_experience"
echo "  2. python play_human.py --game beesAndBirds"
echo ""
echo "========================================"
echo ""
echo "Optional: Install full dependencies for model experiments"
echo "  conda activate language_and_experience"
echo "  pip install -r requirements.txt"
echo "  conda install -c conda-forge mpi4py openmpi"
echo ""
echo "See SETUP_COMPLETE.md for more information."
echo "========================================"
