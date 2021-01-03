import os
import random

import cherrypy

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""

class Coordinates(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getMagnitude(self, other):
        len_x = other.x - self.x
        len_y = other.y - self.y
        mag = len_x**2 + len_y**2
        mag = mag**0.5
        return mag

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        print (self.x, self.y)    

class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "Tai",  # TODO: Your Battlesnake Username
            "color": "#9d03fc",  # TODO: Personalize
            "head": "shac-caffeine",  # TODO: Personalize
            "tail": "freckled",  # TODO: Personalize
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        data = cherrypy.request.json
        print("START")
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        moves = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
        data = cherrypy.request.json
        board = Coordinates(data['board']['height'], data['board']['width'])
        move = moves[0]
        head = Coordinates(data['head']['x'], data['head'], ['y'])
        print (head)
        if head.getX() == (board.getX() - 1):
            moves['up'] = -1
        if head.getX() == 0:
            moves['down'] = -1
        if head.getY() == board.getY() - 1:
            moves['right'] = -1
        if head.getY() == 0:
            moves['left'] = -1
        # Choose a random direction to move in
        #possible_moves = ["up", "down", "left", "right"]
        #move = random.choice(possible_moves)
        return max(moves.values())
        #print(f"MOVE: {move}")

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json

        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
