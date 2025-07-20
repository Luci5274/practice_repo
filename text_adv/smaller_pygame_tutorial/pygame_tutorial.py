# Import the pygame module, which gives us game functionality
import pygame

# Initialize all imported pygame modules (must be called before using any pygame features)
pygame.init()

# --- Define color constants as RGB tuples ---
white = (255, 255, 255)   # Background color
green = (0, 255, 0)       # Text color
blue = (0, 0, 128)        # Background for text

# Set the dimensions of the window
x = 600
y = 600

# Create the display window with width x and height y
display_surface = pygame.display.set_mode((x, y))

# Set the window title
pygame.display.set_caption('Show text')

# --- Load a font and prepare the text to display ---

# Load a system font with size 32 (freesansbold.ttf comes with pygame)
font = pygame.font.Font('freesansbold.ttf', 32)

# Render the text with:
#  - The actual string to display
#  - Antialiasing turned on (True)
#  - The text color (green)
#  - The background color of the text (blue)
text = font.render(' >:)', True, green, blue)

# Get the rectangle that contains the rendered text so we can position it
textRect = text.get_rect()

# Center the textRect within the window
textRect.center = (x // 2, y // 2)

# --- Start the main game loop ---
while True:
    # Fill the screen with white before drawing anything else
    display_surface.fill(white)

    # Draw the text onto the screen at the position defined by textRect
    display_surface.blit(text, textRect)

    # Handle events (key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        # If the window close button is clicked, quit the game safely
        if event.type == pygame.QUIT:
            pygame.quit()  # Uninitialize all pygame modules
            quit()         # Exit the Python program

    # Update the screen with the new frame
    pygame.display.update()
