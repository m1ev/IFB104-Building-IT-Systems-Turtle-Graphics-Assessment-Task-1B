
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



# draw color-filled hexagon in turtle
  


# First Shark
def shark1(x, y):
    speed('fastest')
    tracer(False)
    goto(x-50, y+50) # go to coordinate of hexagon

    for border in range(6):
        pensize(2)
        pendown()
        forward(60)
        left(300)
        penup()

    #Fin
    goto(x-20, y+15)
    pendown()
    color('light blue')
    begin_fill()
    forward(20) # draw base
    left(120)
    forward(20)
    left(120)
    forward(20)
    end_fill()
    penup()
    

    #Body
    goto(x-50, y+50)
    fillcolor('blue')
    setheading(200)
    backward(-20)
    setheading(300)
    forward(70)
    begin_fill()
    def body(rad):
     
      #radius of arc
      for length in range(2):
     
        # two arcs
        pendown()
        circle(rad,90)
        circle(rad//2,90)
 
    # Main section
    # tilt the shape to negative 45
    seth(-45)
 
    # calling draw method
    body(35)
    end_fill()
    penup()

    # Eyes
    pensize(3)
    setheading(-40)
    backward(50)
    setheading(-10)
    forward(70)
    pendown()
    fillcolor('red')
    begin_fill()
    circle(5)
    end_fill()
    penup()

    #mouth
    pensize(2)
    goto(-500,125)
    pendown()
    fillcolor('black')
    begin_fill()
    for _ in range(4):
        forward(15) 
        left(90)
        end_fill()
        penup()
        pendown()
        

    #scales
    goto(-510,130)
    setheading(-90)
    backward(15)
    penup()
    setheading(-20)
    forward(10)
    setheading(-20)
    pendown()
    backward(20)
    setheading(90)
    forward(10)
    setheading(-20)
    backward(8)
    penup()

    #second fin
    goto(-510,125)
    pendown()
    setheading(0)
    color('light blue')
    begin_fill()
    forward(10) 
    right(120)
    forward(10)
    right(120)
    forward(10)
    end_fill()
    penup()

    #tail
    pendown()
    goto(x-55, y+5)
    setheading(-30)
    color('black')
    begin_fill()
    forward(20) 
    right(120)
    forward(20)
    right(120)
    forward(20)
    end_fill()
    penup()

    
    
    #second_Hexagon

def second_fish(x,y):
    speed('fastest')
    tracer(False)
    goto(x-50, y+50) # go to coordinate of hexagon
    setheading(0)

    # Border Hexagon
    
    for border in range(6): 
        pensize(2)
        pendown()
        forward(60)
        left(300)
        penup()

    # second Body
    goto(x-60, y+65)
    fillcolor('blue')
    setheading(200)
    backward(-20)
    setheading(300)
    forward(100)
    begin_fill()
    def secondbody(rad):
     
      #ellipse
      for length in range(2):
        pendown()
        circle(rad,90)
        circle(rad//2,90)
        
    # tilt the shape to northeast 
    seth(-10)
 
    # calling draw method
    secondbody(35)
    end_fill()
    penup()

    #eyes for second fish
    pensize(3)
    setheading(-90)
    bk(30)
    setheading(0)
    fd(10)
    pendown()
    fillcolor('red')
    begin_fill()
    circle(5)
    end_fill()
    penup()

#Scales
    pensize(2)
    goto(-510,-35)
    setheading(-90)
    backward(15)
    penup()
    setheading(-20)
    forward(10)
    setheading(-20)
    pendown()
    backward(20)
    setheading(90)
    forward(15)
    setheading(-20)
    backward(8)
    penup()

    #second tail
    pensize(3)
    goto(x-30, y+30)
    pendown()
    setheading(-30)
    color('black')
    begin_fill()
    forward(20) 
    right(120)
    forward(20)
    right(120)
    forward(20)
    end_fill()
    penup()



   # Description for 2nd Entity

def secondfish_desc(x,y):
    penup()
    goto(x+50, y-50)
    write('North East', align = 'right', font= (40))

secondfish_desc(-530, -30)


#Third_Hexagon

def third_fish(x,y):
    speed('fastest')
    tracer(False)
    goto(x-50, y+50) # go to coordinate of hexagon
    setheading(0)

    # Border Hexagon
    
    for border in range(6): 
        pensize(2)
        pendown()
        forward(60)
        left(300)
        penup()
        
#third body
    goto(x,y-10)
    pendown()
    fillcolor('blue')
    setheading(-90)
    begin_fill()
    def thirdbody(rad):
     
      #ellipse
      for length in range(2):
        pendown()
        circle(rad,90)
        circle(rad//2,90)
        
    # tilt the shape
    seth(100)
 
    # calling draw method
    thirdbody(35)
    end_fill()
    penup()

#Third_fish description

def thirdfish_desc(x,y):
    penup()
    goto(x+50, y-50)
    write('South East', align = 'right', font= (40))

thirdfish_desc(-530, -180)
    
#Fourth_Hexagon
def fourth_fish(x,y):
    speed('fastest')
    tracer(False)
    goto(x-50, y+50) 
    setheading(0)

    #Border Hexagon
    
    for border in range(6): 
        pensize(2)
        pendown()
        forward(60)
        left(300)
        penup()

    #fourth body
    goto(x-30,y+20)
    pendown()
    fillcolor('blue')
    setheading(-90)
    begin_fill()
    def fourthbody(rad):
     
      #ellipse
      for n in range(2):
        pendown()
        circle(rad,90)
        circle(rad//2,90)
        
    # tilt the shape
    seth(225)
 
    # calling draw method
    fourthbody(35)
    end_fill()
    penup()

    #eyes for fourth fish
    pensize(3)
    setheading(-90)
    backward(20)
    setheading(90)
    backward(55)
    pendown()
    fillcolor('red')
    begin_fill()
    circle(5)
    end_fill()
    penup()
    
    #tail
    pensize(3)
    goto(x-30, y+40)
    pendown()
    setheading(0)
    color('black')
    begin_fill()
    forward(20) 
    right(120)
    forward(20)
    right(120)
    forward(20)
    end_fill()
    penup()

    

#Fifth_Hexagon
def fifth_fish(x,y):
    speed('fastest')
    tracer(False)
    goto(x-50, y+50) # go to coordinate of hexagon
    setheading(0)

    # Border Hexagon
    
    for border in range(6): 
        pensize(2)
        pendown()
        forward(60)
        left(300)
        penup()


#fifth body

    goto(x-30,y-30)
    pendown()
    fillcolor('blue')
    setheading(-90)
    begin_fill()
    def fifth_body(rad):
     
      #ellipse
      for g in range(2):
        circle(rad,90)
        circle(rad//2,90)
        
    # tilt the shape 
    seth(-10)
 
    # calling draw method
    fifth_body(35)
    end_fill()
    penup()

    #eyes for fifth fish
    pensize(3)
    setheading(-90)
    backward(10)
    setheading(0)
    fd(10)
    pendown()
    fillcolor('red')
    begin_fill()
    circle(5)
    end_fill()
    penup()


#Fifth_fish description

def Fifth_fish_desc(x,y):
    penup()
    goto(x+50, y-50)
    write('South West', align = 'right', font= (40))

Fifth_fish_desc(530,-30)


#Sixth_Hexagon
def sixth_fish(x,y):
    speed('fastest')
    tracer(False)
    goto(x-50, y+50) # go to coordinate of hexagon
    setheading(0)

    # Border Hexagon
    
    for border in range(6): 
        pensize(2)
        pendown()
        forward(60)
        left(300)
        penup()

#sixth body

    goto(x-50,y-20)
    pendown()
    fillcolor('blue')
    setheading(-90)
    begin_fill()
    def sixth_body(rad):
     
      #ellipse
      for p in range(2):
        circle(rad,90)
        circle(rad//2,90)
        
    # tilt the shape to south
    seth(-45)
 
    # calling draw method
    sixth_body(35)
    end_fill()
    penup()

    #eyes for sixth fish
    pensize(3)
    setheading(-90)
    backward(10)
    setheading(0)
    fd(10)
    pendown()
    fillcolor('red')
    begin_fill()
    circle(5)
    end_fill()
    penup()

    #tail
    pensize(3)
    goto(x, y-5)
    pendown()
    setheading(30)
    color('black')
    begin_fill()
    forward(20) 
    right(120)
    forward(20)
    right(120)
    forward(20)
    end_fill()
    penup()
    
   
    

#Sixth_fish description

def sixth_fish_desc(x,y):
    penup()
    goto(x+50, y-50)
    write('West', align = 'right', font= (40))

sixth_fish_desc(500,-180)



# Title of the First Fish Direction

def shark_first_desc(x,y):
    penup()
    goto(x+20, y-30)
    write('East', align = 'right', font = (40))

shark_first_desc(-520, 100) 
    

#Fourth_fish description

def fourthfish_desc(x,y):
    penup()
    goto(x+50, y-50)
    write('South', align = 'right', font= (40))

fourthfish_desc(500,120)
    
    
       
        
        

# Calling out drawings by specific coordinates

def visualise_data(rename):
    shark1(-500, 150)
    second_fish(-500, 0)
    third_fish(-500, -150)
    fourth_fish(550,150)
    fifth_fish(550,0)
    sixth_fish(550,-150)

pass


# Index

shark_drawing_index = [shark1, second_fish, third_fish, fourth_fish, fifth_fish, sixth_fish]
#y_coordinate = 
step = [0, 1, 2, 3, 4]


    


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
