# ######################################################
# # Project: Project 2
# # UIN: 654360057
# # repl.it URL: <address to your repl.it for the project>

# # For this project, I received help from the following members of CS111.
# # Student1name, netID 12345678: help with background loop
# # Colin Cazho, netID: ccazh2: help with collision


# ######################################################
#### imports
import turtle
import math
import random

#### variables

s = turtle.Screen()
t2 = turtle.Turtle()
s.setup(width= 300, height = 300)
w, h = s.screensize()
s.tracer(0)
speed = 50
game_objects = [
  {"t" : turtle.Turtle(),"x":0, "y":-125, "radius": 10, "image":"rocket.gif", "type":"rocket"}, 
  {"t" : turtle.Turtle(),"x":50, "y":25, "radius": 10, "image":"asteroid.gif", "type":"asteroid"}, 
  {"t" : turtle.Turtle(),"x":100, "y":75, "radius": 10, "image":"asteroid2.gif", "type":"asteroid2"},
  {"t" : turtle.Turtle(),"x":10, "y":-25, "radius": 10, "image":"asteroid2.gif", "type":"asteroid2"},
  {"t" : turtle.Turtle(),"x":-50, "y":-75, "radius": 10, "image":"asteroid.gif", "type":"asteroid"},
  {"t" : turtle.Turtle(),"x":random.randint(-125,125), "y":125, "radius": 10, "image":"dest.gif", "type":"destin"}
  
]
t = game_objects[0]["t"]

#### key press functions

def up():
    t.setheading(90)
    t.forward(50)

    game_objects[0]["y"] += speed

    if game_objects[0]["y"] > h/2:
      game_objects[0]["y"] = -h/2

      x = game_objects[0]["x"]
      y = game_objects[0]["y"]

      t.goto(x,y)
    

              
def down():
  t.setheading(-90)
  t.forward(15)

  game_objects[0]["y"] -= speed

  if game_objects[0]["y"] < -h/2:
    game_objects[0]["y"] = -h/2

    x = game_objects[0]["x"]
    y = game_objects[0]["y"]

    t.goto(x,y)

def left():
  t.setheading(180)
  t.forward(15)

  game_objects[0]["x"] -= speed

  if game_objects[0]["x"] < -w/2:
    game_objects[0]["x"] = w/2

    x = game_objects[0]["x"]
    y = game_objects[0]["y"]

    t.goto(x,y)
def right():
  t.setheading(0)
  t.forward(15)

  game_objects[0]["x"] += speed

  if game_objects[0]["x"] > w/2:
    game_objects[0]["x"] = -w/2

    x = game_objects[0]["x"]
    y = game_objects[0]["y"]

    t.goto(x,y)


s.onkey(up, "Up")
s.onkey(down, "Down")
s.onkey(left, "Left")
s.onkey(right, "Right")
s.listen()

lives = 3
score = 0
level = 0
sped = 0.1

