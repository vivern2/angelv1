import ollama 


#Below is a function that will connect to the ai and give the ai's response
def get_response(user_text):
    try:
        #Below will connect to the ai and get the response
        response = ollama.chat(
            
            )
        return response

    #below is error handlign
    except Exception as e:
        #Below will print an error message in the terminal
        print("ERROR:", e)
        return f"Error: {e}"