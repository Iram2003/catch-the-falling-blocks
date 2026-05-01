# OpenGL Catch the Blocks Game

A simple and fun 2D arcade game built using **Python OpenGL (GLUT)**.  
The player controls a basket to catch falling blocks while trying to avoid misses.

# Features
- 3 falling blocks at a time (maximum)
- Score system (catch blocks to earn points)
- Miss counter (game over after 3 misses)
- Smooth real-time animation using GLUT timer
- Keyboard controls (Arrow keys)
- Restart game using `R` key
- Transparent blocks using blending

# How to Play
- Use **LEFT ARROW (←)** to move basket left
- Use **RIGHT ARROW (→)** to move basket right
- Catch falling red blocks in the basket
- Each catch = +1 score
- Missing 3 blocks = Game Over
- Press **R** to restart the game

# Game Logic
- Blocks fall from the top of the screen
- If a block touches the basket → score increases
- If it misses → miss counter increases
- Game ends after 3 misses
- Blocks reset automatically after reaching bottom

# Technologies Used
- Python 
- PyOpenGL
- GLUT (OpenGL Utility Toolkit)
