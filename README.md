# CS-510-Email-Organizer

# How to run my project 
* Go to my github link and download the Email.py file
* Now, login to your personal google account on chrome and open Apps Script (do not use business account for now as that would need additional permissions from the admin and google to run the script on gmail)
* Click on ‘Start Scripting’ on Apps script
* Click on “New Project”
* Now go back to my Email.py file and open it on VS code
  
  - If you are using my code for the first time, please directly run the Email.py file and add your labels to it, else, please update the prompt guideline in Email.py file with the most current script from your Apps Script to successfully add labels to the email.
    
* Now replace the Gemini API key with your generated API key 
* Run the python file using command: python3 Email.py
* Enter the input requests in the command line and wait for the updated code to be generated
* Copy the updated code from the command line and paste it on the Apps script
* On the side panel on Apps Scripts, under services add “Gmail”
* Click the “Run” button on Apps Script
* For first time users - it’ll prompt for gmail authentication, click “allow” to grant permissions
* Once it starts executing, wait for it to complete 
* On completion, check inbox - The labels should be created and emails should be organized in them
  -  Pls Note: Run the Apps Script for the same account you want the inbox to be manipulated  for 
