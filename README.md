# Pong Game

A simple **Pong-style arcade game** where you play against a bot opponent. Control your paddle, block the ball, and try to outscore the opponent!

## 🎮 Gameplay

- You control the **right paddle**
- The **bot controls the left paddle**
- The ball bounces between paddles
- If the opponent misses the ball, you score a point
- Scores are **saving when you exiting the game**

## ⌨️ Controls

| Key | Action |
|----|------|
| **W** | Move paddle up |
| **S** | Move paddle down |

## 🤖 Bot Opponent

The bot automatically moves its paddle to follow the ball and attempt to block it.

## 🧮 Scoring

- Both the **player** and **bot** have a score
- A point is awarded when the opponent fails to hit the ball
- **Scores persist between sessions** and are saved when you exit the game

## 📦 Features

- Classic Pong gameplay
- Player vs Bot
- Simple keyboard controls
- Persistent score saving
- Lightweight and easy to run

# 🚀 Installation & Running the Game

Follow these steps to run the game locally.

## 1. Clone the Repository

```bash
git clone https://github.com/LubCore12/Pong-Game.git
cd pong-game
```

## 2. Create a Virtual Environment

 - Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

 - Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies

Install the required packages from requirements.txt.

```bash
pip install -r requirements.txt
```

## 4. Run the Game

```bash
python code/main.py
```


## 🕹️ Goal

Score as many points as possible against the bot and improve your high score over time.

---

Enjoy playing Pong! 🏓
