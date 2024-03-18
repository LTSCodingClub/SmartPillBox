import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from datetime import datetime
import json, os
import logging
import threading

from gpiozero import LED, Button
from time import sleep

# PillBox GPIO
#
# +5V 			(Red) 		- 	Pin 4
# GND 			(Black 		- 	Pin 6
# Spare GND 	(White)		-	Pin 16 	GPIO 23
# Sunday +V 	(Brown)		-	Pin 18 	GPIO 24
# Saturday +V	(Yellow) 	- 	Pin 22 	GPIO 25
# Evening GND 	(Orange)	-	Pin 24	GPIO 08
# Friday +V		(Green)		-	Pin 26	GPIO 07
# Thursday +V	(Blue)		-	Pin 28	GPIO 01
# Lunch GND		(Purple)	-	Pin 32	GPIO 12
# Wednesday +V	(Grey)		-	Pin 36	GPIO 16
# Morning GND	(White)		-	Pin 38	GPIO 20
# Tuesday +V	(Black)		-	Pin 40	GPIO 21
# Monday +V		(Brown)		-	Pin 37	GPIO 26

# Button Sig (White)	-	Pin 3	GPIO 2
# Button GND (Black)	-	Pin 14 GND

# We have a button which the user can press to signify that they have taken their pills
button = Button(2)


# Spare GND 	(White)		-	Pin 16 	GPIO 23
SpareGND = LED(23)
# Sunday +V 	(Brown)		-	Pin 18 	GPIO 24
SundayLED = LED(24)
# Saturday +V	(Yellow) 	- 	Pin 22 	GPIO 25
SaturdayLED = LED(25)
# Evening GND 	(Orange)	-	Pin 24	GPIO 08
EveningGND = LED(8)
# Friday +V		(Green)		-	Pin 26	GPIO 07
FridayLED = LED(7)
# Thursday +V	(Blue)		-	Pin 28	GPIO 01
ThursdayLED = LED(1)
# Lunch GND		(Purple)	-	Pin 32	GPIO 12
LunchGND = LED(12)
# Wednesday +V	(Grey)		-	Pin 36	GPIO 16
WednesdayLED = LED(16)
# Morning GND	(White)		-	Pin 38	GPIO 20
MorningGND = LED(20)
# Tuesday +V	(Black)		-	Pin 40	GPIO 21
TuesdayLED = LED(21)
# Monday +V		(Brown)		-	Pin 37	GPIO 26
MondayLED = LED(26)


MondayLED.off()
TuesdayLED.off()
WednesdayLED.off()
ThursdayLED.off()
FridayLED.off()
SaturdayLED.off()
SundayLED.off()

MorningGND.off()
LunchGND.off()
EveningGND.off()
SpareGND.off()

