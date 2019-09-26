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
import searchAgents

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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    fn_custo = lambda sequencia_estados: problem.getCostOfActions([x[1] for x in sequencia_estados]) + \
                                         heuristic(sequencia_estados[-1][0], problem)
    borda = util.PriorityQueueWithFunction(fn_custo)
    explorado = []
    borda.push([(problem.getStartState(), "Stop", 0)])

    while not borda.isEmpty():
        path = borda.pop()
        s = path[len(path) - 1]
        s = s[0]
        if problem.isGoalState(s):
            return [x[1] for x in path][1:]
        if s not in explorado:
            explorado.append(s)
            for filho in problem.getSuccessors(s):
                if filho[0] not in explorado:
                    caminho_filho = path[:]
                    caminho_filho.append(filho)
                    borda.push(caminho_filho)
    return []

#     no = No(problem.getStartState(), 0, heuristic(problem.getStartState(), problem), [])
#     borda = util.PriorityQueue()
#     borda.push(no, no.custo_total)
#     explorado = {}
#     while not borda.isEmpty():
#         no = borda.pop()
#         print "Borda: " + str(borda.heap)
#         print(no)
#         explorado.setdefault(hash(no), no.getinfo())
#         print "Explorado: " + str(explorado)
#         if problem.isGoalState(no.estado):
#             print problem.getCostOfActions(no.caminho)
#             return no.caminho
#         for filho, acao, custo_acao in problem.getSuccessors(no.estado):
#             no_filho = No(filho, no.custo_caminho + custo_acao, heuristic(filho, problem), no.caminho+[acao])
#             if no_filho.estado not in borda.heap : ##and no_filho.estado not in explorado:
#                 borda.push(no_filho, no_filho.custo_total)
#             else:
#                 borda.update(no_filho, no_filho.custo_total)
#         # raw_input()
#
#     return "Erro"


# class No:
#     def __init__(self, estado, custo_caminho, custo_objetivo, caminho):
#         self.estado = estado
#         self.custo_caminho = custo_caminho
#         self.custo_objetivo = custo_objetivo
#         self.caminho = caminho
#         self.custo_total = 0
#         self.atualiza_custos()
#
#     def __repr__(self):
#         return "\nEstado: %s \nGrid:\n%s\n\nCustos:\n - Caminho: %d\n - Objetivo: %d\n - Total: %d\nCaminho: %s\n\n"\
#             % (self.estado[0], self.estado[1], int(self.custo_caminho), int(self.custo_objetivo), int(self.custo_total), self.caminho)
#
#     def __hash__(self):
#         return hash(self.estado[1])
#
#     def getinfo(self):
#         return {
#             "Estado": self.estado,
#             "Custo Total": self.custo_total,
#             "Custo Caminho": self.custo_caminho,
#             "Custo Objetivo": self.custo_objetivo,
#             "Caminho": self.caminho
#         }
#
#     def atualiza_custos(self):
#         self.custo_total = self.custo_caminho + self.custo_objetivo


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
