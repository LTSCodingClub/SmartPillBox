import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from datetime import datetime
import json, os
import logging
import threading
## Set up fake times
morningList = ['10:00','10:00','10:00','10:00','10:00','10:00','10:00']
lunchList = ["13:00","13:00","13:00","13:00","13:00","13:00","13:00"]
eveningList = ["15:00","15:00","15:00","15:00","15:00","15:00","15:00"]
spareList = ["19:00","19:00","19:00","19:00","19:00","19:00","19:00"]
generalInfo = ["none","none","none","none","none@none.com"]

def get_file_last_modified_time(file_path):
    if os.path.exists(file_path):
        timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(timestamp)
    else:
        return None
    
# Read list to memory
def read_list(fileName):
    # for reading also binary mode is important
    with open(fileName, 'rb') as fp:
        n_list = json.load(fp)
        return n_list

def load_general():
    global generalInfo    

    latest_modified_time = get_file_last_modified_time("generalInfo.json")
    
    if latest_modified_time != last_modified_time:
        
        print("Contact information has been updated")
        generalInfo=read_list("generalInfo.json")


def load_schedule():

    global morningList
    global lunchList
    global eveningList
    global spareList
    global last_modified_time
    
    latest_modified_time = get_file_last_modified_time("MorningList.json")
    #print("latest_modified_time = ",latest_modified_time)
    
    if latest_modified_time != last_modified_time:
        
        print("Schedule has been updated")
        morningList=read_list("MorningList.json")
        lunchList=read_list("LunchList.json")
        eveningList=read_list("EveningList.json")
        spareList=read_list("SpareList.json")
        print("Displaying the current schedule")
        print(morningList)
        print(lunchList)
        print(eveningList)
        print(spareList)
        last_modified_time = latest_modified_time
        print(last_modified_time)

    #else:
          
       # print("No changes to the schedule")


def sendmail(sender_email, sender_password, receiver_email, subject, message):
    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Create a secure SSL context
    context = smtplib.SMTP(smtp_server, port)
    context.starttls()

    # Log in to the SMTP server
    context.login(sender_email, sender_password)

    # Construct the message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add message body - HTML format!
    msg.attach(MIMEText(message, 'html'))

    # Send the email
    context.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the connection
    context.quit()



def informCarer(day, time, taken):

    global generalInfo
    
    # load the general information if necessary
    load_general()

    # This should send an email to the official caregiver

    patientFirstname=generalInfo[0]
    patientSurname=generalInfo[1]

    carerFirstname=generalInfo[2]
    carerSurname=generalInfo[3]

    # The following could be editable and stored in the general info .json file:
    
    sender_email = "####Enter your address####"  
    receiver_email = generalInfo[4]
    sender_password = "####Enter your password####"
    
   
    # Now send an email...
    #
    # the day is Monday > Sunday (not the date) although the email will automatically have the date when sent.
    #
    # the time is the time that the pill was highlighted (supposed to be taken)
    #
    # the flag take is a boolean flag to say True - Patient took the pill or False patient has not yet taken the pill.
    #
    #

    if taken:
            
        subject = "Good news from the smart pill box"

        message = "Dear "+carerFirstname+",<br><br>This is just to let you know that "+patientFirstname+" has taken their pill(s) at "+time
        message = message+"<br><br>The smart pill box"
    else:
        
        subject = "Warning from the smart pill box"

        message = "Dear "+carerFirstname+",<br><br>At the moment, "+patientFirstname+" has NOT taken their pill(s) at the specified time of "+time+" on a "+day
        message = message+"<br>you may wish to investigate<br><br>"
        message = message+"<br><br>The smart pill box"
        
    sendmail(sender_email, sender_password, receiver_email, subject, message)



def medicationTime():

    global morningList
    global lunchList
    global eveningList
    global spareList
    global sentEmail
    
    testTime=datetime.now()
    #print (testTime)
    testDay=testTime.strftime("%A")
    #print(testDay)
    #print(testTime.minute)
    #print(testTime.hour)
    
    # Which Day is it?
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Spare"]
    offset=days.index(testDay)
    #print(offset)

    # Get the times as hours and minutes
    morningString=morningList[offset]
    morningHour=int(morningString[0:2])
    morningMinute=int(morningString[3:5])
    
    
    lunchString=lunchList[offset]
    lunchHour=int(lunchString[0:2])
    lunchMinute=int(lunchString[3:5])
    

    eveningString=eveningList[offset]
    eveningHour=int(eveningString[0:2])
    eveningMinute=int(eveningString[3:5])
    
    spareString=spareList[offset]
    spareHour=int(spareString[0:2])
    spareMinute=int(spareString[3:5])
    
    #print(lunchHour,":",lunchMinute)
    # Compare the curret time to see if it falls within a pill reminder boundary
    if testTime.hour==morningHour:
        
        if testTime.minute == morningMinute:
            
            # It is time to take a pill from today's morning compartment
            print("It is time to take a pill from today's morning compartment")
    
    if testTime.hour==lunchHour:
        
        if testTime.minute == lunchMinute:
            
            # It is time to take a pill from today's lunch compartment
            print("It is time to take a pill from today's lunch compartment")
            
    if testTime.hour==eveningHour:
        
        if testTime.minute == eveningMinute:
            
            # It is time to take a pill from today's evening compartment
            print("It is time to take a pill from today's evening compartment")
            
    if testTime.hour==spareHour:
        
        if testTime.minute == spareMinute:
            
            # It is time to take a pill from today's spare compartment
            print("It is time to take a pill from today's spare compartment")

    if debugging:
        # Test debugging code - set to a close time for testing - remove or disable for production version
        if testTime.hour==17:
            
           # print("Correct Hour")
            if testTime.minute == 28:
                
                # It is time to take a pill from today's spare compartment
                print("It is time to take a pill from today's debugging compartment")
                if sentEmail==False:
                    
                    informCarer("Saturday", "17:20", True)
                    sentEmail=True
        
# Main program

# Set a flag for debugging and development - don't forget to switch to flase!
debugging=True
sentEmail=False

# Set up a base date for the file comparison - to avoid loaduing the same files unnecessarily.
last_modified_time=datetime(2024, 3, 7)

event = threading.Event()

while True:

    
    # load the schedule if it has changed
    load_schedule()

    # Now we need to check if is time for a pill... 
    medicationTime()
    # wait for 1 second or more
    event.wait(1)
    
    

    
            



