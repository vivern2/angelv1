#below will import Angels personality traits and characteristics
from brain.personality import ANGEL_PERSONALITY

#below imports ollama which houses the ai models we are using in this project. We will be using two models, Llama 3.1 and DeepSeek
import ollama 

#below imports the functions to save and retrieve memory from the json file
from brain.memory import remember_name, get_name

#below is a simple list that holds the conversation history between the user and the ai
conversation_history = []





#-------BELOW IS THE GET RESPONSE FUNCTION-------------------------------------------------------------
#Below is a function that will connect to the ai and give the ai's response
def get_response(user_text):
    try:
        #below will connect two models we are using and help us choose between them using the choose_model function 
        model = choose_model(user_text)

        #--------------------------------------------------------------------------------------------------------------------------
    #ALL STUFF BELOW IS ABOUT REMEMBERING THE USERS NAME AND INJECTING IT INTO THE AI'S PERSONALITY TO MAKE THE RESPONSES MORE PERSONALIZED AND HUMAN LIKE
        #below will save the users name if already given from memory.py
        remember_name(user_text)
        #below will load memory and get the users name if it is already given, this will allow the ai to use the users name in its responses and make it more personalized
        name = get_name() 

        system_prompt =  ANGEL_PERSONALITY
        #Below will inject the memory into Angels personality
        if name: 
            system_prompt += f"\nThe user's name is {name}. Use it when appropriate."

        #--------------------------------------------------------------------------------------------------------------------------

        #below adds all of the users messages to the conversation history list
        conversation_history.append({"role": "user", "content": user_text})


       #below is the acutal ai response that will be given to the user
        response = ollama.chat(
                model = model,
                messages=[
                    #Below defines Angel as a helpful and friendly assistant, a calm and intelligent AI assistant. This will help the ai to give better responses to the user
                    {"role": "system","content": system_prompt},
                    #below sends the full history to the ai
                ] + conversation_history
            )
        reply = response ["message"]["content"]

        #below stores Angels response in the conversation history list so that it can be used in future responses and to give the ai more context about the conversation
        conversation_history.append({"role": "assistant", "content": reply})

        return reply

    #below is error handlign
    except Exception as e:
        #Below will print an error message in the terminal
        print("ERROR:", e)
        return f"Error: {e}"






#-------BELOW IS THE CHOOSE MODEL FUNCTION-------------------------------------------------------------
def choose_model(user_text):
    text = user_text.lower()

    #if it is a Reasoning or Coding question it will use DeepSeek
    if any(word in text for word in ["code", "solve", "math", "algorithm", "why", "how", "reasoning", "debug"]):
        return "deepseek-r1:8b"
    
    #defualt model is Llama 3.1
    return "llama3"