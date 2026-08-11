#!/usr/bin/env python3
"""
Play games as a human player instead of having the model/agent play.

Usage:
    python play_human.py --game beesAndBirds
    python play_human.py --game plaqueAttack --level 0

Controls:
    Arrow keys: Move (UP, DOWN, LEFT, RIGHT)
    Space: Use/Action
    Q or ESC: Quit

Available games:
    - avoidGeorge
    - beesAndBirds
    - preconditions
    - portals
    - pushBoulders
    - relational
    - plaqueAttack
    - aliens
    - missile_command
    - jaws
"""

import argparse
import os
import sys

# Add repository to path
repo_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, repo_path)

from src.game.play_game import play_game
from src.utils import register_game

AVAILABLE_GAMES = [
    "avoidGeorge",
    "beesAndBirds",
    "preconditions",
    "portals",
    "pushBoulders",
    "relational",
    "plaqueAttack",
    "aliens",
    "missile_command",
    "jaws",
]


def main():
    parser = argparse.ArgumentParser(
        description="Play games as a human player",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        "--game",
        type=str,
        required=True,
        choices=AVAILABLE_GAMES,
        help="Game to play"
    )

    parser.add_argument(
        "--level",
        type=int,
        default=0,
        help="Game level (default: 0)"
    )

    parser.add_argument(
        "--fps",
        type=int,
        default=20,
        help="Frames per second (default: 20)"
    )

    parser.add_argument(
        "--step-by-step",
        action="store_true",
        default=False,
        help="Step-by-step mode (wait for key press for each action)"
    )

    parser.add_argument(
        "--save",
        type=str,
        default=None,
        help="Path to save trajectory (optional)"
    )

    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"Starting game: {args.game}")
    print(f"Level: {args.level}")
    print(f"\nControls:")
    print(f"  Arrow keys: Move")
    print(f"  Space: Use/Action")
    print(f"  Q or ESC: Quit")
    print(f"{'='*60}\n")

    # Register the game
    game_id = register_game(args.game, level=args.level, fast=False)

    # Play the game
    play_game(
        game_id=game_id,
        lvl=args.level,
        step_by_step=args.step_by_step,
        fps=args.fps,
        save_to=args.save,
        verbose=True,
        with_img=True
    )

    print("\nGame ended. Thanks for playing!")


if __name__ == "__main__":
    main()
