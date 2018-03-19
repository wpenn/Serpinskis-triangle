from drawingpanel import *
import math

panel = DrawingPanel(500, 500)
panel.set_background("green")
canvas = panel.canvas

def sierpinski_triangle(iterations):
	'''First iteration / seed '''
	C_Point_Y_Value = 53.5898384862

	if iterations >= 0:
		''' First Iteration '''
		canvas.create_polygon(50, 400, 450, 400, 250, C_Point_Y_Value, fill="black") #Outer triangle
	if iterations >= 1:
		create_triangle(150, (400 + 53.5898384862)/2, 200) #Inner triangle –>  first iteration
	if iterations > 1:
		''' Recursive functions '''
		create_triangle_children(150, (400 + 53.5898384862)/2, 200, iterations - 2)
	

def create_triangle(x, y, side_length):
	canvas.create_polygon(x, y, x + side_length, y, x + (side_length/2), (math.sqrt((3 * side_length **2)/4)) + y, fill="white")


def create_triangle_children(x, y, side_length, iterations):
	'''creates an equilateral triangle'''
	create_triangle((x + 250)/2, (y + 53.5898384862)/2, side_length/2) #top
	create_triangle((x + 450)/2, (y + 400)/2, side_length/2) #right
	create_triangle((x + 50)/2, (y + 400)/2, side_length/2) #left

	if iterations != 0:
		create_triangle_children((x+ 250)/2, (y + 53.5898384862)/2, side_length/2, iterations - 1)
		create_triangle_children((x + 450)/2, (y + 400)/2, side_length/2, iterations - 1)
		create_triangle_children((x + 50)/2, (y + 400)/2, side_length/2, iterations - 1) 
	
def main():
	user_input = ""
	while user_input == "":
		user_input = int(input("How many iterations would you like to do? "))
	sierpinski_triangle(user_input)

main()
