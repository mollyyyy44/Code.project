
#An alternative name for the class could of been Movies or MovieList however
#Movie is more concise.It also eliminates the risk of confusion with the list
#name movies which is used many times throughout the code.
#A class was created alternatively to appending three seperate lists as it
#simplifys the code and reduces repitition.
class Movie:
    __movie_count = 0
    __min_release =100

    #The self parameter was used to represent the instance of the class, the
    #variable was named self rather than something like "access" as it would
    #make it easier for other programmers to understand my code, by using the
    #most common and generally understood name for this parameter. 
    #The __init__ constructor was used as multiple objects were being created
    #within the class, alternatively I could of make three classes for each
    #attribute.
    def __init__(self,title,release,runtime):
        self.__title=title
        self.release=release
        self.__runtime=float(runtime)
        Movie.__movie_count+=1
        self.__movie_number = Movie.__movie_count

    #This accessor returns the variables value and helps to access the private
    #attribute from the class, alternatively the variable title could have been
    #kept public however using this method keeps data hidden from other
    #classes when the program is run.
    #This def was named title as this is the variable it is making private.
    @property
    def title(self):
        return self.__title
    
    #This accessor returns the variables value and helps to access the private
    #attribute from the class, alternatively the variable release could have been
    #kept public however using this method means the data is kept hidden from other
    #classes when the program is run.
    #This def was named release as this is the variable it is making private.
    @property
    def release(self):
        return self.__release

    #The release setter sets the value of the variable, it is used to modify
    #private variables of a class, alternatively the variable release could have been
    #kept public however using this method keeps data hidden from other
    #classes when the program is run.
    @release.setter
    def release(self,release):
        self.__release=Movie.validate_release_year(release)

    #This def is validating the release year using two raised if statements,
    #alternatively this could have been done in the frontend in the show_ui def however
    #passing the variable to be validated in the backend simplifys the code so that
    #show_ui only contains the user interface.
    #A class method was used so this method would not be bound to a specific instance
    #but to the class I did this because I wanted this def to apply to the whole class.
    @classmethod
    def validate_release_year(cls,release):
        release=int(release)
        if (release<cls.__min_release):
            raise ValueError("Year of release must be after"+cls.__min_release)
        if (release>=2023):
            raise ValueError("Year of release must be before 2023")
        return release
    
    #This alternatively could have been done with a while loop that finishes when
    #the index is less than the length of movies however instead a str def was used
    #and then called in the front end as this is a more effective way of writing this code.
    #This method returns the string representation of the object alternatively, if this
    #code was not in a class it would have been in a get_summary def.
    def __str__ (self):
        summary = "Movie "+str(self.__movie_number)+"\n"
        summary+= "\tTitle: "+self.__title+"\n"
        summary+= "\tYear of release: "+str(self.release)+"\n"
        summary+= "\tLength of movie: "+str(self.__runtime)+"\n"
        return summary

    #The repr method was used to return the printable representation of the specified
    #object in a string format alternatively if the program was not object orientated
    #the code in the str and repr methods would have been in a combined def which
    #retrieved the summary for the user.
    def __repr__(self):
        summary = self.__title+","
        summary+= str(self.__release)+","
        summary+= str(self.__runtime)
        return summary

