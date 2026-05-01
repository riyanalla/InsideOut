import random


class Cell:
    def __init__(self, state):
        self.state = state

    def __str__(self):
        return self.state
    
    def __repr__(self):
        return self.state

    @staticmethod
    def majority(neighbors):
        counts = {}
        for i in neighbors:
            if i.state == 'sad':
                counts[i.state] = counts.get(i.state,0) + 1
            if i.state == 'disgust':
                counts[i.state] = counts.get(i.state,0) + 1
            if i.state == 'anger':
                counts[i.state] = counts.get(i.state,0) + 1
            if i.state == 'joy':
                counts[i.state] = counts.get(i.state,0) + 1
            if i.state == 'fear':
                counts[i.state] = counts.get(i.state,0) + 1
        if counts:
            return max(counts, key=counts.get)
        return random.choice(["joy", "sad", "anger", "fear", "disgust"])

    @staticmethod
    def get_neighbors(row, col, cells):
        neighbors = []
        rows = len(cells)
        cols = len(cells[0]) if rows > 0 else 0
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                if r == 0 and c == 0:
                    continue
                r, c = row + r, col + c
                if 0 <= r < rows and 0 <= c < cols:
                    neighbors.append(cells[r][c])
        return neighbors