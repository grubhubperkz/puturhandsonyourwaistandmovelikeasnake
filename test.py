from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()
slug = [ [2,4], [3,4], [4,4] ]
white = (255,255,255)
mystery = (0,0,255)
red = (255,0,0)
direction = "down"
blank = (0,0,0)
hmm = "hmm"
score = 0
count = 1
time = 0.5
flag = 0
def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], white)
        
def do_thing(event):
    global direction
    if event.action == 'pressed':
        print('you pressed me -_-')
        if event.direction == 'up':
            direction = "up"
        elif event.direction == 'down':
            direction = "down"
        elif event.direction == "left":
            direction = "left"
        elif event.direction == "right":
            direction = "right"
        print(direction)
            

def move():
    
    global score
    print(direction)
    last = slug[-1]
    first = slug[0]
    next = list(last)
    sense.stick.direction_any = do_thing        

    if direction == "right":
        if last[0] + 1 == 8:
            next [0] = 0
        else:
            next[0] = last[0] + 1
    elif direction == "left":
        if last[0] - 1 == -1:
            next[0] = 7
        else:
            next[0] = last[0] - 1
            
    elif direction == "down":
        if last[1] + 1 == 8:
            next[1] = 0
        else:
            next[1] = last[1] + 1
            
    elif direction == "up":
        if last[1] - 1 == -1:
            next [1] = 7
        else:
            next[1] = last[1] -1
    slug.append(next)
    print(next)
    sense.set_pixel(next[0], next[1], white)
    
    sense.set_pixel(first[0], first[1], blank)
    
    slug.remove(first)
    
    if next in vegetables:
        vegetables.remove(next)
        score +=1
    if score == 15:
        score = 0
        levelUp()
    if next in bomb:
        bomb.remove(next)
        gameOver()
vegetables = []
bomb = []
def levelUp():
    global count
    sense.clear()
    sense.show_message("LEVEL UP")
    count = count +1
    draw_slug()

    
def makeVeg():
    new = slug [0]

    while new in slug:
        x = randint(0,7)
        y = randint(0,7)
        new = [x,y]
        sense.set_pixel(x,y, mystery)
        vegetables.append ([x,y])

def nono():
    no = slug [0]
    
    while no in slug:
        x = randint(0,7)
        y = randint(0,7)
        no = [x,y]
        sense.set_pixel(x,y, red)
        bomb.append ( [x,y] )

def gameOver():
    sense.clear()
    sense.show_message("GAME OVER")
    global flag
    flag = 1
    sense.clear()
sense.clear()
draw_slug()

yes = "yes"

while flag == 0:
    move()
    speed = time / count
    sleep(speed)
    if len(vegetables) < 4:
        makeVeg()
    if len(bomb) < 2:
        nono()

