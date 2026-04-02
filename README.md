# angelv1
This is my senior project for my own AI assistant


**Here is the Project structure**:
angel_ai/  
│  
├── main.py  
│  
├── gui/  
│ └── interface.py  -> library needed customtkinter
│  
├── voice/  
│ ├── listen.py  -> speechrecognition + pyaudio
│ └── speak.py  -> pyttsx3
│  
├── brain/  
	│ ├── ai.py   -> 
│ └── memory.py  -> starting simple, maybe JSON   
├──memory.json -> keep angels memory
├── safety/  
│ └── respect_filter.py -> better-profanity
and dotenv -(keeps api keys)
