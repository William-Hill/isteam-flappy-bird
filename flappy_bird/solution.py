# solution.py
# Flappy Bird Clone - COMPLETE SOLUTION
# This file contains the full working implementation
# Use this as a reference for checking student work or providing hints

import random
from pgzhelper import *  # Provides sprite animation & rotation helpers

# -----------------------------
# Game Settings (CONSTANTS - Don't change these!)
# -----------------------------
WIDTH = 400
HEIGHT = 708

GRAVITY = 0.3
GAP = 150           # Gap between top and bottom pipes
PIPE_SPEED = 2
SPAWN_INTERVAL = 1.5 # Seconds between pipe spawns

# -----------------------------
# Game State Variables
# -----------------------------
# SOLUTION: Create the bird actor
bird = Actor("bird0", (75, 350))
bird.images = ["bird0", "bird1", "bird2"]  # Flapping animation frames
bird.fps = 10
bird.vy = 0

# SOLUTION: Create a list to hold pipe pairs
pipes = []      # Holds tuples of (top_pipe, bottom_pipe)
# SOLUTION: Initialize score to 0
score = 0
# SOLUTION: Set game_over to False
game_over = False

# -----------------------------
# Sound Effects (CONSTANTS - Don't change these!)
# -----------------------------
# Pygame Zero automatically loads sounds from the sounds folder
flap_sound = "sfx_wing"      # Bird wing flap sound
score_sound = "sfx_point"    # Point/score sound
hit_sound = "sfx_hit"        # Hit collision sound
die_sound = "sfx_die"        # Game over sound

# -----------------------------
# Functions
# -----------------------------

