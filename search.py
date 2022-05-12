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
    
    """soducode:
    visited
    fringe
    while currentState is not goal
        if currentState has not been visited

    """
    # Old fail version:
    # visited = set() # The collection of visited nodes
    # fringe = util.Stack() # The collection of non-visited nodes
    # actionPath = [] # The record of all path the algorithm found
    # fringe.push((problem.getStartState(), actionPath)) # Only one positional argument can be pushed into set. The visited path will be recorded in `actionPath`
    # 
    # currentState, currentPath = fringe.pop()
    # visited.add(currentState)
    #
    # while not problem.isGoalState(currentState):
    #     
    #         
    #     for state, path, cost in problem.getSuccessors(currentState):
    #         if not currentState in visited:
    #             currentPath += path
    #             if problem.isGoalState(state):
    #                 return currentPath
    #             else:
    #                 fringe.push((state, currentPath))
    #                 visited.add(currentPath)
    #     currentState = fringe.pop()

    visited = set() # The collection of visited nodes
    fringe = util.Stack() # The collection of non-visited nodes
    pathCollection = []
    fringe.push((problem.getStartState(), pathCollection)) # Push the (0)initial state and (1)empty path into fringe
    # if problem.isGoalState(problem.getStartState()): # Check whether the initial state is the goal state.
    #     return pathCollection
    while (not fringe.isEmpty()): 
        currState, pathCollection = fringe.pop() # Follow DFS to check the last added node
        if problem.isGoalState(currState):
            return pathCollection
        elif not currState in visited:
            visited.add(currState)
            for next in problem.getSuccessors(currState):
                nextState = next[0]
                nextPath = next[1]
                if not nextState in visited:
                    # Push the (0)next state into unvisited set and (1)path from started state to next state
                    fringe.push((nextState, pathCollection + [nextPath])) 

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = set() # The collection of visited nodes
    fringe = util.Queue() # The collection of non-visited nodes
    pathCollection = []
    fringe.push((problem.getStartState(), pathCollection)) # Push the (0)initial state and (1)empty path into fringe
    # if problem.isGoalState(problem.getStartState()): # Check whether the initial state is the goal state.
    #     return pathCollection
    while (not fringe.isEmpty()): 
        currState, pathCollection = fringe.pop() # Follow BFS to check the nodes in the same layer
        if problem.isGoalState(currState):
            return pathCollection
        elif not currState in visited:
            visited.add(currState)
            for next in problem.getSuccessors(currState):
                nextState = next[0]
                nextPath = next[1]
                if not nextState in visited:
                    # Push the (0)next state into unvisited set and (1)path from started state to next state
                    fringe.push((nextState, pathCollection + [nextPath])) 

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = set() # The collection of visited nodes
    fringe = util.PriorityQueue() # The collection of non-visited nodes
    pathCollection = []
    fringe.update((problem.getStartState(), pathCollection), 0) # Push the (0)initial state, (1)empty path and (2)path cost into fringe
    # if problem.isGoalState(problem.getStartState()): # Check whether the initial state is the goal state.
    #     return pathCollection
    while (not fringe.isEmpty()): 
        currState, pathCollection = fringe.pop() # Follow UCS to check which node has the least path cost
        if problem.isGoalState(currState):
            return pathCollection
        elif not currState in visited:
            visited.add(currState)
            for next in problem.getSuccessors(currState):
                nextState = next[0]
                if not nextState in visited:
                    nextPath = next[1]
                    cost = problem.getCostOfActions(pathCollection + [nextPath])
                    # Push the (0)next state into unvisited set, (1)path from started state to next state and (2)path cost
                    fringe.update((nextState, pathCollection + [nextPath]), cost) 

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = set() # The collection of visited nodes
    fringe = util.PriorityQueue() # The collection of non-visited nodes
    pathCollection = []
    fringe.update((problem.getStartState(), pathCollection), 0) # Push the (0)initial state, (1)empty path and (2)path cost into fringe
    # if problem.isGoalState(problem.getStartState()): # Check whether the initial state is the goal state.
    #     return pathCollection
    while (not fringe.isEmpty()): 
        currState, pathCollection = fringe.pop() # Follow A* to check which node has the least path cost
        if problem.isGoalState(currState):
            return pathCollection
        elif not currState in visited:
            visited.add(currState)
            for next in problem.getSuccessors(currState):
                nextState = next[0]
                if not nextState in visited:
                    nextPath = next[1]
                    cost = problem.getCostOfActions(pathCollection + [nextPath]) + heuristic(nextState, problem)
                    # Push the (0)next state into unvisited set, (1)path from started state to next state and (2)path cost
                    fringe.update((nextState, pathCollection + [nextPath]), cost) 


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
