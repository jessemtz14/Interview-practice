# num islands

# given a 2d grid of '1'(land) and '0' (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water.

# example :
# grid = {
#     ['1', '1', '0', '0'],
#     ['1', '1', '0', '0'],
#     ['0', '0', '1', '0'],
#     ['0', '0', '0', '1']
# }
# output: 3

from collections import deque

def num_islands(grid):
    # check if the grid is empty, if yes return 0
    if not grid:
        return 0
    # Initialize the rows, cols, visited set and island count
    rows, cols = len(grid), len(grid[0])
    visited = set()
    island_count = 0

    # set directions for moving up, down, left, right in the grid
    directions = {
        (1, 0), # down ( row  + 1, col)
        (-1, 0), # up (row - 1, col)
        (0, 1), # right (row, col + 1)
        (0, -1)  # left (row, col - 1)
    }

    # loop through each cell in the grid
    for row in range(rows):
        for col in range(cols):

            # if the cell is land(1) and not visited, we found a new island
            if grid[row][col] == '1' and (row, col) not in visited:
                island_count += 1 # increment the island count

                visited.add((row, col)) # mark the current cell as visited
                queue = deque([(row, col)]) # create a queue for BFS and add the current cell

                # perform BFS to visit all connected land cells
                while queue:
                    row, col = queue.popleft() # get the current cell from the queue

                    for dir_row, dir_col in directions:
                        new_row = row + dir_row
                        new_col = col + dir_col

                        if(
                            0 <= new_row < rows and # check if the new row is witin bounds
                            0 <= new_col < cols and # check if the new col is within bounds
                            grid[new_row][new_col] == '1' and # check if the new cell is land
                            (new_row, new_col) not in visited # check if the new cell is not visited
                        ):
                            visited.add((new_row, new_col)) # mark the new cell as visited
                            queue.append((new_row, new_col)) # add the new cell to the queue
    return island_count # return the total number of islands


# test case
if __name__ == "__main__":
    grid = [
        ['1', '1', '0', '0'],
        ['1', '1', '0', '0'],
        ['0', '0', '1', '0'],
        ['0', '0', '0', '1']
    ]
    print(num_islands(grid)) # Output: 3
    if num_islands(grid) == 3:
        print("Test case passed!")
    else:
        print("Test case failed!")

