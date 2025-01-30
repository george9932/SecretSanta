## 🎅 Secret Santa Assignment Script  

This Python script randomly assigns Secret Santa pairs and sends email notifications using the macOS Mail app. It reads participant names and emails from `participants.txt`, ensures no one is assigned to themselves, and sends assignments automatically.  

### Requirements  
- macOS with the Mail app  
- Python 3
- A text file (`participants.txt`) with names and emails in the format:  

Participant1 <participant1@example.com>  
Participant2 <participant2@example.com>  
Participant3 <participant3@example.com>  
... 

### Running the script  
 
```sh
python3 secret_santa.py
