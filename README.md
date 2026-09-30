# Rock, Paper, Scissors — Command-Line Game

## Overview of the Project:

The **Rock, Paper, Scissors** game is a lightweight, interactive command-line game developed in Python. It allows a player to compete against an AI opponent by selecting Rock, Paper, or Scissors. The player chooses a target score, and the match continues until either the player or the AI reaches the required number of points.

The application provides a simple terminal-based interface with score tracking, random AI choices, round-by-round results, input validation, and match replay functionality. The game uses Python's built-in `random` and `sys` modules and requires no external dependencies.

## Features:

### Target Score Selection:

Allows the player to enter the number of points required to win the match. The program accepts only positive integer values and provides appropriate error messages for invalid input. The player can also enter `q` to exit before starting the match.

### Player vs AI Gameplay:

The player competes against an AI opponent. The AI randomly selects Rock, Paper, or Scissors for every round using Python's random selection functionality.

### Rock, Paper, Scissors Rules:

The program follows the standard game rules:

* Rock defeats Scissors
* Paper defeats Rock
* Scissors defeats Paper
* Matching choices result in a tie

### Score Tracking:

The game maintains separate scores for the player and AI. A point is awarded to the winner of each non-tied round, and the match continues until one side reaches the selected target score.

### Input Validation & Error Handling:

The application checks player commands and accepts only `1`, `2`, `3`, or `Q` during gameplay. Invalid selections are rejected without affecting the score. Target-point input is also validated using integer conversion and exception handling.

### Replay Support:

After a match finishes, the program asks whether the player wants to play another match. Entering `y` or `yes` starts a new game, while other responses end the application.

## Technical Specifications:

**Language:** Python 3

**Primary Functions:** `get_target_points()`, `play_rock_paper_scissors()`

**Python Modules:** `random`, `sys`

**Data Structures:** Dictionaries and tuples

**Core Concepts:** Functions, loops, conditional statements, dictionary mapping, random selection, exception handling, user input, score tracking, and formatted output.

**Game Choices:** Rock, Paper, Scissor

**Execution Mode:** Interactive Command-Line Interface

## How It Works:

### Target Point Input:

The program first calls `get_target_points()` and repeatedly asks the player to enter a positive integer representing the score required to win. Invalid values are rejected, while `q` exits the program.

### Game Initialization:

The player and AI scores are initialized to zero. A dictionary maps the numeric commands `1`, `2`, and `3` to Rock, Paper, and Scissor respectively.

### Player and AI Selection:

During every round, the player enters a choice. The AI then randomly selects one of the three available choices. The selected choices are displayed before determining the winner.

### Winner Determination:

The program compares the player's choice with the AI's choice using conditional statements. If both choices are the same, the round is a tie. Otherwise, the program applies the standard Rock-Paper-Scissors winning combinations and increases the appropriate score.

### Match Completion:

The match continues until either the player's score or the AI's score reaches the target points. The program then displays the match winner and the final score.

## Execution Guide:

### Run the Python Program:

```bash
python "Barani (1)(1).py"
```

or:

```bash
python3 "Barani (1)(1).py"
```

### Start the Game:

After launching the program, enter the target number of points required to win.

Example:

```text
Enter target points to win: 5
```

The game then displays:

```text
--- Match Started! First to 5 wins! ---
```

### Play a Round:

Choose one of the available options:

```text
Choose: [1] Rock   [2] Paper   [3] Scissors   [Q] Quit
Your choice: 1
```

The program displays both the player's and AI's choices and announces the round result.

### Quit During a Match:

Enter:

```text
q
```

or:

```text
quit
```

to abandon the current match.

## Known Edge Cases & Quick Handling:

### Invalid Target Score:

If the user enters a non-numeric value or a number less than or equal to zero, the program displays an error message and requests another value.

For example:

```text
Please enter a positive integer greater than 0.
```

### Invalid Game Selection:

If the user enters a value other than `1`, `2`, `3`, or `Q`, the program displays:

```text
Invalid selection! Please enter 1, 2, 3, or Q.
```

The invalid input does not affect the current score.

### Match Exit:

The player can leave the game before reaching the target score by entering `q` or `quit`. The program then returns from the current match.

## Conclusion:

The **Rock, Paper, Scissors** command-line game provides a simple and interactive implementation of a classic game using Python. Through this project, fundamental programming concepts such as functions, loops, conditional logic, dictionaries, random number selection, exception handling, user input, and score management are applied in a practical way.

The combination of player input and randomly generated AI choices creates an interactive gameplay experience, while target-based scoring allows matches to continue until a clear winner is determined. The replay functionality also allows users to start additional matches without restarting the program.

Potential future enhancements could include difficulty levels for the AI, match statistics, win/loss history, customizable game rules, tournament mode, and a graphical user interface.
