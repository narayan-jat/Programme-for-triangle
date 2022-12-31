# Given 3 angles of a triangle as input ,print if the triangle is "Acute","Obtuse",Right angled ,"Invalid"

'''
This module contains 

Author: Narayan Jat
Date: December 14,2022
'''
#Prompting user to enter three angles
angle1 = float(input("Enter the value of first angle of triangle: "))
angle2 = float(input("Enter the value of second angle of triangle: "))
angle3 = float(input("Enter the value of third angle of triangle: "))

#Creating function to check a tringle is valid or not
def is_triangle(angle1 ,angle2 ,angle3 ):
	'''
	Returns: True if these three angles forming a triangle otherwise False.

	parameters angle1:It is anmgle of triangle
	precondition:It must be float type

	parameters angle2:It is anmgle of triangle
	precondition:It must be float type

	parameters angle3:It is anmgle of triangle
	precondition:It must be float type

	>>> is_triangle(60 ,45 ,32 )
	False
	>>> is_triangle(60 ,60 ,60 )
	True
	>>> is_triangle(60 ,80 ,90 )
	False
	'''
	if angle1 == 0 or angle2 == 0 or angle3 == 0 :
		return False
	return angle3 + angle1 + angle2 == 180

# Function to tell type of triangle
def comment_triangle(angle1 ,angle2 ,angle3 ):
	'''
	Returns:Acute,Obtuse,Right angled or Invalid 

	parameters angle1:It is anmgle of triangle
	precondition:It must be float type

	parameters angle2:It is anmgle of triangle
	precondition:It must be float type

	parameters angle3:It is anmgle of triangle
	precondition:It must be float type

	>>> comment_triangle(60 ,60 ,60 )
	'Acute'
	>>> comment_triangle(120 ,30 ,30 )
	'Obtuse'
	>>> comment_triangle(90 ,15 ,75 )
	'Right angled'
	>>> comment_triangle(60 ,60 ,80 )
	'Invalid'
	'''
	if not(is_triangle(angle1 ,angle2 ,angle3 )):
		return "Invalid"
	elif angle1 > 90 or angle2 > 90 or angle3 > 90 :
		return "Obtuse"
	elif angle1 == 90 or angle2 == 90 or angle3 == 90 :
		return "Right angled"
	else:
		return "Acute"
