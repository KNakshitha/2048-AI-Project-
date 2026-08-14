<div align="center">

# 🎮 2048 Game in Python

A classic 2048 sliding block puzzle game built from scratch in Python using **Tkinter** for graphical user interface and animation.

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blueviolet?style=for-the-badge)
![Game](https://img.shields.io/badge/Game-2048-orange?style=for-the-badge)

</div>

---

## 📌 Overview

This project is a desktop recreation of the popular single-player sliding block puzzle game **2048**. The objective is to slide numbered tiles on a 4×4 grid using arrow keys, combining matching tiles to create a tile with the number **2048** (and beyond).

---

## ✨ Features

* 🎯 **Classic 4x4 Grid:** Smooth grid rendering with authentic tile color matching for each value.
* ⌨️ **Keyboard Controls:** Play using standard arrow keys (`Up`, `Down`, `Left`, `Right`).
* 🔢 **Tile Merging Logic:** Full implementation of row/column compression, merging, and score tracking.
* 🎲 **Dynamic Tile Spawning:** Generates random tiles (`2` or `4`) after every valid move.
* ⚡ **Zero External Dependencies:** Built entirely with Python standard libraries (`tkinter`, `random`).

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Framework:** `tkinter` (Standard GUI toolkit)
* **Logic:** Matrix transformation & manipulation

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/KNakshitha/2048-AI-Project-.git](https://github.com/KNakshitha/2048-AI-Project-.git)
cd 2048-AI-Project-

2. Run the game
​Since it uses standard built-in Python libraries, no extra pip install is needed!
  On windows/Ubuntu:
        python3 2048.py
  (Or python 2048.py depending on your setup)

🕹️ Controls
  KeyAction
⬆️ Up ArrowSlide all tiles Up
⬇️ Down ArrowSlide all tiles Down
⬅️ Left ArrowSlide all tiles Left
➡️ Right ArrowSlide all tiles Right
