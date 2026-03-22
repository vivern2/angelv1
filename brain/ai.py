

#Below is a test of the function get_response() to connect it to the gui
def get_response(text):
    text = text.lower()
    if "hello" in text:
        return "Hello! I'm Angel. How can I assist you today?"
    if "population of cuba?" in text:
        return "The population of Cuba is approximately 11 million people."
    
    return "Sorry, I don't understand that yet. I'm still learning!"