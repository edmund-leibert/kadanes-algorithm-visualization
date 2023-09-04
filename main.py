import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def kadanes_algorithm(arr):
    max_current = max_global = arr[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(arr)):
        if arr[i] > max_current + arr[i]:
            max_current = arr[i]
            temp_start = i
        else:
            max_current += arr[i]

        if max_current > max_global:
            max_global = max_current
            start = temp_start
            end = i

    return max_global, start, end

st.title("Kadane's Algorithm Visualization")

# User input for array
user_input = st.text_input("Enter a list of integers separated by commas:", "1, -2, 3, 4, -1, 2, 1, -5, 4")
arr = list(map(int, user_input.split(',')))

# Calculate using Kadane's Algorithm
max_sum, start, end = kadanes_algorithm(arr)
st.write(f"Largest Sum Contiguous Subarray: {arr[start:end+1]}")
st.write(f"Sum: {max_sum}")

# Visualization using Matplotlib
plt.figure(figsize=(10, 5))
plt.axhline(0, color="gray", lw=0.5)
plt.plot(arr, "o-", label="Array elements")
plt.fill_between(range(start, end + 1), arr[start:end + 1], color="green", alpha=0.5, label="Max Sum Subarray")
plt.title("Kadane's Algorithm Visualization")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()

# Show plot in Streamlit
st.pyplot(plt.gcf())
