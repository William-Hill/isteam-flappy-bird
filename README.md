# Flappy Bird Teaching Project

A complete Flappy Bird clone built with Pygame Zero, designed specifically for teaching programming concepts in a classroom setting. This project includes both a complete working version and a teaching shell version for guided instruction.

## 🎯 Project Overview

This Flappy Bird clone demonstrates key programming concepts including:
- Game loops and event handling
- Sprite animation and physics
- Collision detection
- Sound effects and user input
- Object-oriented programming concepts
- Game state management

## 📁 Project Structure

```
isteam-flappy-bird/
├── flappy_bird/
│   ├── main.py              # Main game file (teaching shell version)
│   ├── images/              # Game assets
│   │   ├── background.png   # Background image
│   │   ├── bird0.png        # Bird animation frame 1
│   │   ├── bird1.png        # Bird animation frame 2
│   │   ├── bird2.png        # Bird animation frame 3
│   │   ├── birddead.png     # Dead bird image
│   │   ├── bottom.png       # Bottom pipe image
│   │   ├── top.png          # Top pipe image
│   │   └── newyork.jpg      # Alternative background
│   └── sounds/              # Audio assets
│       ├── sfx_wing.wav     # Bird flap sound
│       ├── sfx_point.wav    # Score sound
│       ├── sfx_hit.wav      # Collision sound
│       ├── sfx_die.wav      # Game over sound
│       └── sfx_swooshing.wav # Pipe passage sound
└── README.md                # This file
```

## 🚀 Getting Started

### Prerequisites

1. **Python 3.7+** - Download from [python.org](https://python.org)
2. **Pygame Zero** - Install via pip:
   ```bash
   pip install pgzero
   ```
3. **pgzhelper** - Install via pip:
   ```bash
   pip install pgzhelper
   ```

### Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd isteam-flappy-bird
   ```
3. Run the game:
   ```bash
   pgzrun flappy_bird/main.py
   ```

## 🎮 How to Play

- **SPACE** - Make the bird flap upward
- **SPACE** (when game over) - Restart the game
- **Objective** - Navigate through pipes without hitting them
- **Scoring** - Earn points by successfully passing through pipe gaps

## 📚 Teaching Guide

### For Instructors

This project is designed for teaching programming concepts step-by-step. The `main.py` file contains a teaching shell with detailed TODO comments that guide students through implementation.

#### Recommended Teaching Sequence:

1. **Setup & Imports** (5 minutes)
   - Explain Pygame Zero framework
   - Add required import statements

2. **Game Constants** (5 minutes)
   - Review the predefined constants
   - Explain why we use constants

3. **Game State Variables** (10 minutes)
   - Create the bird actor
   - Initialize game variables
   - Explain object properties

4. **Core Functions** (30-45 minutes)
   - `create_pipe()` - Object creation and positioning
   - `reset_game()` - State management
   - `draw()` - Rendering and UI
   - `update()` - Game physics and logic
   - `on_key_down()` - Event handling
   - `update_pipes()` - Timing and spawning

5. **Testing & Debugging** (10-15 minutes)
   - Run the game
   - Identify and fix issues
   - Discuss common programming errors

#### Key Learning Objectives:

- **Variables & Data Types**: Understanding different variable types and their uses
- **Functions**: Creating and calling functions with parameters
- **Control Flow**: If statements, loops, and conditional logic
- **Object-Oriented Concepts**: Working with actors and their properties
- **Game Development**: Understanding game loops, physics, and user input
- **Debugging**: Identifying and fixing common programming errors

### For Students

The `main.py` file contains TODO comments that guide you through building the game:

1. **Follow the TODO comments** - Each section has step-by-step instructions
2. **Test frequently** - Run the game after completing each function
3. **Ask questions** - Don't hesitate to ask for clarification
4. **Experiment** - Try modifying values to see how they affect the game

## 🔧 Customization Ideas

Once students complete the basic game, encourage them to experiment with:

- **Visual Changes**: Modify colors, add new backgrounds, change bird appearance
- **Gameplay Mechanics**: Adjust gravity, pipe speed, gap size
- **New Features**: Add power-ups, different bird types, or scoring multipliers
- **Sound Effects**: Add new sounds or modify existing ones
- **UI Improvements**: Add menus, high score tracking, or difficulty settings

## 🐛 Troubleshooting

### Common Issues:

1. **"pgzrun not found"**
   - Ensure Pygame Zero is installed: `pip install pgzero`

2. **"pgzhelper not found"**
   - Install pgzhelper: `pip install pgzhelper`

3. **Images not loading**
   - Check that all image files are in the `images/` folder
   - Verify file names match exactly (case-sensitive)

4. **Sounds not playing**
   - Check that all sound files are in the `sounds/` folder
   - Verify file names match exactly (case-sensitive)

5. **Game runs but bird doesn't move**
   - Check that the `update()` function is properly implemented
   - Verify gravity and velocity variables are being updated

## 📖 Additional Resources

- [Pygame Zero Documentation](https://pygame-zero.readthedocs.io/)
- [pgzhelper Documentation](https://github.com/CarlGroth/pgzhelper)
- [Python Game Development Tutorials](https://realpython.com/python-game-development/)

## 🤝 Contributing

This is a teaching project, so contributions that improve the educational experience are welcome! Consider:

- Adding more detailed comments
- Creating additional teaching exercises
- Improving the documentation
- Adding alternative difficulty levels

## 📄 License

This project is designed for educational use. Feel free to use and modify for teaching purposes.

---

**Happy Coding! 🐦✨** 