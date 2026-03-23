#below allows us to acess operating system features such as environment variables(env) and more
import os
#below connects acess to the python .env feature to use api keys saved there
from dotenv import load_dotenv
#below we are using openai for the actual ai for now
from openai import OpenAI

#below loads the environment variables
load_dotenv()

#creates open ai client with the specific api key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


#Below is a function that will connect to the ai and give the ai's response
def get_response(user_text):
    try:
        #below the response = client stuff creates request to AI
        response = client.chat.completions.create(
            #below will be the model we are using we can change later
            model = "gpt-4o-mini",

            #below messages is how we talk to the AI
            messages=[ 
                #below defines who Angel is with a system message
                {"role": "system", "content": "you are Angel, a helpful and polite AI assistant"},
                #below is the user and what the user messages 
                {"role": "user", "content": user_text}
            ]
        )

        #below extracts the ai's answer text, basically the AI's output
        return response.choices[0].message.content

    #below is error handlign
    except Exception as e:
        #Below will print an error in the terminal
        print("ERROR:", e)
        return "Sorry, something went wrong."