import pygame
import random
import string
import math

# Initialize Pygame
pygame.init()

# Define window dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)  # Create a borderless window
pygame.display.set_caption("Fireworks")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
aquamarine4 = (69, 139, 116)  # RGB code for aquamarine4

# Define border thickness
border_width = 2

# Load custom font
font_path = "PixelifySans-Regular.ttf"  # Make sure the path is correct
font = pygame.font.Font(font_path, 24)  # Reduce font size for more letters

# Draw the frame with segments
def draw_frame():
    # Draw the frame segments
    pygame.draw.line(screen, white, (30, 30), (width - 30, 30), border_width)  # Top
    pygame.draw.line(screen, white, (30, 30), (30, height - 80), border_width)  # Left
    pygame.draw.line(screen, white, (width - 30, 30), (width - 30, height - 80), border_width)  # Right
    pygame.draw.line(screen, white, (30, height - 80), (width // 2 - 80, height - 80), border_width)  # Bottom left
    pygame.draw.line(screen, white, (width // 2 + 100, height - 80), (width - 30, height - 80), border_width)  # Bottom right

# Function to generate random points with letters
def generate_random_points(num_points):
    points = []
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!?"
    letters = ''.join(char for char in s if char in string.ascii_letters)
    for _ in range(num_points):
        x = random.randint(60, width-60)
        y = random.randint(60, height - 160)  # Leave space for the trash
        letter = random.choice(letters)
        vx = random.uniform(-1, 1)  # Velocity in x
        vy = random.uniform(-1, 1)  # Velocity in y
        size = 24  # Initial font size
        points.append([x, y, letter, size, vx, vy, False])  # Add a state for click
    return points

# Function to check collisions and adjust directions
def check_collisions(points):
    for i, (x1, y1, _, _, vx1, vy1, _) in enumerate(points):
        for j, (x2, y2, _, _, vx2, vy2, _) in enumerate(points):
            if i != j:
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if distance < 24:  # Collision threshold
                    # Reverse directions to move letters apart
                    points[i][4] = -vx1
                    points[i][5] = -vy1
                    points[j][4] = -vx2
                    points[j][5] = -vy2

# Draw the trash with animation
def draw_trash(mouse_x, mouse_y, is_open, angle):
    trash_x = width // 2 - 100
    trash_y = height - 80
    trash_width = 200
    trash_height = 50
    border_width = 3

    # Draw the trash rectangle
    pygame.draw.aalines(screen, white, False, [(trash_x, trash_y),(trash_x,trash_y+trash_height),(trash_x+trash_width, trash_y+trash_height),(trash_x+trash_width, trash_y)], blend=1)
    # Draw the open top segment with animation
    if is_open:
        end_x1 = trash_x + trash_width // 2 + int(100 * math.cos(math.radians(angle)))
        end_y1 = trash_y - int(100 * math.sin(math.radians(angle)))
        end_x2 = trash_x + trash_width // 2 - int(100 * math.cos(math.radians(angle)))
        end_y2 = trash_y - int(100 * math.sin(math.radians(angle)))
        pygame.draw.line(screen, white, (trash_x, trash_y), (end_x1, end_y1), border_width)
        pygame.draw.line(screen, white, (trash_x + trash_width, trash_y), (end_x2, end_y2), border_width)
    else:
        pygame.draw.line(screen, white, (trash_x, trash_y), (trash_x + trash_width, trash_y), border_width)

    return trash_x, trash_y, trash_width, trash_height

# Main loop
running = True
clock = pygame.time.Clock()
points = generate_random_points(200)  # Initial number of points
selected_letter = None
trash_open = False
trash_angle = 0
trash_animation_speed = 20
countdown = 0
collected_letters = []
reset_countdown = False
display_message = False
message_timer = 0
falling_letter = None
falling_speed = 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for i, (x, y, letter, size, vx, vy, clicked) in enumerate(points):
                if x - size // 2 < mouse_x < x + size // 2 and y - size // 2 < mouse_y < y + size // 2:
                    points[i][6] = True
                    selected_letter = i
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_letter is not None:
                points[selected_letter][6] = False
                mouse_x, mouse_y = event.pos
                x, y = points[selected_letter][:2]
                if trash_x < x < trash_x + trash_width and trash_y < y < trash_y + trash_height:
                    falling_letter = points.pop(selected_letter)
                    falling_letter[1] = trash_y  # Position the letter above the trash
                    trash_open = True
                selected_letter = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_countdown = True
                countdown = 300  # Increase countdown duration
                display_message = True
                message_timer = 120  # Display duration for the message

    # Fill the screen with the aquamarine4 color
    screen.fill(aquamarine4)

    # Draw the frame with segments
    draw_frame()

    # Draw a solid white rectangle at the bottom
    pygame.draw.rect(screen, white, (0, height - 50, width, 50))

    # Check collisions
    check_collisions(points)

    # Draw the trash with animation
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if selected_letter is not None:
        x, y = points[selected_letter][:2]
        if trash_x < x < trash_x + trash_width and trash_y < y < trash_y + trash_height:
            trash_open = True
        if trash_open and trash_angle < 160:
            trash_angle += trash_animation_speed
        elif not trash_open and trash_angle > 0:
            trash_angle -= trash_animation_speed
    else:
        if trash_angle > 0:
            trash_angle -= trash_animation_speed

    trash_x, trash_y, trash_width, trash_height = draw_trash(mouse_x, mouse_y, trash_open, trash_angle)

    # Update and display the points
    for i, (x, y, letter, size, vx, vy, clicked) in enumerate(points):
        if not clicked:
            x += vx  # Update x position
            y += vy  # Update y position

            # Reappear on the other side if the letter goes off-screen
            if x < 30: x = width - 30
            if x > width - 30: x = 30
            if y < 30: y = height - 80
            if y > height - 80: y = 30

        # Calculate the distance to the mouse
        distance_to_mouse = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)

        # Adjust size based on distance
        if distance_to_mouse < 100:
            size = int(24 + (48 - 24) * (1 - distance_to_mouse / 100))  # Gradual zoom
        else:
            size = 24  # Restore font size

        if clicked:
            x, y = mouse_x, mouse_y  # Follow the mouse

        points[i] = [x, y, letter, size, vx, vy, clicked]  # Update the points list

        font = pygame.font.Font(font_path, size)
        text = font.render(letter, True, white)
        screen.blit(text, (x - size // 2, y - size // 2))

    # Animate the letter falling into the trash
    if falling_letter:
        falling_letter[1] += falling_speed  # Fall slowly
        if falling_letter[1] > trash_y + trash_height:
            collected_letters.append(falling_letter[2])
            falling_letter = None
            trash_open = False
        else:
            font = pygame.font.Font(font_path, falling_letter[3])
            text = font.render(falling_letter[2], True, white)
            screen.blit(text, (falling_letter[0] - falling_letter[3] // 2, falling_letter[1] - falling_letter[3] // 2))

    # Display collected letters at the bottom of the screen
    collected_text = ' '.join(collected_letters)
    font = pygame.font.Font(font_path, 24)
    text = font.render(collected_text, True, aquamarine4)
    screen.blit(text, (10, height - 30))

    # Display the message and countdown if all letters are collected or "R" is pressed
    if len(points) == 0 or reset_countdown:
        if display_message:
            font = pygame.font.Font(font_path, 48)
            text = font.render("Oops, no more letters!", True, white)
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
            message_timer -= 1
            if message_timer == 0:
                display_message = False
                countdown = 300  # Start countdown after message display
        else:
            if countdown > 0:
                countdown -= 1
                if countdown % 60 == 0:
                    font = pygame.font.Font(font_path, 48)
                    text = font.render(str(countdown // 60), True, white)
                    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
            if countdown == 0:
                points = generate_random_points(200)
                collected_letters = []
                reset_countdown = False

    # Update the display
    pygame.display.flip()
    clock.tick(30)  # Adjust this value to change the animation speed

pygame.quit()
