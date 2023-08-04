
#-----Statement of Authorship----------------------------------------#
#
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 12323
student_name   = "Lea"
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the online video instructions for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts
#  and you will submit your final solution as this single Python 3
#  file only, whether or not you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
if isfile('assignment_1_config.py'):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print("\nCannot find file 'assignment_1_config.py', aborting!\n")
    abort()

# Define the function for generating data sets, using the
# imported raw data generation function if available, but
# otherwise creating a dummy function that just returns an
# empty list
if isfile('assignment_1_data_source.py'):
    print('Data generation module found ...\n')
    from assignment_1_data_source import raw_data
    def data_set(new_seed = randint(0, 99999)):
        print('Using random number seed', new_seed, '...\n')
        seed(new_seed) # set the seed
        return raw_data() # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.
#

# All of your code goes in, or is called from, this function.
# Make sure that your code does NOT call function data_set (or
# raw_data) because it's already called in the main program below.

# Draw an arc
def arc(turtle, radius, direction, angle):
    arc_length = 2 * 3.1415 * angle * radius / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        turtle.forward(step_length)
        if direction == 'left':
            turtle.left(step_angle)
        elif direction == 'right':
            turtle.right(step_angle)
            
# Display a message on top of the grid
def display_message(message):
    goto(0, 0.5 * window_height-cell_side)
    write(message, align='center', font=coord_font)
    
# Write the description for each of the 6 demonstrated moves
def set_desc(x,y,desc):
    goto(x, y - 0.65 * cell_width)
    write(desc, align='center', font=(40))
        
