import numpy as np

# Define the reward matrix for a 4-state environment
R = np.array([
    [-1, 2, 0, 1],  # Rewards from s0
    [1, -1, 3, 2],  # Rewards from s1
    [0, 3, -1, 4],  # Rewards from s2
    [2, 1, 0, -1]   # Rewards from s3
])

# Define the discount factor for the 4x4 matrix scenario
gamma = 0.9

# Define a more sophisticated set of policies with different actions for each state
policies = {
    'Policy1': [0, 1, 2, 3],  # Different action in each state
    'Policy2': [1, 0, 3, 2],  # Different action in each state
    'Policy3': [2, 3, 0, 1],  # Different action in each state
    'Policy4': [3, 2, 1, 0],  # Different action in each state
    'Policy5': [0, 3, 1, 2],  # Different action in each state
    'Policy6': [1, 2, 3, 0],  # Different action in each state
    # ... more policies could be defined
}

# Calculate the expected reward for each sophisticated policy
expected_rewards = {}
for policy_name, actions in policies.items():
    expected_reward = 0
    for t, action in enumerate(actions):
        # Assuming the agent moves to the next state as per action
        state = t
        expected_reward += (gamma**t) * R[state, action]
    expected_rewards[policy_name] = expected_reward

# Find the optimal policy among the sophisticated set
optimal_policy = max(expected_rewards, key=expected_rewards.get)
optimal_reward = expected_rewards[optimal_policy]

# Print the optimal policy and its expected reward
print("Optimal Policy:", optimal_policy)
print("Expected Reward:", optimal_reward)



