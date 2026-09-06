
# 🐍 Neon Snake Game

![Snake Gameplay](assets/snake-game.mp4) [click to download]

A modern, cyberpunk-themed twist on the classic Snake game, built with Python's built-in `turtle` library and Object-Oriented Programming (OOP).

## ✨ Features
- 🎨 **Neon Aesthetic:** Dark navy UI with glowing green and hot pink elements.
- 🌈 **Gradient Body:** Dynamic color shifting as the snake grows.
- 🔄 **Wrap-around Mechanics:** Pass through walls to teleport to the opposite side.
- 🏆 **Session High Score:** Tracks your best run in real-time.

## 📂 Project Structure
Built with clean, modular OOP principles:
```text
📦 neon-snake-game
 ┣ 📂 assets/
 ┃ ┗ 📜 snake.gif
 ┣ 📜 main.py          # Game loop & setup
 ┣ 📜 snake.py         # Snake movement & logic
 ┣ 📜 food.py          # Food spawning
 ┗ 📜 scoreboard.py    # UI & score tracking
```
## 🚀 How to Run
No external dependencies required! Just Python 3.x.
bash
git clone https://github.com/da69sh/neon-snake-game.git
cd neon-snake-game
python main.py

## 🎮 Controls
- **Arrow Keys:** Change direction (⬆️ ⬇️ ⬅️ ➡️)
- **Goal:** Eat the 🟣 hot pink food to grow. Avoid hitting your own body!
- *Pro Tip:* Hitting the wall won't kill you; you'll wrap around to the other side.

## 🔮 Future Improvements
- [ ] Save high score persistently (JSON/TXT).
- [ ] Dynamic speed increase as score grows.
- [ ] Add retro sound effects.
