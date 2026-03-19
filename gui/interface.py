import customtkinter 

#below creates the main app window
app = customtkinter.CTk()

#----------CUSTOMIZATION--------------------------------------
#below sets the title of the app window
app.title("Angel AI")
#below sets the mode + theme of the app window
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")  
#below sets the size of the app window
app.geometry("400x300")
#---------------------------------------------------------------

#below starts the GUI loop
app.mainloop()