#A second class was created rather than using multiple seperate defs to simplify
#the code and improve code consistency so it was all object orientated programming.
#This was done to increase code organisation and reusablity which are both benefits
#of using classes rather than multiple defs as all defs called in the front end
#can now be called directly from BackEndManager.
class BackEndManager:

    #Alternatively if the BackEndManager class was not created a
    #get_new_data_structure would of been used rather than creating self.__movies
    #as an object, however using a class to create this data structure was a more
    #effective way of writing this code.
    #init makes objects
    #The init contructor lets the class initialise the objects attributes for this
    #reason the init only contains the objects being made and all other code was put in
    #seperate defs in the class.
    def __init__(self):
        self.__movies = []
        self.data_file=""

    #This def was originally named load_data_from_file however, to simplify
    #the name it was changed to load_from_file.
    #If I had not used a class to create this list I could of alternatively
    #made three different load_from_file defs saving the different data types
    #in different places however this method significantly decreases code
    #duplication and simplifies the program overall.
    def load_from_file(self,file_name):

        #The variable was named in_file_obj to clarify if the code is loading
        #data out of the file or into the file, if the code was performing the
        #alternative it would of been called out_file_obj as seen later in the code.
        #When having the user name the file, originally an existing file called
        #data.csv was modified rather than creating a new file however this was
        #changed to make sure the code will function with any file name whether
	#the file already exists or not. 
        try:
            in_file_obj=open(file_name,"r")

        #The ValueErrors in this function have been created with different outputs
        #to eachother so the user can differentiate between errors and identify
        #where in the program their issue is occuring.
        #The variable could of alternatively been named text or row however it was
        #named line as this is the most accurate description.
        except:
            raise ValueError("Unable to open file: "+file_name)

        line = in_file_obj.readline()

        #A while loop was used to perform this function as opposed to using the
        #if, else function so the code would run and repeat until false.
        #The ValueErrors will are used in this code block with different outputs
        #as it helps the user to troubleshoot and identify what is going wrong
        #in the code.
        while(line!=""):
            fields=line.strip().split(",")

            #Alternatively the arithemtic operators if less than three or more
            #than three could of been used however this using the != operator
            #simplifies the code and the chance of any other errors.
            #The ValueErrors in this function and loop have been created with
            #different outputs to eachother so the user can differentiate between
            #errors and identify where in the program their issue is occuring.
            if(len(fields)!=3):
                raise ValueError("Incorrect number of values on line: "+line)

            #Alternatively to assigning each variable to an the index in this
            #order, a different order could of been used, however to build
            #consistency in the code I attempted to copy the order in which
            #the input was entered.
            try:
                title=fields[0]
                release=fields[1]
                runtime=fields[2]

            #The ValueError could alternatively ask the user to re-format their
            #line and re-enter the data however, this may not fix the problem
            #so the data will be entered regardless of the format.
            #The ValueErrors in this function and loop have been created with
            #different outputs to eachother so the user can differentiate between
            #errors and identify where in the program their issue is occuring.
            except:
                raise ValueError("Badly formatted data line in file: "+line)
            self.add_movie(title,release,runtime)
            line=in_file_obj.readline()

        in_file_obj.close()

    #This method was named validate_release_year however it could of alternatively
    #been called confirming_release_year however validate release year is more
    #accurate to the function the program is performing.
    #This method was created as a static method so it is bound to the class this
    #was done because I didn't want subclasses of the class to change or override
    #the specific implementation of the method.
    @staticmethod
    def validate_release_year(release):
        return Movie.validate_release_year(release)

    #This def was called add_movie as opposed to add_movies as the program is
    #are creating and appending to the new list movie not movies
    #If a class was not used, title, release and runtime would of been appended
    #seperately however appending the list as one simplifies the code and
    #involves less repetition.
    def add_movie(self,title,release,runtime):
        movie=Movie(title,release,runtime)
        self.__movies.append(movie)

    #This method returns the string representation of the object alternatively, if this
    #code was not in a class it would have been in a get_summary def.
    #This def was called __str__ as this is the method in python to achieve the
    #outcome the code was code was trying to achieve.
    def __str__(self):
        summary = ""
        index = 0

        #A while loop was used as opposed to printing each input as the user enters
        #it, as it uses the len() function to determine the length of the list
        #according to the index, and how many times the program will need to repeat
        #the function, making it was more adaptable to change and error.
        #Alternatively, I could of used the less than sign and asked the list to repeat
        #when the length of the movies was less than the index.
        while(index< len(self.__movies)):
            summary+="\n"+str(self.__movies[index])
            index+=1
        return summary

    #The repr method was used to return the printable representation of the specified
    #object in a string format alternatively if the program was not object orientated
    #the code in the str and repr methods would have been in a combined def which
    #retrieved the summary for the user.
    def __repr__(self):
        summary = ""
        index = 0
        
        #A while loop was used as opposed to printing each input as the user enters
        #it, as it uses the len() function to determine the length of the list
        #according to the index, and how many times the program will need to repeat
        #the function, making it was more adaptable to change and error.
        #Alternatively, I could of used the less than sign and asked the list to repeat
        #when the length of the movies was less than the index.
        while(index< len(self.__movies)):
            summary+=repr(self.__movies[index])+"\n"
            index+=1
        return summary

    #This def could of alternatively been named write_to_file however I didnt want
    #any crossover between this and the "write" function it was also to clarify
    #that this function is writing, saving and closing therefore performing multiple
    #functions rather than just writing to the file so I thought it more appropriate
    #to name it save_to_file.
    #This def creates and uses the variable summary rather than sys.stdout.write as
    #we are writing to the file rather than to the python idle.
    def save_to_file(self,file_name):
        out_file_obj=open(file_name,"w")
        out_file_obj.write(repr(self) )
        out_file_obj.close()
