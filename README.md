# 🤖 Reinforcement Learning from Scratch with NumPy

[![GitHub license](https://img.shields.io/github/license/ishandutta2007/Reinforcement-Learning-Using-Numpy)](https://github.com/ishandutta2007/Reinforcement-Learning-Using-Numpy/blob/master/License)
[![GitHub stars](https://img.shields.io/github/stars/ishandutta2007/Reinforcement-Learning-Using-Numpy)](https://github.com/ishandutta2007/Reinforcement-Learning-Using-Numpy/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ishandutta2007/Reinforcement-Learning-Using-Numpy)](https://github.com/ishandutta2007/Reinforcement-Learning-Using-Numpy/network)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
<a href="https://github.com/ishandutta2007?tab=followers">
  <img alt="followers" title="Follow me on Github" src="https://custom-icon-badges.herokuapp.com/github/followers/ishandutta2007?color=236ad3&labelColor=1155ba&style=for-the-badge&logo=person-add&label=Follow&logoColor=white"/>
</a>

A minimal, self-contained **Q-learning** implementation that trains a 4×4 grid-world agent **without any high-level library except NumPy**. This project is an ideal educational resource for understanding the core mechanics of Reinforcement Learning (RL) from first principles.

---

## 📋 Table of Contents

- [🌟 Key Features](#-key-features)
- [🧠 Why Reinforcement Learning from Scratch?](#-why-reinforcement-learning-from-scratch)
- [🚀 Getting Started](#-getting-started)
- [📖 How it Works](#-how-it-works)
- [📊 Results](#-results)
- [🙏 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🌟 Key Features

*   **⚡ Minimalist:** Solves a frozen-lake style task (Start ➜ Goal, avoid traps) using basic Python and NumPy.
*   **🏎️ Fast Performance:** Learns the optimal policy in less than a second on a standard laptop.
*   **🎓 Educational Focused:** The code is designed for clarity, making it perfect for students and researchers to experiment with.
*   **🔗 Zero Dependencies:** No need for OpenAI Gym/Gymnasium, PyTorch, or TensorFlow. Just pure NumPy.

---

## 🧠 Why Reinforcement Learning from Scratch?

Building algorithms like **Q-Learning** from scratch helps in understanding:
- **Markov Decision Processes (MDPs):** How states, actions, and rewards interact.
- **The Bellman Equation:** The mathematical foundation behind value updates.
- **Exploration vs. Exploitation:** Balancing $\epsilon$-greedy strategies.
- **Vectorization:** Leveraging NumPy for efficient state-transition matrix operations.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python ≥3.8 and NumPy installed:

```bash
pip install numpy
```

### Running the Agent

Clone the repository and run the main script:

```bash
git clone https://github.com/ishandutta2007/Reinforcement-Learning-Using-Numpy.git
cd Reinforcement-Learning-Using-Numpy
python q_learning_numpy.py
```

---

## 📖 How it Works

The `q_learning_numpy.py` script implements the **Temporal Difference (TD) Q-learning** algorithm:

1.  **Environment Setup:** A 4x4 grid where specific cells are "traps" (reward -1) and one is the "goal" (reward +1).
2.  **Q-Table Initialization:** A state-action matrix initialized to zeros.
3.  **Training Loop:** 
    - The agent selects actions using an **$\epsilon$-greedy** policy.
    - Transitions are deterministic based on the grid dynamics.
    - The Q-values are updated using the formula:
      $$Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$
4.  **Policy Extraction:** Once trained, the agent derives the optimal path by taking the `argmax` of each state in the Q-table.

---

## 📊 Results

After 5,000 episodes, the agent learns a policy represented by directional arrows:

```text
learned policy:
[['↓' '→' '↓' '←']
 ['↓' '↑' '↓' '↑']
 ['→' '↓' '↓' '↑']
 ['↑' '→' '→' '↑']]
```

*Note: The actual output may vary slightly due to the stochastic nature of exploration.*

---

## 🙏 Contributing

Contributions are welcome! Whether it's adding new environments, optimizing the NumPy operations, or improving the documentation.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [License](License) file for details.

---

### ✨ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ishandutta2007/Reinforcement-Learning-Using-Numpy&type=date&legend=top-left)](https://www.star-history.com/#ishandutta2007/Reinforcement-Learning-Using-Numpy&type=date&legend=top-left)
