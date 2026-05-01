from cell import Cell
from grid import Grid
import pygame
import random

pygame.init()
font = pygame.font.SysFont(None, 30, bold=False, italic=False)
titleFont = pygame.font.SysFont(None, 40, bold=False, italic=False)

w = 1000
h = 750
screen = pygame.display.set_mode([w,h])
clock = pygame.time.Clock()

grid = Grid([
[Cell('sad'), Cell('joy'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('sad'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy')],
[Cell('anger'), Cell('joy'), Cell('disgust'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy')],
[Cell('joy'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('joy'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('joy'), Cell('sad'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('fear')],
[Cell('sad'), Cell('fear'), Cell('fear'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('fear'), Cell('sad'), Cell('anger'), Cell('joy'), Cell('fear'), Cell('sad'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy')],
[Cell('disgust'), Cell('sad'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('fear'), Cell('joy'), Cell('anger'), Cell('sad'), Cell('joy'), Cell('disgust'), Cell('fear'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy')],
[Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('fear'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust')],
[Cell('fear'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('fear'), Cell('joy')],
[Cell('sad'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('fear'), Cell('sad'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad')],
[Cell('disgust'), Cell('joy'), Cell('sad'), Cell('anger'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy')],
[Cell('joy'), Cell('fear'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear')],
[Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy')],
[Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger')],
[Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy'), Cell('disgust'), Cell('joy'), Cell('anger'), Cell('joy'), Cell('sad'), Cell('joy'), Cell('fear'), Cell('joy')]
]) #giant grid


imageMap = {
        "joy": pygame.image.load("joy.png"),
        "sad": pygame.image.load("sadness.png"),
        "disgust": pygame.image.load("disgust.png"),
        "fear": pygame.image.load("fear.png"),
        "anger": pygame.image.load("anger.png") #similar to p5 js but good to show all on grid
    }

for key in imageMap:
    imageMap[key] = pygame.transform.scale(imageMap[key], (50, 50))


energy = 50
running = True

emotionStrengths = {"joy": 0.7, "sad": 0.5, "anger": 0.4, "fear": 0.3, "disgust": 0.3}
startTime = pygame.time.get_ticks()
latestTime = 0


def nowClick(r, c): # only for user interaction if decide to do that
    currentState = grid.cells[r][c].state
    for nextR in [-1, 0, 1]:
        for nextC in [-1, 0, 1]:
            newR = r+nextR
            newC = c+nextC
            if 0<=newR< len(grid.cells) and 0<=newC<len(grid.cells[0]):
                if newR == newC:
                    grid.cells[newR][newC].state = currentState
                else:
                    strength = emotionStrengths[currentState]
                    if random.random() < strength:
                        grid.cells[newR][newC].state = currentState
    # if currentState == "fear" or currentState == "disgust":
    #     grid.cells[r][c].state = "sad" #so this is for random emotion, cuz fear and disgust arent as important
    if currentState == "joy" and Cell.majority(Cell.get_neighbors(r, c, grid.cells)) == "joy":
        grid.cells[r][c].state = "sad"

text = "Let's Begin"
while running:
    screen.fill((250, 250, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = pygame.time.get_ticks()
    done = now - startTime

    if now - latestTime > 500:

        if 5000 < done < 15000:
            grid.cells = Grid.firstPart(grid.cells)
            text = "Wrath of Joy"
        
        elif 15000 < done < 25000:
            grid.cells = Grid.secondPart(grid.cells)
            text = "Sadness Takes Over"
        
        elif 25000 < done < 35000:
            grid.cells = Grid.thirdPart(grid.cells)
            text = "Uncontrolled Ship - Chaos"
        
        elif done > 35000:
            grid.cells = Grid.lastPart(grid.cells)
            text = "Balance"
        
        latestTime = now

    counts = {"joy": 0, "sad": 0, "anger": 0, "fear": 0, "disgust": 0}

    for row in grid.cells:
        for cell in row:
            counts[cell.state] += 1 #how many of each emotion 

    total = sum(counts.values())

    energy = (
        counts.get("joy", 0) * 1.6 +
        counts.get("sad", 0) * 0.3 +
        counts.get("anger", 0) * 1.7 +
        counts.get("fear", 0) * 1.2 +
        counts.get("disgust", 0) * 0.7
    ) 

    energy = max(0, energy)
    
    mainTitle = titleFont.render("Inside Out: The Movie", True, (0,0,15))
    screen.blit(mainTitle, (10, 10))
    energy_text = font.render(f"Energy: {int(energy)}", True, (0,0,0))
    screen.blit(energy_text, (10, 40))
    textLabel = font.render(f"Phase: {text}", True, (0,0,0))
    screen.blit(textLabel, (10, 70))

    for r in range(len(grid.cells)):
        for c in range(len(grid.cells[r])):
            state = grid.cells[r][c].state
            img = imageMap[state]
            screen.blit(img, (c*50, r*50 + 100)) #display all together

    pygame.display.flip()
    clock.tick(50)


pygame.quit()