def main():
  ###### start screen code
  game_state = "start screen"
  s.bgcolor('grey')
  if game_state == "start screen":
    t2.clear()
    t2.color("white")
    t2.pensize()
    t2.goto(-100, 0)
    t2.hideturtle()
    t2.write("Press Spacebar. Reach star to advance", align="Left",font= ("Arial", 8))
  
  game_state = "over screen"
  s.bgcolor('grey')
  if game_state == "over screen":
    t2.clear()
    t2.color("white")
    t2.pensize()
    t2.goto(-100, 0)
    t2.hideturtle()
    t2.write("Press Spacebar. Reach star to advance", align="Left",font= ("Arial", 8))


  def start():
    playscreen()


      
  s.onkey(start, " ")
  s.listen()
 
    # game_state = "game over screen"
    # s.bgcolor('grey')
    # if game_state == "game over screen":
    #   t2.clear()
    #   t2.color("red")
    #   t2.pensize()
    #   t2.goto(-100, 0)
    #   t2.hideturtle()
    #   t2.write("Game over", font= ("Arial", 20))

  def playscreen():
    game_state == "play"
    t2.clear()
    s.bgpic("background.gif")

    for obj in game_objects:
      s.addshape(obj["image"])
      obj["t"].shape(obj["image"])
    t3 = turtle.Turtle()
    t3.penup()
    t3.hideturtle()
    t3.goto(-130, 120 )
    t3.color('white')
    

    t4 = turtle.Turtle()
    t4.penup()
    t4.hideturtle()
    t4.goto(60, 120)
    t4.color('white')

    t_level = turtle.Turtle()
    t_level.penup()
    t_level.hideturtle()
    t_level.goto(-30,120)
    t_level.color('white')

  ###### collision

    def collision():
      global lives
      global score 
      global level
      global sped
      distance1 = math.sqrt((math.pow(game_objects[0]["x"] - game_objects[1]["x"], 2)) + (math.pow(game_objects[0]["y"] - game_objects[1]["y"], 2)))
      
      distance2 = math.sqrt((math.pow(game_objects[0]["x"] - game_objects[2]["x"], 2)) + (math.pow(game_objects[0]["y"] - game_objects[2]["y"], 2)))

      distance3 = math.sqrt((math.pow(game_objects[0]["x"] - game_objects[3]["x"], 2)) + (math.pow(game_objects[0]["y"] - game_objects[3]["y"], 2)))

      distance4 = math.sqrt((math.pow(game_objects[0]["x"] - game_objects[4]["x"], 2)) + (math.pow(game_objects[0]["y"] - game_objects[4]["y"], 2)))

      distance5 = math.sqrt((math.pow(game_objects[0]["x"] - game_objects[5]["x"], 2)) + (math.pow(game_objects[0]["y"] - game_objects[5]["y"], 2)))



      if distance1 < 27:
        x = game_objects[0]["x"] = 0
        y = game_objects[0]["y"] = -125
        t.goto(x, y)
        lives -=1
        if lives == 0:
          for obj in game_objects:
            obj["t"].clear()
      if distance2 < 27:
        x = game_objects[0]["x"] = 0
        y = game_objects[0]["y"] = -125
        t.goto(x, y)
        lives -=1
        if lives == 0:
          for obj in game_objects:
            obj["t"].clear()
      if distance3 < 27:
        x = game_objects[0]["x"] = 0
        y = game_objects[0]["y"] = -125
        t.goto(x, y)
        lives -=1
        if lives == 0:
          game_objects["t"].clear()
      if distance4 < 27:
        x = game_objects[0]["x"] = 0
        y = game_objects[0]["y"] = -125
        t.goto(x, y)
        lives -=1
        for obj in game_objects:
            obj["t"].clear()
        # game_objects["t"].clear()

###### destination object collision 

      if distance5 < 27:
        x = game_objects[0]["x"] = 0
        y = game_objects[0]["y"] = -125
        t.goto(x, y)
        game_objects[5]["x"] = random.randint(-125,125)
        game_objects[5]["y"] = 125
        score += 1
        level += 1
        sped += 0.2

####### animation loop

    while (game_state != "over"):
      t3.clear()
      t3.write("Lives:" + str(lives), font = "Arial")
      t4.clear()
      t4.write("Score:" + str(score), font = "Arial")
      t_level.clear()
      t_level.write("Level:" + str(level), font = "Arial")
      for obj in game_objects:
        obj["t"].clear()
        obj["t"].penup()

        if (obj["type"] == "asteroid"):
          obj["x"] += sped
          if obj["x"] > w/2:
            obj["x"] = -w/2
        if (obj["type"] == "asteroid2"):
          obj["x"] -= sped
          if obj["x"] < -w/2:
              obj["x"] = w/2
         
        obj["t"].goto(obj["x"], obj["y"])
      
      
      collision()
      if lives == 0:
        for obj in game_objects:
          obj["t"].clear()
          t2.write("Game Over")
        
      
      
      s.update()
      
main()

