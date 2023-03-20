from utils import Utils
import re
from models import *
from constants import *
import uuid

flag = True
while flag:
    print("1. Thompson Algorithm\n2. Exit")
    opc=input("Choose an option: ")
    
    if opc == '2':
        exit()
    elif opc == '1':
        expression,balanced = Utils.get_infix_expression()
        
        if balanced is True:
            expression = Utils.parse_expresion(expression) 
            expanded_expression = Utils.expand(expression)
            postfix_expression = Utils.infix_to_postfix(expanded_expression)
            
            afn = Utils.thompson_algorithm(postfix_expression)
            file_name = str(uuid.uuid4().fields[-1])[:5]
            Utils.write_txt_file(file_name,afn)
            Utils.graphic(afn,file_name,method='AFN')
            
            evaluation_exp = input('Expression to evaluate: ')
            state = Utils.simulate(evaluation_exp,afn=afn)
            if state is True:
                print('The expression: ' + str(evaluation_exp) + ' is valid \n')
            else:
                print('The expression: ' + str(evaluation_exp) + ' is not valid \n')
        else:
            print('Error in the expression: ' +str(expression) + '\n')
        
    elif opc !="":
      print("\nWrong option") 