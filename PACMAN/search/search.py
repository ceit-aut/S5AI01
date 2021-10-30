# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    fringe = util.Stack() # Our fringe for extracing nodes
    visited = [] # We are going to use the Graph data structure 
    actions = [] # We need to have a path to return
    path = util.Stack() # For having the current path we are going to use stack

    fringe.push(problem.getStartState()) # Getting the first node explored in fringe
    current_node = fringe.pop() # A current node for locating the current status

    while not problem.isGoalState(current_node):
        if current_node not in visited:
            visited.append(current_node)
            successors = problem.getSuccessors(current_node)

            for successor in successors:
                fringe.push(successor[0])
                temp = actions + [successor[1]] # We add a copy of past actions + new action to a temp just to add it to stack
                path.push(temp)

        current_node = fringe.pop()
        actions = path.pop() # This means that we are done with a node and we take out its path to check the goal result
    
    return actions

    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    fringe = util.Queue() # Our fringe for extracing nodes
    visited = [] # Just like DFS we have visitied for graph Data structure
    actions = [] # Actions that we should return
    path = util.Queue() # A list for storing all of the actions

    fringe.push(problem.getStartState()) # Getting the first node to explore
    current_node = fringe.pop() # A current node setting

    while not problem.isGoalState(current_node):
        if current_node not in visited:
            visited.append(current_node)
            successors = problem.getSuccessors(current_node)

            for successor in successors:
                fringe.push(successor[0])
                temp = actions + [successor[1]]
                path.push(temp)

        current_node = fringe.pop()
        actions = path.pop()

    return actions

    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    fringe = util.PriorityQueue() # Our fringe to extracing nodes
    visited = [] # Same as always, the visited nodes
    actions = [] # Actions to return
    path = util.PriorityQueue() # Our list of all pathes

    fringe.push(problem.getStartState(), 0) # Getting the first node
    current_node = fringe.pop() # Setting the current node

    while not problem.isGoalState(current_node):
        if current_node not in visited:
            visited.append(current_node)
            successors = problem.getSuccessors(current_node)

            for successor in successors:
                temp = actions + [successor[1]]
                cost = problem.getCostOfActions(temp)
                if successor[0] not in visited: # A search for the child of a successor in previous nodes
                    fringe.push(successor[0], cost)
                    path.push(temp, cost)
        
        current_node = fringe.pop()
        actions = path.pop()
    
    return actions

    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    fringe = util.PriorityQueue()
    visited = []
    actions = []
    path = util.PriorityQueue()

    fringe.push(problem.getStartState(), 0)
    current_node = fringe.pop()

    while not problem.isGoalState(current_node):
        if current_node not in visited:
            visited.append(current_node)
            successors = problem.getSuccessors(current_node)

            for successor in successors:
                temp = actions + [successor[1]]
                cost = problem.getCostOfActions(temp) + heuristic(successor[0], problem)
                if successor[0] not in visited:
                    fringe.push(successor[0], cost)
                    path.push(temp, cost)
        
        current_node = fringe.pop()
        actions = path.pop()

    return actions

    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