def flash_until_button_pressed_or_time_up(day,time,requiredTime):

    global button,event
    global SpareGND,SundayLED,SaturdayLED,EveningGND,FridayLED,ThursdayLED,LunchGND,WednesdayLED,MorningGND,TuesdayLED,MondayLED
    
    # The idea is to flash the LED for time seconds.
    # if the button gets pressed then stop flashing and return True (as in the person says that they took their pill
    # if the button doesn't get pressed within the time left, return False to let the carer know that there may be a problem.
    pillTaken=False
    MorningGND.off()
    LunchGND.off()
    EveningGND.off()
    SpareGND.off()
    
    # Establish which time zone we want:
    
    if time=="Morning":
        MorningGND.on()
    
    if time=="Lunch":
        LunchGND.on()
        
    if time=="Evening":
        EveningGND.on()
        
    if time=="Spare":
        SpareGND.on()
    
    # Establish the day

    # There must be a better way but this should work!
    
    if day=="Monday":
        
        flashTime=0
    
        while flashTime<=requiredTime:
        
            #Flash the LED
            MondayLED.on()
            # wait for 1 second or more
            button.wait_for_press(1)
            MondayLED.off()
            # wait for 1 second or more
            button.wait_for_press(1)
            if button.is_pressed:
                print("Button is pressed - so send email to say all fine")
                pillTaken=True
                flashTime=requiredTime+2
                
            flashTime=flashTime+2
            
            
    if day=="Tuesday":
        
        flashTime=0
    
        while flashTime<=requiredTime:
        
            #Flash the LED
            TuesdayLED.on()
            # wait for 1 second or more
            button.wait_for_press(1)
            TuesdayLED.off()
            # wait for 1 second or more
            button.wait_for_press(1)
            if button.is_pressed:
                print("Button is pressed - so send email to say all fine")
                pillTaken=True
                flashTime=requiredTime+2
                
            flashTime=flashTime+2
            
    if day=="Wednesday":
        
        flashTime=0
    
        while flashTime<=requiredTime:
        
            #Flash the LED
            WednesdayLED.on()
            # wait for 1 second or more
            button.wait_for_press(1)
            WednesdayLED.off()
            # wait for 1 second or more
            button.wait_for_press(1)
            if button.is_pressed:
                print("Button is pressed - so send email to say all fine")
                pillTaken=True
                flashTime=requiredTime+2
                
            flashTime=flashTime+2
            
    if day=="Thursday":
        
    
        flashTime=0
    
        while flashTime<=requiredTime:
        
            #Flash the LED
            ThursdayLED.on()
            # wait for 1 second or more
            button.wait_for_press(1)
            ThursdayLED.off()
            # wait for 1 second or more
            button.wait_for_press(1)
            if button.is_pressed:
                print("Button is pressed - so send email to say all fine")
                pillTaken=True
                flashTime=requiredTime+2
                
            flashTime=flashTime+2
            
    if day=="Friday":
        
        flashTime=0
    
        while flashTime<=requiredTime:
        
            #Flash the LED
            FridayLED.on()
            # wait for 1 second or more
            button.wait_for_press(1)
            FridayLED.off()
            # wait for 1 second or more
            button.wait_for_press(1)
            if button.is_pressed:
                print("Button is pressed - so send email to say all fine")
                pillTaken=True
                flashTime=requiredTime+2
                
            flashTime=flashTime+2
            
    if day=="Saturday":
        
        flashTime=0
    
        while flashTime<=requiredTime:
        
            #Flash the LED
            SaturdayLED.on()
            # wait for 1 second or more
            button.wait_for_press(1)
            SaturdayLED.off()
            # wait for 1 second or more
            button.wait_for_press(1)
            if button.is_pressed:
                print("Button is pressed - so send email to say all fine")
                pillTaken=True
                flashTime=requiredTime+2
                
            flashTime=flashTime+2
            
            
    if day=="Sunday":
        
        flashTime=0
    
        while flashTime<=requiredTime:
        
            #Flash the LED
            SundayLED.on()
            # wait for 1 second or more
            button.wait_for_press(1)
            SundayLED.off()
            # wait for 1 second or more
            button.wait_for_press(1)
            if button.is_pressed:
                print("Button is pressed - so send email to say all fine")
                pillTaken=True
                flashTime=requiredTime+2
                
            flashTime=flashTime+2
            
        
    MorningGND.off()
    LunchGND.off()
    EveningGND.off()
    SpareGND.off()
    
    
    SpareGND.off()
    SaturdayLED.off()
    return pillTaken




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


def send_mail(sender_email, sender_password, receiver_email, subject, message):
    print("send_mail - called")
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



def inform_carer(day, time, taken):
    

    global generalInfo
    
    # load the general information if necessary
    load_general()

    # This should send an email to the official caregiver

    patientFirstname=generalInfo[0]
    patientSurname=generalInfo[1]

    carerFirstname=generalInfo[2]
    carerSurname=generalInfo[3]

    # The following could be editable and stored in the general info .json file:
    
    sender_email = "****email****"  
    receiver_email = generalInfo[4]
    sender_password = "***Password****"
    
   
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
        message = message+"<br><br>Kindest regards<br><br>The smart pill box"
    else:
        
        subject = "Warning from the smart pill box"

        message = "Dear "+carerFirstname+",<br><br>At the moment, "+patientFirstname+" has NOT taken their pill(s) at the specified time of "+time+" on a "+day
        message = message+"<br>you may wish to investigate<br><br>"
        message = message+"<br><br>The smart pill box"
        
    print(message)
    send_mail(sender_email, sender_password, receiver_email, subject, message)