# Create 2 mirrored images of the shark to correctly display its
# movements on canvas
def create_shark_turtle():
    speed('fastest')
    tracer(False)
    hideturtle()
    
    hex_start_x = -(cell_side / 2)
    hex_start_y = cell_height / 2
        
    test_shark = Turtle()
    test_shark.penup()
    
    # Make the mirrored image of the shark
    test_shark.shapetransform(-1, 0, 0, 1)
    
    # Start drawing... 
    # Upper fin
    test_shark.goto(hex_start_x, 5)
    test_shark.fillcolor('#127891')
    test_shark.pensize(1)
    test_shark.begin_fill()
    test_shark.begin_poly()
    test_shark.pendown()
    test_shark.left(20)
    arc(test_shark, 40, 'right', 30)
    test_shark.left(110)
    arc(test_shark, 40, 'right', 30)
    test_shark.left(135)
    arc(test_shark, 70, 'left', 30)
    arc(test_shark, 2, 'left', 150)
    test_shark.goto(hex_start_x, 5)
    test_shark.end_poly()
    test_shark.end_fill()
    upper_fin = test_shark.get_poly()
    register_shape("upper_fin", upper_fin)
    test_shark.shape("upper_fin")
    upper_fin_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    test_shark.penup()
    
    # Lower Fin 1
    test_shark.goto(hex_start_x + 45, hex_start_y - 40)
    test_shark.fillcolor('#0E5E72')
    test_shark.pensize(1)
    test_shark.pendown()
    test_shark.begin_fill()
    test_shark.begin_poly()
    test_shark.left(25)
    arc(test_shark, 50, 'left', 10)
    test_shark.left(45)
    arc(test_shark, 2, 'left', 150)
    test_shark.right(45)
    test_shark.forward(10)
    test_shark.goto(hex_start_x + 45, hex_start_y - 40)
    test_shark.end_poly()
    test_shark.end_fill()
    lower_fin1 = test_shark.get_poly()
    register_shape("lower_fin1", lower_fin1)
    test_shark.shape("lower_fin1")
    lower_fin1_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    test_shark.penup()

    # Lower body
    test_shark.goto(hex_start_x + 20, hex_start_y - 5)
    test_shark.fillcolor('white')
    test_shark.pensize(1)
    test_shark.pendown()
    test_shark.begin_fill()
    test_shark.begin_poly()
    test_shark.right(45)
    arc(test_shark, 100, 'right', 10)
    test_shark.left(25)
    test_shark.forward(15)
    test_shark.right(40)
    arc(test_shark, 25, 'right', 70)
    test_shark.left(10)
    arc(test_shark, 25, 'left', 75)
    test_shark.setheading(180)
    test_shark.forward(10)
    test_shark.goto(hex_start_x + 20, hex_start_y - 5)
    test_shark.end_poly()
    test_shark.end_fill()
    lower_body = test_shark.get_poly()
    register_shape("lower_body", lower_body)
    test_shark.shape("lower_body")
    lower_body_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    test_shark.penup()
    
    # Lower Fin 2
    test_shark.goto(hex_start_x + 35, hex_start_y - 45)
    test_shark.fillcolor('#189BBC')
    test_shark.pensize(1)
    test_shark.pendown()
    test_shark.begin_fill()
    test_shark.begin_poly()
    test_shark.left(45)
    arc(test_shark, 15, 'left', 30)
    test_shark.right(70)
    arc(test_shark, 10, 'right', 13)
    test_shark.right(50)
    arc(test_shark, 50, 'right', 30) 
    arc(test_shark, 1, 'right', 180)
    test_shark.goto(hex_start_x + 35, hex_start_y - 45)
    test_shark.end_poly()
    test_shark.end_fill()
    lower_fin2 = test_shark.get_poly()
    register_shape("lower_fin2", lower_fin2)
    test_shark.shape("lower_fin2")
    lower_fin2_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    test_shark.penup()
 
    # Upper body
    test_shark.goto(hex_start_x + 20, hex_start_y - 5)
    test_shark.fillcolor('#1693B3')
    test_shark.pensize(1)
    test_shark.pendown()
    test_shark.begin_fill()
    test_shark.begin_poly()
    test_shark.left(-110)
    arc(test_shark, 100, 'left', 20)
    arc(test_shark, 75, 'left', 30)
    arc(test_shark, 2, 'right', 80)
    test_shark.forward(20)
    arc(test_shark, 2, 'left', 165)
    test_shark.forward(20)
    arc(test_shark, 2, 'right', 40)
    test_shark.forward(15)
    arc(test_shark, 2, 'left', 160)
    test_shark.forward(15)
    test_shark.left(15)
    arc(test_shark, 10, 'right', 130)
    test_shark.left(75)
    arc(test_shark, 2, 'left', 150)
    test_shark.right(150)
    arc(test_shark, 2, 'right', 150)
    test_shark.left(90)
    test_shark.forward(5)
    test_shark.left(35)
    arc(test_shark, 45, 'left', 10)
    test_shark.right(25)
    arc(test_shark, 50, 'left', 10)
    test_shark.right(45)
    test_shark.forward(7)
    test_shark.left(140)
    test_shark.forward(5)
    test_shark.right(70)
    test_shark.forward(1)
    arc(test_shark, 3, 'left', 110)
    test_shark.right(45)
    test_shark.forward(8)
    test_shark.right(45)
    test_shark.forward(10)
    test_shark.setheading(90)
    test_shark.forward(5)
    test_shark.goto(hex_start_x + 20, hex_start_y - 5)
    test_shark.end_poly()
    test_shark.end_fill()
    upper_body = test_shark.get_poly()
    register_shape("upper_body", upper_body)
    test_shark.shape("upper_body")
    upper_body_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.penup()
    
    # Eye
    test_shark.goto(hex_start_x + 20, hex_start_y - 30 + 5)
    test_shark.fillcolor('yellow')
    test_shark.pensize(1)
    test_shark.pendown()
    test_shark.begin_fill()
    test_shark.begin_poly()
    test_shark.setheading(90)
    test_shark.forward(8)
    test_shark.right(100)
    arc(test_shark, 6, 'right', 170)
    test_shark.goto(hex_start_x + 20, hex_start_y - 25)
    test_shark.end_poly()
    test_shark.end_fill()
    eye1 = test_shark.get_poly()
    register_shape("eye1", eye1)
    test_shark.shape("eye1")
    eye1_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    test_shark.penup()

    test_shark.goto(hex_start_x + 21, hex_start_y - 21)
    test_shark.fillcolor('black')
    test_shark.pensize(1)
    test_shark.pendown()
    test_shark.begin_fill()
    test_shark.begin_poly()
    arc(test_shark, 2, 'right', 360)
    test_shark.end_poly()
    test_shark.end_fill()
    eye2 = test_shark.get_poly()
    register_shape("eye2", eye2)
    test_shark.shape("eye2")
    eye2_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    test_shark.penup()
    
    # Nose
    test_shark.goto(hex_start_x + 23, hex_start_y - 13)
    test_shark.fillcolor('gray')
    test_shark.color('gray')
    test_shark.pensize(1)
    test_shark.pendown()
    test_shark.begin_fill()
    test_shark.begin_poly()
    arc(test_shark, 1, 'right', 360)
    test_shark.end_poly()
    test_shark.end_fill()
    nose = test_shark.get_poly()
    register_shape("nose", nose)
    test_shark.shape("nose")
    nose_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    test_shark.penup()
    
    # Mouth
    test_shark.goto(hex_start_x + 30, hex_start_y - 17)
    test_shark.color('black')
    test_shark.pensize(1)
    test_shark.pendown()
    test_shark.begin_poly()
    test_shark.right(80)
    arc(test_shark, 180, 'left', 2)
    test_shark.penup()
    test_shark.left(180)
    arc(test_shark, 180, 'right', 2)
    test_shark.end_poly()
    mouth = test_shark.get_poly()
    register_shape("mouth", mouth)
    test_shark.shape("mouth")
    mouth_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    
    # Gill1
    test_shark.goto(hex_start_x + 18, hex_start_y - 35)
    test_shark.color('#0F697F')
    test_shark.pensize(2)
    test_shark.pendown()
    test_shark.begin_poly()
    test_shark.left(10)
    arc(test_shark, 20, 'right', 45)
    test_shark.penup()
    test_shark.goto(hex_start_x + 18, hex_start_y - 35)
    test_shark.end_poly()
    gill1 = test_shark.get_poly()
    register_shape("gill1", gill1)
    test_shark.shape("gill1")
    gill1_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    
    # Gill2
    test_shark.goto(hex_start_x + 19, hex_start_y - 39)
    test_shark.pendown()
    test_shark.begin_poly()
    test_shark.left(10)
    arc(test_shark, 20, 'right', 35)
    test_shark.penup()
    test_shark.goto(hex_start_x + 19, hex_start_y - 39)
    test_shark.end_poly()
    gill2 = test_shark.get_poly()
    register_shape("gill2", gill2)
    test_shark.shape("gill2")
    gill2_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    
    # Gill3
    test_shark.goto(hex_start_x + 20, hex_start_y - 43)
    test_shark.pendown()
    test_shark.begin_poly()
    test_shark.left(10)
    arc(test_shark, 20, 'right', 22)
    test_shark.penup()
    test_shark.goto(hex_start_x + 20, hex_start_y - 43)
    test_shark.end_poly()
    gill3 = test_shark.get_poly()
    register_shape("gill3", gill3)
    test_shark.shape("gill3")
    gill3_2 = test_shark.get_shapepoly()
    test_shark.shape("classic")
    test_shark.setheading(0)
    
    # Clear after drawing
    test_shark.clear()
    test_shark.hideturtle()
    
    # Create a compound shape of our shark and its mirrored image
    shark = Shape("compound")
    shark.addcomponent(upper_fin, "#127891", '#0B4C5B')
    shark.addcomponent(lower_fin1, "#0E5E72", '#0B4C5B')
    shark.addcomponent(lower_body, "white", '#0B4C5B')
    shark.addcomponent(upper_body, "#1693B3", '#0B4C5B')
    shark.addcomponent(eye1, "yellow", '#0B4C5B')
    shark.addcomponent(eye2, "black", 'black')
    shark.addcomponent(lower_fin2, "#189BBC", '#0B4C5B')
    shark.addcomponent(nose, "gray", 'gray')
    shark.addcomponent(mouth, "black", 'black')
    shark.addcomponent(gill1, "#0F697F", '#0B4C5B')
    shark.addcomponent(gill2, "#0F697F", '#0B4C5B')
    shark.addcomponent(gill3, "#0F697F", '#0B4C5B')
    
    shark2 = Shape("compound")
    shark2.addcomponent(upper_fin_2, "#127891", '#0B4C5B')
    shark2.addcomponent(lower_fin1_2, "#0E5E72", '#0B4C5B')
    shark2.addcomponent(lower_body_2, "white", '#0B4C5B')
    shark2.addcomponent(upper_body_2, "#1693B3", '#0B4C5B')
    shark2.addcomponent(eye1_2, "yellow", '#0B4C5B')
    shark2.addcomponent(eye2_2, "black", 'black')
    shark2.addcomponent(lower_fin2_2, "#189BBC", '#0B4C5B')
    shark2.addcomponent(nose_2, "gray", 'gray')
    shark2.addcomponent(mouth_2, "black", 'black')
    shark2.addcomponent(gill1_2, "#0F697F", '#0B4C5B')
    shark2.addcomponent(gill2_2, "#0F697F", '#0B4C5B')
    shark2.addcomponent(gill3_2, "#0F697F", '#0B4C5B')
    
    return shark, shark2

