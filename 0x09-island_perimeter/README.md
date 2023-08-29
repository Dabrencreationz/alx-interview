# 0x09-island_perimeter

Here's a breakdown of the task:

- Define the function island_perimeter which takes a single argument, grid, a list of lists representing the island layout.

- Inside the function, initialize a variable count to keep track of the perimeter.

- Get the number of rows and columns in the grid using len(grid) and len(grid[0]) respectively. The special case len(grid[0]) if row else 0 handles the situation where there are no rows in the grid, ensuring that you don't access an index that doesn't exist.

- Use two nested loops to iterate through each cell in the grid.

For each cell, calculate the indices of its four neighboring cells (idx). These indices are checked to ensure they are within the valid range of row and column indices using a list comprehension (check).

If the current cell is land (contains a 1), sum up the values in a list comprehension. This list comprehension checks if the corresponding neighbor exists within the grid (check) and whether that neighbor cell is water (contains a 0). If both conditions are met, it contributes to the count of exposed sides.

After iterating through all cells and calculating the count of exposed sides, return the total count, which represents the perimeter of the island.
