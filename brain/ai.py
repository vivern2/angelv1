#below will import Angels personality traits and characteristics
from brain.personality import ANGEL_PERSONALITY

#below imports ollama which houses the ai models we are using in this project. We will be using two models, Llama 3.1 and DeepSeek
import ollama 


#below is a simple list that holds the conversation history between the user and the ai
conversation_history = []





#-------BELOW IS THE GET RESPONSE FUNCTION-------------------------------------------------------------
#Below is a function that will connect to the ai and give the ai's response
def get_response(user_text):
    try:
        #below will connect two models we are using and help us choose between them using the choose_model function 
        model = choose_model(user_text)

        #below adds all of the users messages to the conversation history list
        conversation_history.append({"role": "user", "content": user_text})


       #below is the acutal ai response that will be given to the user
        response = ollama.chat(
                model = model,
                messages=[
                    #Below defines Angel as a helpful and friendly assistant, a calm and intelligent AI assistant. This will help the ai to give better responses to the user
                    {"role": "system","content": ANGEL_PERSONALITY},
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