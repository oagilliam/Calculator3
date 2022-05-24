#Created by: Olivia G.
#Completion date: 5/24/2022
#Prompt: Create a calculator that takes two numbers and calculates tham based on an operator selected by the usser.
#The calculator should continue to perform calculations until the user enters 'AC' or 'ac'. Any invalid inputs
#should be ignored.

import sys
import operator

#This dictionary contains math operators.
ops = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}


while True: #This while loop allows the loops inside to continue runnig.

    #This loop will ask for the first input and check to make sure the input is valid. It will ignore invalid inputs.
    while True:
        print('Enter first number')
        input_1 = input('>>')
        if input_1 not in ['AC','ac'] and input_1.isdigit() == True:
            num1 = input_1
            break
        elif input_1 in ['AC','ac']:
            print('ALL CLEAR')
            sys.exit()

    #This loop will ask for the second input and check to make sure the input is valid. It will ignore invalid inputs.
    while True:
        print('Enter an operator (+,-,/,*)')
        op_input = input('>>')
        if op_input in ops:
            oper = op_input
            break

    #This loop will ask for the third input and check to make sure the input is valid. It will ignore invalid inputs.
    while True:
        print('Enter second number')
        input_2 = input('>>')
        if input_2 not in ['AC', 'ac'] and input_2.isdigit() == True:
            num2 = input_2
            break
        elif input_2 in ['AC','ac']:
            print('ALL CLEAR')
            sys.exit()

    #This function will perform a mathematical calculation based on the inputs entered by the user. 
    def calculation(num1,oper,num2):
        num1, num2 = int(num1), int(num2)
        result = ops[oper](num1,num2)
        print('=', result) 

    calculation(num1,oper,num2)