# Calculate the new shark position
def get_new_pos(x, y):
    goto(x, y)
    forward(cell_height) 
    x_new, y_new = pos()
   
    return round(x_new), round(y_new)

# Move the shark  
def make_move(shark_type, direction, x, y):
    if x == 0 and y == 0:
        # Speed up the drawing of move #0
        speed('fastest')
    else:
        # How fast each move of the shark appears on canvas
        delay(200)
        speed('slowest')
    
    # Draw the shark moves one by one
    tracer(True)
    
    # Draw hexagon
    goto(x, y)
    shape(shark_type)
    draw_hexagon(x, y)

    # Draw the shark itself
    goto(x, y)
    if direction == 150:
        # Correction of the angle for "West" direction
        setheading(direction+30)
        stamp()
        setheading(direction)
    else:
        setheading(direction)
        stamp()
        
    speed('fastest')
    
def draw_hexagon(x, y):
    speed('slowest')
    tracer(False)
    goto(x-cell_side/2, y+cell_height/2)
    setheading(0)
    fillcolor('#00FFFF')
    begin_fill()
    for border in range(6):
        pensize(2)
        pendown()
        forward(60)
        left(300)
        penup()
    end_fill()
    
# Display 6 possible shark moves (canvas legend)
def display_shark_moves(shark_moves):
    speed('fastest')
    tracer(False)
    angle = 90
    
    for direction in shark_moves:
        x = 6 * horiz_spacing
        y = 1.5 * cell_height
 
        setheading(angle)
        if direction=='North':
            x = -x
            shape("Shark1")
            angle -= 60
        elif direction=='North east':
            x = -x
            y = 0
            angle -= 60
        elif direction=='South east':    
            x = -x
            y = -y
            angle -= 60
        elif direction=='South':  
            shape("Shark2")
            angle -= 60
        elif direction=='South west':  
            y = 0
            angle -= 30
        elif direction=='North west':  
            y = -y
            angle -= 60
            direction='West'
    
        set_desc(x, y, direction)
        get_heading = heading()
        draw_hexagon(x, y)
        setheading(get_heading)
        goto(x, y)
        stamp()
        penup()
              
