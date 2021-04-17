from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
slug = [ [2,4], [3,4], [4,4] ]
white = (255,255,255)
direction = "down"
blank = (0,0,0)
hmm = "hmm"

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
    
sense.clear()
draw_slug()

yes = "yes"

while yes == "yes":
    move()
    sleep(0.5)


