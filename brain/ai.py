import ollama 


#Below is a function that will connect to the ai and give the ai's response
def get_response(user_text):
    try:
        #below will connect two models we are using and help us choose between them using the choose_model function 
        model = choose_model(user_text)

       #below is the acutal ai response that will be given to the user
        response = ollama.chat(
                model = model,
                messages=[
                    #Below defines Angel as a helpful and friendly assistant, a calm and intelligent AI assistant. This will help the ai to give better responses to the user
                    {
                        "role": "system",
                        "content": "You are Angel, a helpful and friendly assistant.a calm and intelligent AI assistant."
                    },
                    # below is the user input that will be sent to the ai
                    {"role": "user", "content": user_text}
                ]
            )
        return response ["message"]["content"]

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