def create_pipe():
    """
    Create a new pair of pipes with a random gap position.
    
    SOLUTION: Implement this function to:
    1. Generate a random gap position between 150 and 500
    2. Create a top pipe actor positioned above the gap
    3. Create a bottom pipe actor positioned below the gap
    4. Add both pipes to the pipes list as a tuple
    """
    # SOLUTION: Generate a random gap position between 150 and 500
    gap_y = random.randint(150, 500)
    
    # SOLUTION: Create a top pipe actor positioned above the gap
    # Adjust for pipe image height (~640px) - position it above the gap
    top_pipe = Actor("top", (WIDTH + 50, gap_y - GAP // 2 - 320))
    
    # SOLUTION: Create a bottom pipe actor positioned below the gap
    # Position it below the gap
    bottom_pipe = Actor("bottom", (WIDTH + 50, gap_y + GAP // 2 + 320))
    
    # SOLUTION: Add both pipes to the pipes list as a tuple
    pipes.append((top_pipe, bottom_pipe))

def reset_game():
    """
    Reset the game state to start a new round.
    
    SOLUTION: Implement this function to:
    1. Reset bird position to (75, 350)
    2. Reset bird's vertical velocity to 0
    3. Reset bird's rotation angle to 0
    4. Clear the pipes list
    5. Reset score to 0
    6. Set game_over to False
    """
    global pipes, score, game_over
    
    # SOLUTION: Reset bird position to (75, 350)
    bird.y = 350
    
    # SOLUTION: Reset bird's vertical velocity to 0
    bird.vy = 0
    
    # SOLUTION: Reset bird's rotation angle to 0
    bird.angle = 0
    
    # SOLUTION: Clear the pipes list
    pipes = []
    
    # SOLUTION: Reset score to 0
    score = 0
    
    # SOLUTION: Set game_over to False
    game_over = False

def draw():
    """
    Draw all game objects on the screen.
    
    SOLUTION: Implement this function to:
    1. Draw the background image
    2. Draw all pipe pairs (top and bottom pipes)
    3. Draw the bird
    4. Display the current score
    5. If game is over, show "GAME OVER!" message and restart instructions
    """
    # SOLUTION: Draw the background image
    screen.blit("background", (0, 0))

    # SOLUTION: Draw all pipe pairs (top and bottom pipes)
    for top, bottom in pipes:
        top.draw()
        bottom.draw()

    # SOLUTION: Draw the bird
    bird.draw()

    # SOLUTION: Display the current score
    screen.draw.text(f"Score: {score}", midtop=(WIDTH//2, 10), fontsize=40, color="white")

    # SOLUTION: If game is over, show "GAME OVER!" message and restart instructions
    if game_over:
        screen.draw.text("GAME OVER!", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="red")
        screen.draw.text("Press SPACE to restart", center=(WIDTH//2, HEIGHT//2 + 60), fontsize=30, color="yellow")

def update():
    """
    Update game logic each frame (called automatically by Pygame Zero).
    
    SOLUTION: Implement this function to:
    1. If game is over, return early (don't update anything)
    2. Apply gravity to bird (increase vy by GRAVITY)
    3. Update bird position (add vy to y)
    4. Animate bird flapping (next_image())
    5. Rotate bird based on velocity (tilt up when flapping, down when falling)
    6. Move all pipes to the left by PIPE_SPEED
    7. Remove pipes that have moved off screen
    8. Increment score when bird passes a pipe
    9. Play sound effects for scoring
    10. Check for collisions with pipes or screen boundaries
    11. If collision detected, play hit/die sounds and set game_over to True
    """
    global game_over, score

    # SOLUTION: If game is over, return early (don't update anything)
    if game_over:
        return

    # SOLUTION: Apply gravity to bird (increase vy by GRAVITY)
    bird.vy += GRAVITY
    
    # SOLUTION: Update bird position (add vy to y)
    bird.y += bird.vy
    
    # SOLUTION: Animate bird flapping (next_image())
    bird.next_image()
    
    # SOLUTION: Rotate bird based on velocity (tilt up when flapping, down when falling)
    bird.angle = max(-30, min(60, -bird.vy * 5))

    # SOLUTION: Move all pipes to the left by PIPE_SPEED
    for top, bottom in pipes:
        top.x -= PIPE_SPEED
        bottom.x -= PIPE_SPEED

    # SOLUTION: Remove pipes that have moved off screen and increment score when bird passes a pipe
    if pipes and pipes[0][0].right < 0:
        pipes.pop(0)
        score += 1
        # SOLUTION: Play sound effects for scoring
        sounds.sfx_point.play()
        sounds.sfx_swooshing.play()

    # SOLUTION: Check for collisions with pipes or screen boundaries
    for top, bottom in pipes:
        if bird.colliderect(top) or bird.colliderect(bottom) or bird.top < 0 or bird.bottom > HEIGHT:
            # SOLUTION: If collision detected, play hit/die sounds and set game_over to True
            sounds.sfx_hit.play()
            sounds.sfx_die.play()
            game_over = True
            break

def on_key_down(key):
    """
    Handle key presses for flap and restart.
    
    SOLUTION: Implement this function to:
    1. Check if SPACE key was pressed
    2. If game is over and SPACE pressed, call reset_game()
    3. If game is running and SPACE pressed, make bird flap upward
    4. Play wing flap sound when flapping
    """
    global game_over
    
    # SOLUTION: Check if SPACE key was pressed
    if key == keys.SPACE:
        # SOLUTION: If game is over and SPACE pressed, call reset_game()
        if game_over:
            reset_game()
        else:
            # SOLUTION: If game is running and SPACE pressed, make bird flap upward
            bird.vy = -6
            # SOLUTION: Play wing flap sound when flapping
            sounds.sfx_wing.play()

def update_pipes():
    """
    Spawn pipes periodically.
    
    SOLUTION: Implement this function to:
    1. Check if game is not over
    2. Check if no pipes exist OR if the last pipe is far enough away
    3. If conditions are met, call create_pipe()
    """
    # SOLUTION: Check if game is not over
    if not game_over:
        # SOLUTION: Check if no pipes exist OR if the last pipe is far enough away
        if not pipes or pipes[-1][0].x < WIDTH - 200:
            # SOLUTION: If conditions are met, call create_pipe()
            create_pipe()

# SOLUTION: Schedule the pipe spawning function to run every SPAWN_INTERVAL seconds
clock.schedule_interval(update_pipes, SPAWN_INTERVAL) 