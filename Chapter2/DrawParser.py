# Exercise 4
from turtle import *
import os
import re

class Pen:
  def __init__(self, id, color='black', speed=5):
    self.id = id
    self.turtle = Turtle()
    self.turtle.up()
    self.turtle.speed(speed)

  def __eq__(self, other):
    return self.id == other.id

  def __hash__(self):
    return hash(self.id)

class GraphicSystem:
  def __init__(self):
    self.pens = {}
    self.current_pen = Pen(0)
    self.screen = getscreen()

  def selectPen(self, pen_id):
    self.current_pen = self.pens.setdefault(pen_id, Pen(pen_id))
  
  def movePenDown(self):
    self.current_pen.turtle.down()
    print('Moved down')
  
  def movePenUp(self):
    self.current_pen.turtle.up()
    self.current_pen.turtle.hideturtle()
  
  def movePenWithAngle(self, angle, dist):
    self.current_pen.turtle.setheading(angle)
    self.current_pen.turtle.forward(dist)

  def movePenNorth(self, dist):
    self.current_pen.turtle.setheading(90)
    self.current_pen.turtle.forward(dist)
    print('Moved North')

  def movePenSouth(self, dist):
    self.current_pen.turtle.setheading(270)
    self.current_pen.turtle.forward(dist)
    print('Moved South')
  
  def movePenEast(self, dist):
    self.current_pen.turtle.setheading(180)
    self.current_pen.turtle.forward(dist)
    print('Moved East')

  def movePenWest(self, dist):
    self.current_pen.turtle.setheading(0)
    self.current_pen.turtle.forward(dist)
    print('Moved West')

  def execute(self, command, args):
    if args:
      command(self, args)
    else:
      command(self)

  def getPositionOfPen(self, pen_id=None):
    if pen_id:
      return self.pens[pen_id].turtle.position
    return self.current_pen.turtle.position

  def holdScreen(self):
    self.screen.exitonclick()

  def setPosition(self, position):
    self.current_pen.turtle.goto(position)

  def drawPoint(self, diameter=2):
    self.current_pen.turtle.dot()

class Parser:
  def __init__(self):
    self.command_dict = {
      'P': GraphicSystem.selectPen,
      'D': GraphicSystem.movePenDown,
      'W': GraphicSystem.movePenWest,
      'N': GraphicSystem.movePenNorth,
      'E': GraphicSystem.movePenEast,
      'S': GraphicSystem.movePenSouth,
      'U': GraphicSystem.movePenUp,
      'SP': GraphicSystem.setPosition,
      'DP': GraphicSystem.drawPoint
    }

  def readFile(self, filename=None):
    if not filename:
      script_dir = os.path.dirname(__file__)
      relative_path = 'drawCommands.txt'
      filename = os.path.join(script_dir, relative_path)
    
    with open(filename) as f:
      commands = f.readlines()
      
    return commands

  def parse(self, command):
    [command_without_comment, *comment] = re.split('#', command, maxsplit=1)
    
    [command_code, *args] = command_without_comment.split()

    if len(args) == 1:
      return (self.command_dict[command_code], int(args[0]))
      
    if len(args) > 1:
      args = (int(arg) for arg in args)

    return (self.command_dict[command_code], args)
  
if __name__ == '__main__':
  parser = Parser()
  gs = GraphicSystem()

  for command in parser.readFile():
    if not command.isspace():
      func, args = parser.parse(command)
      gs.execute(func, args)
      print(gs.getPositionOfPen())

  gs.holdScreen()
  