def medication_time():

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
    
    # Three chances to take the pill
    global numberOfTimesNotTaken
    
    #print(lunchHour,":",lunchMinute)
    # Compare the current time to see if it falls within a pill reminder boundary
    if testTime.hour==morningHour:
        
        if testTime.minute == morningMinute:
            
            # It is time to take a pill from today's morning compartment
            print("It is time to take a pill from today's morning compartment")
            if flash_until_button_pressed_or_time_up(testDay,"Morning",20):
                print("Pill taken")
                if sentEmail==False:
                    
                    inform_carer(str(testDay), str(morningHour)+":"+str(morningMinute), True)
                    sentEmail=True
                sleep(60)
            else:
                print("Pill not taken!")
                print(numberOfTimesNotTaken)
                if numberOfTimesNotTaken >=3:
                    # Three chances to take the pill
                    numberOfTimesNotTaken = 0
                    if sentEmail==False:
                        
                        inform_carer(str(testDay), str(morningHour)+":"+str(morningMinute), False)
                        sentEmail=True
    
    if testTime.hour==lunchHour:
        
        if testTime.minute == lunchMinute:
            
            # It is time to take a pill from today's lunch compartment
            print("It is time to take a pill from today's lunch compartment")
            if flash_until_button_pressed_or_time_up(testDay,"Lunch",20):
                print("Pill taken")
                if sentEmail==False:
                    
                    inform_carer(str(testDay), str(lunchHour)+":"+str(lunchMinute), True)
                    sentEmail=True
                sleep(60)
            else:
                print("Pill not taken!")
                numberOfTimesNotTaken =numberOfTimesNotTaken +1
                print(numberOfTimesNotTaken)
                if numberOfTimesNotTaken >=3:
                    # Three chances to take the pill
                    numberOfTimesNotTaken = 0
                    if sentEmail==False:
                        
                        inform_carer(str(testDay), str(lunchHour)+":"+str(lunchMinute), False)
                        sentEmail=True
                        
            
    if testTime.hour==eveningHour:
        
        if testTime.minute == eveningMinute:
            
            # It is time to take a pill from today's evening compartment
            print("It is time to take a pill from today's evening compartment")
            if flash_until_button_pressed_or_time_up(testDay,"Evening",20):
                print("Pill taken")
                if sentEmail==False:
                    
                    inform_carer(str(testDay), str(eveningHour)+":"+str(eveningMinute), True)
                    sentEmail=True
                sleep(60)
            else:
                print("Pill not taken!")
                numberOfTimesNotTaken =numberOfTimesNotTaken +1
                print(numberOfTimesNotTaken)
                if numberOfTimesNotTaken >=3:
                    # Three chances to take the pill
                    numberOfTimesNotTaken = 0
                    if sentEmail==False:
                        
                        inform_carer(str(testDay), str(eveningHour)+":"+str(eveningMinute), False)
                        sentEmail=True
                        
                        
    if testTime.hour==spareHour:
        
        if testTime.minute == spareMinute:
            
            # It is time to take a pill from today's spare compartment
            print("It is time to take a pill from today's spare compartment")
            if flash_until_button_pressed_or_time_up(testDay,"Spare",20):
                print("Pill taken")
                sleep(60)
                if sentEmail==False:
                    
                    inform_carer(str(testDay), str(spareHour)+":"+str(spareMinute), True)
                    sentEmail=True
            else:
                print("Pill not taken!")

                numberOfTimesNotTaken =numberOfTimesNotTaken +1
                

                if numberOfTimesNotTaken >=3:
                    
                    if sentEmail==False:
                        # Three chances to take the pill
                        numberOfTimesNotTaken = 0
                        inform_carer(str(testDay), str(spareHour)+":"+str(spareMinute), False)
                        sentEmail=True
                    
# Main program
# Three chances to take the pill
numberOfTimesNotTaken = 0
    
sentEmail=False

# Set up a base date for the file comparison - to avoid loaduing the same files unnecessarily.
last_modified_time=datetime(2024, 3, 7)

event = threading.Event()


while True:

    
    # load the schedule if it has changed
    load_schedule()

    # Now we need to check if is time for a pill... 
    medication_time()
    # wait for 1 second or more
    event.wait(1)
