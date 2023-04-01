import sys
import backend

#This class was named FrontEndUI as it is what is displaying the user interface
#alternatively it could of been called Main or MainUI but labelling it as front end
#makes it easier to distinguish against other classes when it is being called from
#other applications.
#Alternatively the code in this class could of been all placed in the init def however
#having one def specifically used for user outputs and inputs is a better way of
#organising the code as it increases the code readability and makes it easier to modify,
#and add operations and methods in the future.
class FrontEndUI:

    #This def was called get_str as it is collecting a string data type from the
    #user, alternatively it could of been called shortcut_readline however this
    #function is performing more than just collecting data through a readline. Using
    #the word readline might also cause cause confusion or bugs in the code.
    #This def was created to avoid repitition in the code and is used in all
    #revelant places except where the user is entering input to correct mistakes.
    @staticmethod
    def __get_str(prompt:str)->str:
        sys.stdout.write(str(prompt))
        sys.stdout.flush()
        
        #Justification 1: This code used the try and except condition so the code would
        #not crash if the function could not be performed, alternatively I could of
        #entered this into the program without the try, except condition however this
        #increases the chance of the program crashing.
        #This variable could of alternatively been named input however I didnt want the
        #this is already a function in python so the_input was used instead.
        try:
            the_input = sys.stdin.readline().strip()
            
        #Justification 2: Alternatively the exception could of been named with
        #another letter but to build consistency throughout the program, the same
        #letter e has been used.
        #Justification 3: The program could of alternatively used sys.stdout.write
        #to state a general error however, this method indentifies the exact problem
        #with the code and communicates this to the user.
        except Exception as e:
            sys.stdout.write("Something went wrong")
            sys.stdout.write(str(e))
        return the_input


    #The calling of the save_to_file method and the load_from_file method were originally
    #placed in the initialiser however as it was giving output to the user I decided to put
    #it in user interface instead even though the output was the result of an exception.
    #The init contructor lets the class initialise the objects attributes for this
    #reason the init only contains the objects being made and all other code was put in
    #seperate defs in the class.
    def __init__(self, be):
        self.b = be
        self.file_name=be.data_file



    #The def is called show_ui as it is where the inputs are taken from the user and where
    #the outputs are given it could of alternatively been called main_def however show_ui is
    #more specific to  the function this method is performing for the program and therefore
    #more effective.
    #Originally I created three defs for if the user enters "a", "d", or "x" however
    #once I realised I could create the same outcome with the code by putting it
    #inside of a while loop and using an if, else statment I decided to use this
    #method to create my program as it was using less code and simplified it significantly.      
    def show_ui(self):


        #Alternatively the load_from_file def could have been used after the save_to_file
        #def however this method was not loading existing csv files and was creating a
        #new file everytime even if the file was  existing.
        #Refer to justification 1
        try:
            self.b.load_from_file(self.file_name)

        #Refer to justification 2
        #Refer to justification 3
        except Exception as e:
            sys.stdout.write("\nThere are no existing files called: "+self.file_name+ " \nCreating a new file now...\n")
  
        #Initially the save_to_file def was only called in the show_ui def after the data
        #had been entered, however it was entered here so the computer would create the
        #new file before any of the user interface was shown.
        #Refer to justification 1
        try:
            self.b.save_to_file(self.file_name)

        #Refer to justification 2
        #Refer to justification 3
        except Exception as e:
            sys.stdout.write(str(e))

        menu ="\nWhat would you like to do?\n"
        menu+="[A]dd a movie\n"
        menu+="[D]isplay all movies\n"
        menu+="E[x]it\n"

        choice = FrontEndUI.__get_str(menu).lower()

        #Alternatively the user could have chosen between three options which were
        #numbered however, using singular letters was a more effective way of
        #writing the code as it can be taken and compared as a string rather than
        #taken as an int and compared using arithmetic operators, this creates
        #limited options for the user and therefore less chance of error.
        #Another way this code could of been written would of been to create three
        #seperate defs for each letter and their outcomes and called them in the
        #main function, however as these functions could not of been created in the
        #backend it is more effective to leave the code in the main def.
        while (choice!= "x"):
            
            #Alternatively the word add could of been used however, the use of the
            #singular letter "a" minimises the chance of error from the user.
            #The get_str function was used rather than a readline to decrease code
            #duplication.
            #The variable title was called originally called "name" but was
            #changed to title to make it searchable in code and to differentiate
            #it from variable file_name.
            if choice =="a":

                title = FrontEndUI.__get_str("\nEnter the movies name: ")
                #The variable title was called originally called "name" but was
                #changed to title to make it searchable in code and to differentiate
                #it from variable file_name
                #The get_str function could of been used instead of the readline
                #however, I did not want the program to re-print the input when the
                #user was correcting mistakes.
                while( len(title)==0):
                    title = FrontEndUI.__get_str("\nInput cannot be blank. Re-enter: ")

                    
                release=FrontEndUI.__get_str("\nEnter the year the movie was released:")

                
                #This while loop could of alternatively been created with an if, else
                #function however I put it in a loop so it would repeat until release
                #didn't equal none.
                #This code used the try and except condition so the code would
                #not crash if the function could not be performed, alternatively I could of
                #entered this into the program without the try, except condition however this
                #increases the chance of the program crashing.
                while(release==None):

                    #This variable was chosen to be of the int data type rather than the
                    #float data type as it is more common to refer to a movie by the
                    #year of release rather than the date of release. Therefore the int
                    #data type was a more appropriate choice.
                    #The get_str function was used rather than a readline to reduce code
                    #duplication, the data also needed to be collected as a integer but
                    #could be stored as a string rather than an integer.
                    try:
                        str_release = FrontEndUI.__get_str("\nEnter release date again: ")
                        release = self.b.validate_release_year(str_release)
                        
                    #Refer to justification 2
                    #Refer to justification 3
                    except Exception as e:
                        sys.stdout.write(str(e)+"\nRe-enter...")

                #This variable was named runtime as oppose to duration or lenth as
                #it is a more specific term usually used when referring to movies.
                #The runtime alternatively could have been collected as a integer with
                #the sum of minutes however a float data type was better suited as
                #the user is more likely to enter the data as a decimal.
                #The get_str function was used rather than a readline to reduce code
                #duplication, the data also needs to be collected as as the float
                #data type but can be stored as a string as opposed to being stored
                #as a float.
                #Refer to justification 1
                try:
                    runtime = FrontEndUI.__get_str("\nEnter the runtime of your favourite movie: ")
                    
                #Refer to justification 1
                #Refer to justification 2
                except Exception as e:
                    sys.stdout.write("\nError! The following error has happened: "+str(e))

                
                #This code block was created with a try except function, so the user
                #will be indentified of any error in running the code rather than
                #the program crashing when a demand can not be met.
                #This code block calls the add_movie def from the backend of the code
                #it was placed in the back end rather than the front as it references
                #the Movie class.
                try:
                    self.b.add_movie(title,release,runtime)
                    
                #Refer to justification 2
                #Refer to justification 3
                except Exception as e:
                    sys.stdout.write("Error! the following "+str(e))

            #The word "display" could have been used as the variable as opposed to d,
            #however a single letter simplifies the code and decreases the risk of
            #user error.
            #The program used the str def created in the backend to print the summary
            #of the list alternatively I could of put this while loop in the front
            #end however this way simplifies the show_ui def and the front end code.
            elif (choice=="d"):
                sys.stdout.write(str(self.b) )

            #Alternatively I could of customised an elif function for possible
            #output mistakes the user may of made for example if the user entered a
            #number, or a word over the length of 1. Although this could of
            #overcomplicated the code and not served much of a purpose in the end.
            #A different text output could have been used explaining to the user they
            #did not pick either a, d, or x however I wanted to keep this output
            #short and as concise as possible.
            else:
                sys.stdout.write("Invalid choice\n")

            choice = FrontEndUI.__get_str(menu).lower()
        self.b.save_to_file(self.file_name)
