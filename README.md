- System-level command execution (launching apps, handling tasks)
- Modular architecture for scalability and future enhancements

## Tech Stack
- Language: Python
- Libraries: SpeechRecognition, pyttsx3 (or your TTS library), OS module
- Environment: Windows

## Key Contributions
- Developed voice interaction pipeline (input → processing → output)
- Implemented multiple voice commands for system automation
- Designed modular components for maintainability and scalability
- Debugged and optimized performance for smoother interaction

## Challenges & Solutions
- **Challenge:** Handling inconsistent voice input  
  **Solution:** Improved command parsing and error handling

- **Challenge:** Synchronizing input and output processing  
  **Solution:** Structured execution flow to improve responsiveness

## Future Improvements
- Add natural language processing (NLP) for better understanding
- Improve voice realism and customization
- Integrate APIs for web-based tasks (weather, search, etc.)
- Add GUI for enhanced user interaction

## Status
In active development with ongoing feature expansion

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
