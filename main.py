from tkinter import *

from models.snake_class import Snake
from models.food_class import Food
from settings import SETTINGS

def next_turn(snake, food):
    global direction
    global new_direction

    #CHANGE DIRECTION
    if new_direction.get() == 'left':
        if direction != 'right':
            direction = 'left'
    elif new_direction.get() == 'right':
        if direction != 'left':
            direction = 'right'
    elif new_direction.get() == 'up':
        if direction != 'down':
            direction = 'up'
    elif new_direction.get() == 'down':
        if direction != 'up':
            direction = 'down'

    #MOVE TO CURRENT DIRECTION
    if direction == 'up':
        snake.go_up()
    elif direction == 'down':
        snake.go_down()
    elif direction == 'left':
        snake.go_left()
    elif direction == 'right':
        snake.go_right()

    snake.squares.insert(0, canvas.create_rectangle(snake.coordinates[0][0], snake.coordinates[0][1], snake.coordinates[0][0] + SETTINGS.SPACE_SIZE, snake.coordinates[0][1] + SETTINGS.SPACE_SIZE, fill=SETTINGS.SNAKE_COLOR))

    #SNAKE EAT FOOD
    if snake.coordinates[0][0] == food.coordinates[0] and  snake.coordinates[0][1] == food.coordinates[1]:
        global score
        score += 5
        label.config(text="Score:{}".format(score))
        
        canvas.delete('food')
        food = Food(SETTINGS.SPACE_SIZE, SETTINGS.GAME_WIDTH, SETTINGS.GAME_HEIGHT) #CREATE A FOOD
        canvas.create_oval(food.coordinates[0], food.coordinates[1], food.coordinates[0] + SETTINGS.SPACE_SIZE, food.coordinates[1] + SETTINGS.SPACE_SIZE, fill=SETTINGS.FOOD_COLOR, tag='food')
    else:
        #DELETE LAST PART OF SNAKE
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        
    if check_collision(snake):
        game_over()
    else:
        window.after(SETTINGS.SPEED, next_turn, snake, food)

def check_collision(snake):
    #COLLISION WITH THE WALL
    if snake.coordinates[0][0] < 0 or snake.coordinates[0][0] >= SETTINGS.GAME_WIDTH:
        return True
    if snake.coordinates[0][1] < 0 or snake.coordinates[0][1] >= SETTINGS.GAME_HEIGHT:
        return True
    
    #COLLISION WITH THE WALL
    for body_part in snake.coordinates[1:]:
        if snake.coordinates[0][0] == body_part[0] and snake.coordinates[0][1] == body_part[1]:
            return True
    
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), 
                       text="GAME OVER", fill="red", tag='gameover' )

#GAME LAYOUT CONFIGURATION
window = Tk()
window.title('Snake game')
window.resizable(False, False)

score = 0

new_direction = StringVar(window)
new_direction.set('down')
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=SETTINGS.BACKGROUND_COLOR, width=SETTINGS.GAME_WIDTH, 
                height=SETTINGS.GAME_HEIGHT)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<a>', lambda event: new_direction.set('left'))
window.bind('<d>', lambda event: new_direction.set('right'))
window.bind('<w>', lambda event: new_direction.set('up'))
window.bind('<s>', lambda event: new_direction.set('down'))
window.bind('<Left>', lambda event: new_direction.set('left'))
window.bind('<Right>', lambda event: new_direction.set('right'))
window.bind('<Up>', lambda event: new_direction.set('up'))
window.bind('<Down>', lambda event: new_direction.set('down'))

snake = Snake(SETTINGS.SPACE_SIZE, SETTINGS.BODY_PARTS) #CREATE A SNAKE
for x, y in snake.coordinates:
    snake.squares.append(canvas.create_rectangle(x, y, x + SETTINGS.SPACE_SIZE, 
                                                 y+SETTINGS.SPACE_SIZE, fill=SETTINGS.SNAKE_COLOR, 
                                                 tag='snake'))

food = Food(SETTINGS.SPACE_SIZE, SETTINGS.GAME_WIDTH, SETTINGS.GAME_HEIGHT) #CREATE A FOOD
canvas.create_oval(food.coordinates[0], food.coordinates[1], 
                   food.coordinates[0] + SETTINGS.SPACE_SIZE, 
                   food.coordinates[1] + SETTINGS.SPACE_SIZE, 
                   fill=SETTINGS.FOOD_COLOR, 
                   tag='food')

next_turn(snake, food)

window.mainloop()


