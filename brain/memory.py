#below allows us to use our json files
import json
#below lets us use the os module to interact with the operating system and file system, such as reading and writing files
import os
#Below will be the location of the json memory file for Angel. 
MEMORY_FILE = "brain/memory.json"


#-------BELOW IS THE FUNCTION TO LOAD MEMORY FROM THE JSON FILE-------------------------------------------------------------
def load_memory():
    #below checks if the memory file exists if it does not it returns an empty dictionary 
    if not os.path.exists(MEMORY_FILE):
        return {}
    
    #below opens the memory file and loads the data from it using json
    with open(MEMORY_FILE, "r") as file:
        #below converts the json data into a python dictionary 
        return json.load(file)
    
#-------BELOW IS THE FUNCTION TO SAVE MEMORY TO THE JSON FILE-------------------------------------------------------------
def save_memory(data):
    #below opens the memory file in write mode
    with open(MEMORY_FILE, "w") as file:
        #below converts the python dictionary into json data and saves it to the file with indentation for readability
        json.dump(data, file, indent=4)


#------BELOW IS A FUNCTION TO SAVE THE USERS NAME TO MEMORY-------------------------------------------------------------
def  remember_name(user_text):
    #below calls upon the load_memory function to get the current memory data
    memory = load_memory()

    if "my name is" in user_text.lower():
        #below extracts the name from the user's input by splitting the text at "my name is" and taking the part after it, then stripping any extra whitespace
        name = user_text.lower().split("my name is")[-1].strip()
        #below captilizes the first letter of the name and makes the rest lowercase to ensure consistency in how the name is stored and used in responses
        name = name.capitalize()
        #below saves to memory by adding the name to the memory dictionary under the key "name" and then calls the save_memory function to write the updated memory back to the json file
        memory["name"] = name
        #below saves to file
        save_memory(memory)


#------BELOW IS A FUNCTION TO RETRIEVE THE USERS NAME FROM MEMORY-------------------------------------------------------------
def get_name():
    #below loads currrent memory 
    memory = load_memory()
    #below if name exits returns the name from memrory if not returns none
    return memory.get("name", None)
        


    
