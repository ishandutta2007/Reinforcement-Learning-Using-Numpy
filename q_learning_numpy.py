import numpy as np

# 1. world --------------------------------------------------------------------
n = 4
nS, nA = n * n, 4
GOAL = 15
traps = {5, 7, 11, 12}          # cells that give –1
R = np.zeros(nS); R[GOAL] = 1.; R[list(traps)] = -1.

# 2. dynamics -----------------------------------------------------------------
P = np.zeros((nS, nA, nS))      # deterministic transitions
for s in range(nS):
    row, col = divmod(s, n)
    for a, (dr, dc) in enumerate(((-1,0),(0,1),(1,0),(0,-1))):
        nr, nc = row+dr, col+dc
        if 0 <= nr < n and 0 <= nc < n:        # stay inside
            P[s, a, nr*n+nc] = 1.
        else:
            P[s, a, s] = 1.                    # hit wall → stay

# 3. Q-learning hyper-params --------------------------------------------------
α = 0.8          # learning rate
γ = 0.95         # discount
ε = 0.2          # ε-greedy exploration
episodes = 5_000
Q = np.zeros((nS, nA))

# 4. training loop ------------------------------------------------------------
rng = np.random.default_rng(42)
for _ in range(episodes):
    s = 0
    while s != GOAL:
        # ε-greedy action
        if rng.random() < ε:
            a = rng.integers(nA)
        else:
            a = Q[s].argmax()
        # take step
        s2 = rng.choice(nS, p=P[s, a])
        r = R[s2]
        # Bellman update
        Q[s, a] += α * (r + γ * Q[s2].max() - Q[s, a])
        s = s2

# 5. show learned policy ------------------------------------------------------
policy = np.array(list('↑→↓←'))[Q.argmax(1)].reshape(n, n)
print("learned policy:")
print(policy)
print("final Q-table (clip at 2 decimals):")
print(np.round(Q, 2))
