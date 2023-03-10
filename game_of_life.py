import pygame

# Define grid parameters
cell_size = 20
num_rows = 10
num_cols = 10

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((num_cols*cell_size, num_rows*cell_size))

# Create the grid array
grid = []
for i in range(num_rows):
    row = [0] * num_cols
    grid.append(row)

# Set some cells to be alive
grid[2][3] = 1
grid[3][3] = 1
grid[4][3] = 1

grid[3][2] = 1


# Define the function that determines the rules
def apply_rules(grid):
    new_grid = []
    for i in range(num_rows):
        row = [0] * num_cols
        new_grid.append(row)
        for j in range(num_cols):
            # Get the number of live neighbors
            num_neighbors = 0
            for ii in range(max(i-1,0), min(i+2,num_rows)):
                for jj in range(max(j-1,0), min(j+2,num_cols)):
                    if ii != i or jj != j:
                        num_neighbors += grid[ii][jj]
            # Apply the rules
            if grid[i][j] == 1 and num_neighbors in [2,3]:
                new_grid[i][j] = 1
            elif grid[i][j] == 0 and num_neighbors == 3:
                new_grid[i][j] = 1
    return new_grid

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    # Apply the rules
    new_grid = apply_rules(grid)
   
    # Update the grid
    grid = new_grid
   
    # Draw the grid
    screen.fill((255, 255, 255))
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (j*cell_size, i*cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (j*cell_size, i*cell_size, cell_size, cell_size))
   
    # Update the display
    pygame.display.update()

    pygame.time.wait(1000)

# Clean up Pygame
pygame.quit()