def visualise_data(data_set):
    # Possible shark moves
    shark_moves = [
        'North', 
        'North east',
        'South east',
        'South',
        'South west',
        'North west'
    ]
    
    # Create 2 mirrored shapes of the shark
    shark1, shark2 = create_shark_turtle()
    register_shape("Shark1", shark1)
    register_shape("Shark2", shark2)
     
    # Draw its 6 possible moves
    display_shark_moves(shark_moves)
    
    moves = [
        [90, "Shark1"],
        [30, "Shark1"],
        [-30, "Shark1"],
        [270, "Shark2"],
        [210, "Shark2"],
        [150, "Shark2"]
    ]
    
    special_cell_centers = [
        [270, 52],
        [-90, 156],
        [-360, -104]
    ]
    
    # Look into the generated dataset
    generated_moves = len(data_set) - 1
    moves_available = data_set[0][1]
    init_move = data_set[0][2]
    
    if moves_available < generated_moves:
        num_of_moves = moves_available
        msg = "The shark is resting after move "+str(num_of_moves) 
    else:
        num_of_moves = generated_moves
        msg = "The shark ran out of moves ("+str(num_of_moves)+")"

    # Processing each move
    for move in data_set:
        # Not allowed to make anymore moves, exiting..
        if move[0] > data_set[0][1]:
            display_message(msg)
            break

        # Don't move forward if this is the initial move
        if move[0] == 0:
            ind = shark_moves.index(move[2])
            x_new = 0
            y_new = 0
            
            make_move(moves[ind][1], moves[ind][0], 0, 0)
            # If this is also the only move
            if generated_moves == 0:
                display_message(msg)
            continue

        # Decide which move is next (get index)
        # and get the next position
        if move[1] == 'Move forward':
            ind = ind
        elif move[1] == 'Move & turn left':
            ind = (ind - 1) % 6
        elif move[1] == 'Move & turn right':
            ind = (ind + 1) % 6
            
        x_new, y_new = get_new_pos(x_new, y_new)    
        
        # Check for special cells
        if (special_cell_centers[0] == [int(x_new),int(y_new)]
                or special_cell_centers[1] == [int(x_new),int(y_new)]
                or special_cell_centers[2] == [int(x_new),int(y_new)]):
            make_move(moves[ind][1], moves[ind][0], x_new, y_new)
            display_message('The shark just caught something!')
            break
        
        # The shark is out of the grid
        if (abs(x_new) >= abs(horiz_spacing * grid_width / 2) 
                or abs(y_new) > abs(cell_height * 2)):
            undo()
            display_message('The shark swam away in move '+str(move[0]))
            break
         
        # If all checks are passed, move the shark forward
        make_move(moves[ind][1], moves[ind][0], x_new, y_new)

        # If this is also its last move
        if move[0] == data_set[0][1]:
            display_message(msg)
            break
           
#--------------------------------------------------------------------#



#-----Main Program to Run Student's Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas()

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#
