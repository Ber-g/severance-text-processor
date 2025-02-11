# Fireworks Letter Game

## Overview

Fireworks Letter Game is an interactive Pygame application where users can collect letters that float around the screen and drop them into a trash can. The game features a dynamic and engaging interface with animations and collision detection.

## Features

- **Borderless Window**: The game runs in a borderless window for a seamless experience.
- **Random Letters**: Letters float around the screen with random velocities.
- **Collision Detection**: Letters change direction upon collision with each other.
- **Interactive Trash Can**: Users can drag letters into a trash can, which animates open and close.
- **Countdown and Reset**: The game displays a countdown and resets after all letters are collected or the "R" key is pressed.

## Requirements

- Python 3.x
- Pygame library
- Custom font file (`PixelifySans-Regular.ttf`)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/fireworks-letter-game.git
   cd fireworks-letter-game
   ```

2. **Install Pygame**:
   ```bash
   pip install pygame
   ```

3. **Download the Font**:
   Ensure the `PixelifySans-Regular.ttf` font file is in the same directory as the script.

## Usage

1. **Run the Game**:
   ```bash
   python fireworks_letter_game.py
   ```

2. **Game Controls**:
   - **Mouse**: Click and drag letters to move them.
   - **Trash Can**: Drag letters into the trash can to collect them.
   - **Reset**: Press the "R" key to reset the game.

## Gameplay

- **Collect Letters**: Drag letters into the trash can to collect them.
- **Countdown**: After all letters are collected or the "R" key is pressed, a countdown will start. The game will reset after the countdown.
- **Animations**: The trash can animates open and close when letters are dropped into it.

## Customization

- **Window Size**: Adjust the `width` and `height` variables to change the window size.
- **Number of Letters**: Modify the `generate_random_points` function call to change the initial number of letters.
- **Animation Speed**: Adjust the `clock.tick` value to change the animation speed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


## Future Features

I want it to be a word processor, next step will be to add a line by line return function writting into a txt file.


## License


## Acknowledgments

- Inspired by Severance MDR
- Inspired by various Pygame tutorials and examples.
- Custom font from [Pixelify Sans](https://www.dafont.com/pixelify-sans.font).


---

Enjoy playing the Fireworks Letter Game!
