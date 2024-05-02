
import google.generativeai as genai
import json
print(" ")
label_name = input("Enter the name of the label you want to add: ")
from_keyword = input("Enter the keyword to detect in the from (optional, press Enter to skip): ")
body_keywords_str = input("Enter keywords to detect in the body separated by commas (optional, press Enter to skip): ")
subject_keywords_str = input("Enter keywords to detect in the subject separated by commas (optional, press Enter to skip): ")
print(" ")
body_keywords = body_keywords_str.split(",") if body_keywords_str else []
subject_keywords = subject_keywords_str.split(",") if subject_keywords_str else []

prompt_param = {
        "label name": label_name,
        "contains from": from_keyword,
        "contains body": body_keywords,
        "contains subject": subject_keywords
    }


prompt_param_json = json.dumps(prompt_param)

def generate_prompt(prompt_param):
    print(" ")
    print('Generating the code for you to copy to Apps Script.......')
    print(" ")
    print('-------------------------------------------------------------------------')
    print(" ")

    genai.configure(api_key='AIzaSyAc85igu8tijFrtNRPgfhkCu6AQEzGbhqw')

    #Update the code with your recent App Scripts code to update the labels - dynamic updates implementation is a futre work

    guidelines= r"""Strictly follow these instructions and return just what is asked for. 

Use this code, understand it and then add a code block to it to implement the addition of labels to the emails according to the given instructions:



function processUnreadEmails() {
  const threads = GmailApp.search('is:unread');
  threads.forEach(function(thread) {
    const messages = thread.getMessages();
    messages.forEach(function(message) {
      processMessage(message);
    });
  });
}

function processMessage(message) {
  const from = message.getFrom();
  const subject = message.getSubject().toLowerCase();
  const body = message.getPlainBody().toLowerCase();
  console.log(from, subject, body)
  console.log(/.+@illinois\.edu/.test(from) )

  const thread = message.getThread(); 
  // CS Courses label
  if (/.+@illinois\.edu/.test(from) && (subject.includes("510") || subject.includes("cs 510") || body.includes("510") || body.includes("cs 510"))) {
    createLabelIfNeeded("CS 510");
    const labelToAdd = GmailApp.getUserLabelByName("CS 510"); // Get the existing label
    thread.addLabel(labelToAdd); // Add the label to the thread
    console.log("CS 510 label added to the thread");
  }
  // Job Applications label
  else if (!/.+@illinois\.edu/.test(from) && /(job|resume|interview|internship|internships|thanks for applying)/.test(body)) {
    createLabelIfNeeded("Job related");
    const labelToAdd = GmailApp.getUserLabelByName("Job related"); // Get the existing label
    thread.addLabel(labelToAdd); // Add the label to the thread
    console.log("Job related added to the thread");
  }
  // School or Work label (except CS)
  else if (/.+@illinois\.edu/.test(from) && !subject.includes("510") && !subject.includes("CS 510") && !body.includes("510") && !body.includes("cs 510")) {
    createLabelIfNeeded("School or Work");
    const labelToAdd = GmailApp.getUserLabelByName("School or Work"); // Get the existing label
    thread.addLabel(labelToAdd); // Add the label to the thread
    console.log("School or Work added to the thread");
  }
}

function createLabelIfNeeded(labelName) {
  const label = GmailApp.getUserLabelByName(labelName);
  console.log(!label);
  if (!label) {
    GmailApp.createLabel(labelName);
  }
}
function main() {
  const triggers = ScriptApp.getProjectTriggers();
  let triggerExists = false;
  for (let i = 0; i < triggers.length; i++) {
    if (triggers[i].getHandlerFunction() === "processUnreadEmails") {
      triggerExists = true;
      break;
    }
  }
  if (!triggerExists) {
    ScriptApp.newTrigger("processUnreadEmails")
      .timeBased()
      .everyMinutes(1)
      .create();
  }
}

Give the complete code. Make sure you are following the exact same format as the existing code. 
 """

    # prompt_param=json.dumps(param)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(guidelines+prompt_param_json)
    print(response.text)
    return response.text

generate_prompt(prompt_param)
