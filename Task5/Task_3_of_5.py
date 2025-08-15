# Task3: Tuple Operations
nigerian_states = tuple(input("Enter state:") for _ in range(5))
print("first:", nigerian_states[0], "Last:", nigerian_states[-1])
print("Lagos?", "Yes" if "Lagos" in nigerian_states else "No")
print("count:", len(nigerian_states))