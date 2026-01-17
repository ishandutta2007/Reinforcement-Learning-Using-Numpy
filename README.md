# 🤖 Reinforcement Learning from Scratch with NumPy

A minimal, self-contained Q-learning example that trains a 4×4 grid-world agent **without any library except NumPy**. This project is a great starting point for anyone interested in learning about the fundamentals of reinforcement learning.

---

## 🌟 Key Features

*   **Minimalist:** Solves a frozen-lake style task (start ➜ goal, avoid traps) using only Python and NumPy.
*   **Fast:** Learns the optimal policy in less than a second on a standard laptop.
*   **Educational:** The code is designed to be clear and easy to understand, with every step explained. You can paste it into a notebook and experiment with it.
*   **Zero Dependencies (almost):** The only dependency is NumPy.

---

## 🚀 Getting Started

1.  Make sure you have Python ≥3.8 and NumPy installed:
    ```bash
    pip install numpy
    ```
2.  Run the `q_learning_numpy.py` file:
    ```bash
    python q_learning_numpy.py
    ```

---

## Code Explanation

The `q_learning_numpy.py` script implements the Q-learning algorithm from scratch. Here's a quick overview of the main components:

*   **Grid World:** The environment is a 4x4 grid. The agent can move up, down, left, or right.
*   **Q-table:** A table that stores the expected return for each state-action pair.
*   **Q-learning algorithm:** The agent learns the optimal policy by iteratively updating the Q-table based on its experiences.

---

## 🙏 Contributing

Contributions are welcome! If you have any ideas for improving the code or documentation, please open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License. See the `License` file for details.

---

### ✨ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ishandutta2007/Reinforcement-Learning-Using-Numpy&type=date&legend=top-left)](https://www.star-history.com/#ishandutta2007/Reinforcement-Learning-Using-Numpy&type=date&legend=top-left)