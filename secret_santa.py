import os
import random
import subprocess

# Function to parse participants from the input file
def parse_participants(file_path):
    participants = []
    with open(file_path, 'r') as file:
        for line in file:
            name, email = line.strip().split('<')
            email = email.strip('>')
            participants.append({'name': name.strip(), 'email': email})
    return participants

# Function to assign Secret Santa pairs
def assign_secret_santa(participants):
    names = [p['name'] for p in participants]
    shuffled = names[:]
    random.shuffle(shuffled)

    # Ensure no one is assigned to themselves
    while any(a == b for a, b in zip(names, shuffled)):
        random.shuffle(shuffled)

    return {names[i]: shuffled[i] for i in range(len(names))}

# Function to send email using the Mail app (AppleScript)
def send_email_via_macos(recipient_email, subject, body):
    # AppleScript code, properly formatting the variables
    applescript = f'''
    tell application "Mail"
        set newMessage to make new outgoing message with properties {{subject:"{subject}", content:"{body}"}}
        tell newMessage
            make new to recipient at end of to recipients with properties {{address:"{recipient_email}"}}
            send
        end tell
    end tell
    '''

    # Run AppleScript using osascript
    subprocess.run(["osascript", "-e", applescript])

def main():
    input_file = 'participants.txt'

    # Parse participants and assign Secret Santa pairs
    participants = parse_participants(input_file)
    if len(participants) < 2:
        print("Not enough participants.")
        return

    assignments = assign_secret_santa(participants)

    # Send emails using Mail app
    for participant in participants:
        name = participant['name']
        recipient_name = assignments[name]
        recipient_email = participant['email']
        body = f"Hi {name}!\n\nYou are the Secret Santa for {recipient_name}!\n\nMerry Christmas!"
        send_email_via_macos(recipient_email, "Your Secret Santa Assignment", body)

if __name__ == "__main__":
    main()
