# Game Descriptions

This document describes the objectives and mechanics of each available game.

## Available Games

### 1. beesAndBirds
**Type**: Real-time action  
**Command**: `python play_human.py --game beesAndBirds`

**Objective**: Collect the GREEN box while managing light green boxes that help you.

**Mechanics**:
- Light green boxes "eat" orange boxes (which harm you)
- Light green boxes also "eat" yellow boxes (which also harm you)
- You need to set the light green boxes free to help you
- **Goal**: Collect the GREEN box to win

**Controls**: Arrow keys to move

---

### 2. plaqueAttack
**Type**: Real-time shooting  
**Command**: `python play_human.py --game plaqueAttack`

**Objective**: Defend YELLOW tiles from ORANGE and BROWN attackers (Space Invaders style).

**Mechanics**:
- Protect YELLOW tiles by shooting ORANGE and BROWN tiles
- Attacks come from top and bottom through holes
- Fixed number of enemies - shoot them all to win
- You can shoot sideways too
- Game ends when all YELLOW tiles turn GREEN (loss)

**Controls**: 
- Arrow keys to aim
- Spacebar to shoot

---

### 3. aliens
**Type**: Real-time shooting  
**Command**: `python play_human.py --game aliens`

**Objective**: Classic Asteroids-style game.

**Mechanics**:
- Move the blue square left and right
- Shoot pink squares
- Avoid red squares that come down from enemies

**Controls**:
- Left/Right arrow keys to move
- Spacebar to shoot

---

### 4. avoidGeorge
**Type**: Real-time avoidance  
**Command**: `python play_human.py --game avoidGeorge`

**Objective**: Avoid enemies while navigating the level.

**Mechanics**: Navigate through the level while avoiding dangerous entities.

**Controls**: Arrow keys to move

---

### 5. preconditions
**Type**: Turn-based resource management  
**Command**: `python play_human.py --game preconditions --step-by-step`

**Objective**: Manage resources and satisfy preconditions to progress.

**Mechanics**: Turn-based puzzle where you need to collect or use items in the right order.

**Controls**: Arrow keys to move (turn-based)

---

### 6. portals
**Type**: Real-time puzzle  
**Command**: `python play_human.py --game portals`

**Objective**: Use teleportation portals to navigate the level.

**Mechanics**: Enter portals to teleport to different locations and reach your goal.

**Controls**: Arrow keys to move

---

### 7. pushBoulders
**Type**: Turn-based puzzle (Sokoban-style)  
**Command**: `python play_human.py --game pushBoulders --step-by-step`

**Objective**: Push boulders onto target locations.

**Mechanics**:
- Classic Sokoban mechanics
- Push (not pull) boulders
- Get all boulders to their target positions

**Controls**: Arrow keys to move and push (turn-based)

---

### 8. relational
**Type**: Turn-based puzzle  
**Command**: `python play_human.py --game relational --step-by-step`

**Objective**: Solve puzzles involving object relationships.

**Mechanics**: Navigate and interact with objects that have special relationships with each other.

**Controls**: Arrow keys to move (turn-based)

---

### 9. missile_command
**Type**: Real-time defense  
**Command**: `python play_human.py --game missile_command`

**Objective**: Defend cities from incoming missiles.

**Mechanics**:
- Classic Missile Command style gameplay
- Shoot down missiles before they hit targets

**Controls**: 
- Arrow keys to aim
- Spacebar to shoot

---

### 10. jaws
**Type**: Real-time survival  
**Command**: `python play_human.py --game jaws`

**Objective**: Survive shark attacks.

**Mechanics**: Avoid or fight off dangerous sharks while accomplishing your objective.

**Controls**: Arrow keys to move, Space to use action

---

## Game Types Summary

### Real-time Games
These games continue running and you need to react quickly:
- **beesAndBirds** - Collection with helpers
- **plaqueAttack** - Tower defense shooter
- **aliens** - Space shooter
- **avoidGeorge** - Avoidance
- **portals** - Portal navigation
- **missile_command** - Defense
- **jaws** - Survival

### Turn-based Games
These games wait for your input before advancing:
- **preconditions** - Resource management
- **pushBoulders** - Sokoban puzzle
- **relational** - Object relationship puzzle

Use `--step-by-step` flag for turn-based games.

---

## Tips

1. **Start with beesAndBirds or aliens** - Good introductory games
2. **Use lower FPS for easier games**: `--fps 10`
3. **Use higher FPS for challenges**: `--fps 30`
4. **Turn-based games** need the `--step-by-step` flag
5. **Save trajectories** with `--save filename.pkl` to analyze your gameplay
6. **Try different levels** with `--level 1`, `--level 2`, etc.

---

## Controls Summary

**All Games**:
- **Arrow Keys**: Move/Aim (UP, DOWN, LEFT, RIGHT)
- **Space**: Shoot/Use/Action
- **Q or ESC**: Quit

**Display**: The game window will show colored squares representing different game entities. Learn the meaning through playing or check the human descriptions in `data_input/descriptions/human_no_feedback/`.
