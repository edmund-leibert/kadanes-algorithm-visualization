import streamlit as st
import plotly.graph_objects as go
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
user_input = st.text_input("Enter a list of integers separated by commas:", "2, 3, -1, -20, 5, 10")
arr = list(map(int, user_input.split(',')))

# Calculate using Kadane's Algorithm
max_sum, start, end = kadanes_algorithm(arr)
st.write(f"Largest Sum Contiguous Subarray: {arr[start:end+1]}")
st.write(f"Sum: {max_sum}")

# Initialize Plotly Figure
fig = go.Figure()

# X-Axis annotations
xaxis_labels = [f"{i} ({val})" for i, val in enumerate(arr)]

# Graph all contiguous subarrays starting from different positions
for start_idx in range(len(arr)):
    subarray_cumsum = np.cumsum(arr[start_idx:])
    fig.add_scatter(x=xaxis_labels[start_idx:], y=subarray_cumsum, mode='lines', name=f'Starting at {start_idx}')

# Highlight the largest sum contiguous subarray
highlighted_subarray_cumsum = np.cumsum(arr[start:end+1])
fig.add_scatter(x=xaxis_labels[start:end+1], y=highlighted_subarray_cumsum, mode='lines', name='Largest Sum Subarray', line=dict(color='green', width=4))

# Set Figure Layout
fig.update_layout(
    title="Kadane's Algorithm Visualization",
    xaxis_title="Index (Value at Index)",
    yaxis_title="Cumulative Sum"
)

st.plotly_chart(fig)
