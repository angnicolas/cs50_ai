import sys

class Node():
    def __init__ (self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action 
    def __eq__(self,other_node):
        return self.state == other_node.state


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
        # if node in self.explored():

    def contains(self,state):
        return any([nodes for nodes in self.frontier == state])

    def empty(self):
        return self.frontier == []
    

    def remove(self):
        if self.empty():
            raise Exception('Empty frontier')
        else:
            last_element = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return last_element

class QueuFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception('Empty frontier')
        else:
            first_element = self.frontier[0]
            self.frontier = self.frontier[1:]
            return first_element


class Maze():
    def __init__(self,filename):
        self.walls = []
        self.solution = 0
        with open(filename,'r') as f:
            contents = f.read().splitlines()

        self.height = len(contents)
        self.width = max(len(x) for x in contents)

        for i in range(self.height):
            for j in range(self.width):
                row = []
                if contents[i][j] == 'A':
                    self.start = (i,j)
                    row.append(False)  # dont know why
                elif contents[i][j] == 'B':
                    self.goal = (i,j)
                    row.append(False)
                elif contents[i][j] == ' ':
                    row.append(False)
                else:
                    row.append(True)
            self.walls.append(row)

    def print(self):
        for lines in self.walls:
            print(lines)

    def neighbours(self,state) -> list: 
        row , col = state
        actions = [
            ('up',( row - 1 , col)) ,
            ( 'right', (row, col + 1)),
            ('down', (row + 1, col)),
            ('left' , (row, col + 1))
        ]


        playable_actions = []
        for action, (i, j) in actions: 
            if 0 <= i < self.height and 0 <= j < self.width and not self.walls[i][j]:
                playable_actions.append( (action,(i,j)))
        
        return playable_actions

    def solve(self):

        self.explored = set() ## Create a set of explored states
        self.state = Node(self.start, parent = None, action = None)
        self.num_explored = 0
        frontier = StackFrontier()
        frontier.add(self.state)


        while True:
            if frontier.empty():
                raise Exception('Empty frontier')

            node = frontier.remove()
            self.num_explored +=1
            
            if node.state == self.goal:
                actions_list , nodes_list = [], []
                while node.parent != None:
                    actions_list.append(node.action)
                    nodes_list.append(node.state)
                    node = node.parent
                actions_list.reverse()
                nodes_list.reverse()
                self.solution = (actions_list,nodes_list)

            else:
                self.explored.add(node.state)
                for neighbour in self.neighbours(node.state):
                    action = neighbour[0]
                    c = neighbour[1]
                    if not frontier.contains(c) and c not in self.explored:
                        frontier.add( Node(state = c, parent = node,action = action) )

                    
    def output_image(self, filename, show_solution=True, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )
        img.save(filename)               

                















maze  = Maze('src0/maze1.txt')
maze.solve()
