import random
from cell import Cell


class Grid:
    def __init__(self, cells):
        self.cells = cells

    @staticmethod
    def firstPart(cells):
        newCellsArray = []
        for r in range(len(cells)):
            newRow = []
            for c in range(len(cells[r])):
                newRow.append(Cell(cells[r][c].state))
            newCellsArray.append(newRow)
        for r in range(len(cells)):
            for c in range(len(cells[r])):
                neighbors = Cell.get_neighbors(r, c, cells)
                majority = Cell.majority(neighbors)
                if majority == "joy":
                    if random.random() < 0.35:
                        newCellsArray[r][c].state = "joy"
                elif random.random() < 0.15:
                        newCellsArray[r][c].state = majority
        return newCellsArray

    @staticmethod
    def secondPart(cells):
        newCellsArray = []
        for r in range(len(cells)):
            newRow = []
            for c in range(len(cells[r])):
                newRow.append(Cell(cells[r][c].state))
            newCellsArray.append(newRow)
        for r in range(len(cells)):
            for c in range(len(cells[r])):
                neighbors = Cell.get_neighbors(r, c, cells)
                majority = Cell.majority(neighbors)
                sadneighbors = 0
                for n in neighbors:
                    if n.state == "sad":
                        sadneighbors+=1
                if sadneighbors >= 3 and cells[r][c].state == "sad":
                    if random.random() < 0.4:
                        newCellsArray[r][c].state = "sad"
                elif majority == "joy":
                    if random.random() < 0.03:
                        newCellsArray[r][c].state = "sad"
                elif random.random() < 0.1:
                        newCellsArray[r][c].state = majority
        return newCellsArray

    @staticmethod
    def thirdPart(cells):
        newCellsArray = []
        for r in range(len(cells)):
            newRow = []
            for c in range(len(cells[r])):
                newRow.append(Cell(cells[r][c].state))
            newCellsArray.append(newRow)
        limitedEmotions = ["anger", "fear", "disgust"]
        for r in range(len(cells)):
            for c in range(len(cells[r])):
                neighbors = Cell.get_neighbors(r, c, cells)
                counts = {}
                for neighbor in neighbors:
                    if (neighbor.state in limitedEmotions):
                        counts[neighbor.state] = counts.get(neighbor.state, 0) + 1
                if counts:
                    if random.random() < 0.8:
                        state = random.choices(list(counts.keys()), weights = list(counts.values()))[0]
                    else:
                        state = random.choices(["anger", "fear", "disgust", "joy", "sad"], weights = [3,3,3,1,1])[0]
                else:
                    state = cells[r][c].state
                if random.random() < 0.05:
                    state = random.choice(["anger", "fear", "disgust"])
                newCellsArray[r][c].state = state
        return newCellsArray

    @staticmethod
    def lastPart(cells):
        newCellsArray = []
        for r in range(len(cells)):
            newRow = []
            for c in range(len(cells[r])):
                newRow.append(Cell(cells[r][c].state))
            newCellsArray.append(newRow)
        emotions = ["anger", "fear", "disgust", "joy", "sad"]
        for r in range(len(cells)):
            for c in range(len(cells[r])):
                neighbors = Cell.get_neighbors(r, c, cells)
                counts = {}
                for neighbor in neighbors:
                    counts[neighbor.state] = counts.get(neighbor.state, 0) + 1
                if counts:
                    state = random.choices(list(counts.keys()), weights = list(counts.values()))[0]
                else:
                    state = cells[r][c].state
                if random.random() < 0.1:
                    state = random.choice(emotions)
                newCellsArray[r][c].state = state
        return newCellsArray