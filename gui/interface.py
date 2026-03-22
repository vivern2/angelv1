import customtkinter

#below when working on speak uncomment it
#from voice import speak 

#below creates the main app window
app = customtkinter.CTk()

#----------CUSTOMIZATION--------------------------------------
#below sets the title of the app window
app.title("Angel AI")
#below sets the mode + theme of the app window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")  
#below sets the size of the app window
app.geometry("500x500")
#----CHATBOX-CONVERSATION-BOX--------------------------------------
#below is for the dimensions of the chatbox
chatbox = customtkinter.CTkTextbox(app, width=400, height=300)
#below gives vertical spacing(padding)
chatbox.pack(pady=5)
#----INPUT-FIELD----------------------------------------------------
entry = customtkinter.CTkEntry(app, width=350, placeholder_text="Type your message here...")
entry.pack(pady=5)
#below binds the enter key to the send_button function, so that pressing enter will send the message too
entry.bind("<Return>", lambda event: send_button())
#below entry.focus() is used to set the focus on the entry field when the app starts, so that the user can start typing immediately without having to click on the entry field first
entry.focus()
#---------------------------------------------------------------





#-----SEND-BUTTON------------------------------------------------
#below is the function taht 
def send_button():
    #below gets the text from the entry field,.strip() removes any leading/trailing whitespace
    user_input = entry.get().strip()
    # If the input is empty, do nothing
    if not user_input:
        return   
    
    #-----WORK ON LATER---------------------------------
    #below is a function that will connect with brain to get the response, for now it just echoes the user input
    #response = get_response(user_input)  # This is a placeholder function, replace with actual response generation
    #below updates the chatbox with the user input and the response from the brain, for now it just shows the user input and a placeholder response
    #update_chat(user_input, response)
    #Below will eventually be used to make angel speak out her response connects with the voice
    #speak(response)  # This is a placeholder function, replace with actual text-to-speech functionality
    #---------------------------------------------------

    #below is a place holder function to show user input and response
    chatbox.insert("end", "You: " + user_input + "\n")
    #below "I dont understnad yet" is a placeholder response, replace with response from the brain
    chatbox.insert("end", "Angel: " + "I dont undertand yet" + "\n")

    #below is the autoscroll feature, it scrolls to the end of the chatbox after inserting new messages
    chatbox.see("end")

    #below clears the entry field after sending the message
    entry.delete(0, "end")
# command is just the function for the button to work
button = customtkinter.CTkButton(app, text="Send Message", command=send_button)
button.pack(pady=10)
#--------------------------------------------------------------------

#below starts the GUI loop
app.mainloop()
