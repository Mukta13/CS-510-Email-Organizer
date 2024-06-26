# CS-510-Email-Organizer
* Automatically creates labels for new and unread emails in the Gmail inbox, leveraging Google Apps Script to handle the required user authentication and server permissions.
* While developments on Gmail require user authentication and server permissions, this is a personal project that only requires authentication for my own Gmail account, which can be achieved through Google Apps Script running on Google's servers.
* Currently, I have successfully implemented the ability to automatically create labels for my emails through an open-source script that users can download and run on Apps Script to ensure authentication for their respective accounts.
* Leveraged Large Language Models such as Gemini AI to read and modify my existing code, enabling users to easily add their own customizations for label creation based on their specific needs and requests.

# How to run my project 
1. Download the Email.py file
1. Now, login to your personal google account on chrome and open Apps Script (do not use business account for now as that would need additional permissions from the admin and google to run the script on gmail)
1. Click on ‘Start Scripting’ on Apps script
1. Click on “New Project”
1. Now go back to my Email.py file and open it on VS code
  1. If you are using my code for the first time, please directly run the Email.py file and add your labels to it
  2. Else, please update the prompt guideline in Email.py file with the most current script from your Apps Script to successfully add labels to the email.
1. Now replace the Gemini API key with your generated API key 
1. Run the python file using command: ``` $ python3 Email.py   ```
1. Enter the input requests in the command line and wait for the updated code to be generated
1. Copy the updated code from the command line and paste it on the Apps script
1. On the side panel on Apps Scripts, under services add “Gmail”
1. Click the “Run” button on Apps Script
1. For first time users - it’ll prompt for gmail authentication, click “allow” to grant permissions
1. Once it starts executing, wait for it to complete 
1. On completion, check inbox - The labels should be created and emails should be organized in them

*Pls Note: Run the Apps Script for the same account you want the inbox to be manipulated  for*
