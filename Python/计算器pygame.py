import pygame_widgets
import pygame
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import ButtonArray

# def output():
#     print(textbox.getText())


pygame.init()
win = pygame.display.set_mode((600, 600))
#
# textbox = TextBox(win, 50, 100, 400, 50, fontSize=50,
#                   borderColour=(255, 0, 0), textColour=(0, 200, 0),
#                   onSubmit=output, radius=3, borderThickness=1)

# textbox = TextBox(win, 50, 100, 400, 50, fontSize=35, onSubmit=output)
textbox = TextBox(win, 50, 10, 500, 50, fontSize=35)
textbox.disable()

class Calculator:
    a = 0
    b = 0
    ops = 'add'
    input_stream = []
    def __init__(self):
        pass
    def input_num(self, x: str):
        pass
    def input_ops(self, x: str):
        pass
    def result(self):
        self.input_stream = []
        return 'ok'
board = [
    ['%', 'CE', 'C', '←'],
    ['1/x', 'x^2', 'sqrt', '÷'],
    ['7', '6', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['±', '0', '.', '='],
]
board_list = []
for i,j in [ (i,j) for j in range(4) for i in range(6) ]:
    board_list.append(board[i][j])

buttonArray = ButtonArray(
    win,  # Surface to place button array on
    50,  # X-coordinate
    60,  # Y-coordinate
    500,  # Width
    500,  # Height
    (4, 6),
    border=10,  # Distance between buttons and edge of array
    texts=tuple(board_list),  # Sets the texts of each button (counts left to right then top to bottom)
    # When clicked, print number
    # onClicks=(lambda: print('1'), lambda: print('2'), lambda: print('3'), lambda: print('4'))
)

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    win.fill((255, 255, 255))

    pygame_widgets.update(events)
    pygame.display.update()