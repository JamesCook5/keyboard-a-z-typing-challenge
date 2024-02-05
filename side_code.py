

def database(elapsed_time):
      running = True
      while running == True:
        username = str(input("\nplease enter your username and we will add it to the database.\n\nPlease enter the first letter of your first name followed by the rest of your surname with no spaces.\n\nenter:  ")).upper()
        if username.isdigit():
           running = True
        elif username == "":
            running = True
        else:
            running = False
    
    


      wish = int(input("\ndo you wish to add your score to your database username?\n\nIf you do press <1>\nIf not press <2>\nenter: "))
      if wish == 1:
        filetxt = open("record.txt","a")
        
        answer = username,elapsed_time
        answer = str(answer)
        
        filetxt.write(answer)
        
        filetxt.close()
      else:
          print("thanks for playing!")



