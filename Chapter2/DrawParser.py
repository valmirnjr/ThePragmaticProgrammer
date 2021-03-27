# Exercise 4
import os

class Pen:
  def __init__(self, id):
    self.id = id
    self.position = {
      'x': 0,
      'y': 0,
      'z': 1
    }

class GraphicSystem:
  def __init__(self):
    self.pens = {}
    self.current_pen = Pen(0)

  def selectPen(self, pen_id):
    self.current_pen = self.pens.setdefault(pen_id, Pen(pen_id))
  
  def movePenDown(self):
    self.current_pen.position['z'] = 0
    print('Moved down')
  
  def movePenUp(self):
    self.current_pen.position['z'] = 1
    print('Moved up')
  
  def movePenNorth(self, dist):
    self.current_pen.position['y'] += dist
    print('Moved North')

  def movePenSouth(self, dist):
    self.current_pen.position['y'] -= dist
    print('Moved South')
  
  def movePenEast(self, dist):
    self.current_pen.position['x'] += dist
    print('Moved East')

  def movePenWest(self, dist):
    self.current_pen.position['x'] -= dist
    print('Moved West')

  def execute(self, command, arg):
    if arg:
      command(self, int(arg))
    else:
      command(self)

  def getPositionOfPen(self, pen_id=None):
    if pen_id:
      return self.pens[pen_id].position
    return self.current_pen.position

class Parser:
  def __init__(self):
    self.command_dict = {
      'P': GraphicSystem.selectPen,
      'D': GraphicSystem.movePenDown,
      'W': GraphicSystem.movePenWest,
      'N': GraphicSystem.movePenNorth,
      'E': GraphicSystem.movePenEast,
      'S': GraphicSystem.movePenSouth,
      'U': GraphicSystem.movePenUp
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
    [command_code, argument, *rest] = command.split(' ')

    return (self.command_dict[command_code], argument)
  
if __name__ == '__main__':
  parser = Parser()
  gs = GraphicSystem()

  for command in parser.readFile():
    func, arg = parser.parse(command)
    gs.execute(func, arg)
    print(gs.getPositionOfPen())
    