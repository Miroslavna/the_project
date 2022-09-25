import os
from time import sleep
from datetime import datetime
import time
from tkinter.ttk import Separator

digits = dict()
digits['0'] = '''
            
  ■■■■■■■■  
  ■■    ■■  
  ■■    ■■  
  ■■    ■■  
  ■■■■■■■■  
            
'''
digits['1'] = '''
            
     ■■     
  ■■ ■■     
     ■■     
     ■■        
  ■■■■■■■■  
                       
'''
digits['2'] = '''
            
   ■■■■■■  
  ■     ■■  
       ■■   
     ■■     
  ■■■■■■■■  
            
'''
digits['3'] = '''
            
  ■■■■■■■■  
         ■  
     ■■■■■  
         ■  
  ■■■■■■■■  
            
'''
digits['4'] = '''
            
  ■      ■  
  ■      ■  
  ■■■■■■■■  
         ■  
         ■  
            
'''
digits['5'] = '''
            
  ■■■■■■■■  
  ■         
  ■■■■■■■■  
         ■  
  ■■■■■■■■  
            
'''
digits['6'] = '''
            
  ■■■■■■■■  
  ■         
  ■■■■■■■■  
  ■      ■  
  ■■■■■■■■  
            
'''
digits['7'] = '''
            
  ■■■■■■■■  
        ■■  
       ■    
      ■     
     ■      
           
'''
digits['8'] = '''
            
  ■■■■■■■■  
  ■      ■  
  ■■■■■■■■  
  ■      ■  
  ■■■■■■■■  
            
'''
digits['9'] = '''
            
  ■■■■■■■■  
  ■      ■  
  ■■■■■■■■  
         ■  
  ■■■■■■■■  
            
'''
digits[':'] = '''
            
     ■■       
     ■■        
            
'''


while True:    
    for ch in datetime.now().strftime("%H:%M:%S"):
        if ch in digits:
             print(digits[ch], end='')            
    time.sleep(1)
    if os.name == 'nt':
       os.system('cls')
    else: 
        os.system('clear')