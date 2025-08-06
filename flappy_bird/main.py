# main.py
# Flappy Bird Clone using Pygame Zero + pgzhelper
# Run with: pgzrun main.py

# TODO: Import the required modules
# We need random for generating random numbers
# We need pgzhelper for sprite animation & rotation helpers

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
# TODO: Create the bird actor
# - Position it at (75, 350)
# - Set up the flapping animation frames: ["bird0", "bird1", "bird2"]
# - Set animation speed (fps) to 10
# - Initialize vertical velocity (vy) to 0

# TODO: Create a list to hold pipe pairs
# TODO: Initialize score to 0
# TODO: Set game_over to False

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
    
    TODO: Implement this function to:
    1. Generate a random gap position between 150 and 500
    2. Create a top pipe actor positioned above the gap
    3. Create a bottom pipe actor positioned below the gap
    4. Add both pipes to the pipes list as a tuple
    """
    pass

def reset_game():
    """
    Reset the game state to start a new round.
    
    TODO: Implement this function to:
    1. Reset bird position to (75, 350)
    2. Reset bird's vertical velocity to 0
    3. Reset bird's rotation angle to 0
    4. Clear the pipes list
    5. Reset score to 0
    6. Set game_over to False
    """
    pass

def draw():
    """
    Draw all game objects on the screen.
    
    TODO: Implement this function to:
    1. Draw the background image
    2. Draw all pipe pairs (top and bottom pipes)
    3. Draw the bird
    4. Display the current score
    5. If game is over, show "GAME OVER!" message and restart instructions
    """
    pass

def update():
    """
    Update game logic each frame (called automatically by Pygame Zero).
    
    TODO: Implement this function to:
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
    pass

def on_key_down(key):
    """
    Handle key presses for flap and restart.
    
    TODO: Implement this function to:
    1. Check if SPACE key was pressed
    2. If game is over and SPACE pressed, call reset_game()
    3. If game is running and SPACE pressed, make bird flap upward
    4. Play wing flap sound when flapping
    """
    pass

def update_pipes():
    """
    Spawn pipes periodically.
    
    TODO: Implement this function to:
    1. Check if game is not over
    2. Check if no pipes exist OR if the last pipe is far enough away
    3. If conditions are met, call create_pipe()
    """
    pass

# TODO: Schedule the pipe spawning function to run every SPAWN_INTERVAL seconds
# Use: clock.schedule_interval(update_pipes, SPAWN_INTERVAL)
