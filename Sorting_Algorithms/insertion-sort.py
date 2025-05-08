arr = [2,5,8,1,4,9,3,7]

for i in range(len(arr)): #N Times
    for j in range(i - 1, -1, -1): #N Times
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        else:
            break

print(arr)

# timeComplexity = O(N^2)

#For Grid Visualatization

# import matplotlib.pyplot as plt
# import numpy as np
# import time

# arr = [2, 5, 8, 1, 4, 9, 3, 7]
# steps = [arr.copy()]  # Store each step

# # Initialize the figure
# fig, ax = plt.subplots(figsize=(6, 6))
# ax.set_title("Insertion Sort - Grid Visualization")
# ax.axis("off")  # Hide the axes

# # Function to update the grid
# def update_grid():
#     ax.clear()
#     ax.set_title("Insertion Sort - Grid Visualization")
#     ax.axis("off")
    
#     # Create a table with the current sorting step
#     table_data = np.array(steps)
#     table = ax.table(cellText=table_data, cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
    
#     # Style the table
#     for (i, j), cell in table.get_celld().items():
#         cell.set_edgecolor("black")
#         cell.set_linewidth(2)
#         if i == len(steps) - 1:  # Highlight the latest row
#             cell.set_facecolor("lightblue")
    
#     plt.pause(0.5)  # Pause for animation effect

# # Insertion Sort Algorithm (with real-time visualization)
# for i in range(len(arr)):
#     for j in range(i - 1, -1, -1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             steps.append(arr.copy())  # Store state after swap
#             update_grid()  # Update visualization
#         else:
#             break

# plt.show()
