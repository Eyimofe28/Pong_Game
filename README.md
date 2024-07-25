# PONG Game

## Project Overview

This project is a Python implementation of the classic Pong game using the Turtle graphics library. The game involves two paddles and a ball, and players score points by getting the ball past the opponent's paddle. The game continues until one player reaches 7 points, at which point a winner is declared.

## Features

- **Paddle Movement**: Control paddles using keyboard keys (`Up` and `Down` arrows for the right paddle, `w` and `s` keys for the left paddle).
- **Ball Movement**: The ball moves and bounces off the walls and paddles.
- **Score Keeping**: The scoreboard keeps track of points scored by each player.
- **Game Over**: The game ends when one player reaches 7 points, displaying a winner and loser message.

## Dependencies

- Python 3.x
- Turtle graphics library (comes pre-installed with Python)

## File Descriptions

### `main.py`

The main file containing the game setup, main loop, and collision detection logic.

### `pong_paddle.py`

A module defining the `Paddle` class, which handles paddle creation and movement.

### `pong_ball.py`

A module defining the `Ball` class, which handles ball creation, movement, and collision detection.

### `pong_scoreboard.py`

A module defining the `ScoreBoard` class, which handles score display and updates.

## Getting Started

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Run the Project**: Execute the `main.py` file to start the game.
   ```bash
   python main.py
   ```

## Code Explanation

### Main Game Setup (`main.py`)

The main game file sets up the game environment, creates the paddles, ball, and scoreboard, and contains the main game loop.

### Paddle Class (`pong_paddle.py`)

The `Paddle` class handles the creation and movement of the paddles.


### Ball Class (`pong_ball.py`)

The `Ball` class handles the creation, movement, and collision detection of the ball.

### ScoreBoard Class (`pong_scoreboard.py`)

The `ScoreBoard` class handles the display and update of scores.


## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure your code follows the project’s coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This comprehensive readme should help you understand the structure and functionality of the Pong game application. If you have any questions or need any more help, please don't hesitate to ask.
