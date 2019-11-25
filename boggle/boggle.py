def make_grid(width, height):
    """
    Create a grid that will hold all of the tiles for a boggle game
    """
    return {(row, col): ' ' for row in range(height) # This function creates a dictionary with the row, column tuple as th key, 
        for col in range(width)}                  # and a space as the value