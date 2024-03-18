from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Write schedule to file
def write_list(fileName,listName):
    print("Started writing list data into a json file")
    with open(fileName, "w") as fp:
        json.dump(listName, fp)
        print("Done writing JSON data into .json file")

# Read list to memory
def read_list(fileName):
    # for reading also binary mode is important
    with open(fileName, 'rb') as fp:
        n_list = json.load(fp)
        return n_list    

# Website interaction code       
@app.route('/')
def index():
   return render_template('index.html', emailChanged = False, scheduledChanged = False)

@app.route('/schedule')
def displaySchedule():

   global morningList
   global lunchList
   global eveningList
   global spareList
   
   morningList=read_list("MorningList.json")
   lunchList=read_list("LunchList.json")
   eveningList=read_list("EveningList.json")
   spareList=read_list("SpareList.json")
   
 
   
   print("Displaying the current schedule")
   print(morningList)
   print(lunchList)
   print(eveningList)
   print(spareList)
   

   
   boolean = False
   #True
   # Pass the variable to the HTML template
   return render_template('schedule.html',
                          mondayMorning = morningList[0],
                          tuesdayMorning = morningList[1],
                          wednesdayMorning = morningList[2],
                          thursdayMorning = morningList[3],
                          fridayMorning = morningList[4],
                          saturdayMorning = morningList[5],
                          sundayMorning = morningList[6],
                          
                          mondayLunch = lunchList[0],
                          tuesdayLunch = lunchList[1],
                          wednesdayLunch = lunchList[2],
                          thursdayLunch = lunchList[3],
                          fridayLunch = lunchList[4],
                          saturdayLunch = lunchList[5],
                          sundayLunch = lunchList[6],
                          
                          mondayEvening = eveningList[0],
                          tuesdayEvening = eveningList[1],
                          wednesdayEvening = eveningList[2],
                          thursdayEvening = eveningList[3],
                          fridayEvening = eveningList[4],
                          saturdayEvening = eveningList[5],
                          sundayEvening = eveningList[6],
                          
                          mondaySpare = spareList[0],
                          tuesdaySpare = spareList[1],
                          wednesdaySpare = spareList[2],
                          thursdaySpare = spareList[3],
                          fridaySpare = spareList[4],
                          saturdaySpare = spareList[5],
                          sundaySpare = spareList[6],
                          
                          my_boolean=boolean)
   
@app.route('/setSchedule',methods=['POST'])
def setSchedule():
    global morningList
    global lunchList
    global eveningList
    global spareList
    
    print("Setting the current schedule")
 
    error = None
    if request.method == 'POST':
        
        # Get the morning times
        morningList[0] = request.form['monMorning']
        morningList[1] = request.form['tueMorning']
        morningList[2] = request.form['wedMorning']
        morningList[3] = request.form['thursMorning']
        morningList[4] = request.form['friMorning']
        morningList[5] = request.form['satMorning']
        morningList[6] = request.form['sunMorning']
        
        # Get the lunch times
        lunchList[0] = request.form['monLunch']
        lunchList[1] = request.form['tueLunch']
        lunchList[2] = request.form['wedLunch']
        lunchList[3] = request.form['thursLunch']
        lunchList[4] = request.form['friLunch']
        lunchList[5] = request.form['satLunch']
        lunchList[6] = request.form['sunLunch']
      
        # Get the evening times
        eveningList[0] = request.form['monEvening']
        eveningList[1] = request.form['tueEvening']
        eveningList[2] = request.form['wedEvening']
        eveningList[3] = request.form['thursEvening']
        eveningList[4] = request.form['friEvening']
        eveningList[5] = request.form['satEvening']
        eveningList[6] = request.form['sunEvening']
        
        # Get the spare times
        spareList[0] = request.form['monSpare']
        spareList[1] = request.form['tueSpare']
        spareList[2] = request.form['wedSpare']
        spareList[3] = request.form['thursSpare']
        spareList[4] = request.form['friSpare']
        spareList[5] = request.form['satSpare']
        spareList[6] = request.form['sunSpare']
        
        # Save the details to the appropriate files
        write_list("MorningList.json",morningList)
        write_list("LunchList.json",lunchList)
        write_list("EveningList.json",eveningList)
        write_list("SpareList.json",spareList)
        
   
    # display the index but message the user that a change has been made
    
    return render_template('index.html', emailChanged = False, scheduledChanged = True)

 

@app.route('/email')
def email():
    error = None
    global generalInfo    
    generalInfo=read_list("generalInfo.json")
    return render_template('email.html',
                           patientFirstname=generalInfo[0],patientSurname=generalInfo[1],
                           carerFirstname=generalInfo[2],carerSurname=generalInfo[3],
                           carerEmail=generalInfo[4])

@app.route('/emailSet', methods=['POST'])
def emailSet():
    
    error = None
    
    global generalInfo

    if request.method == 'POST':

        # Get the information
        generalInfo[0] = request.form['pfname']
        generalInfo[1] = request.form['plname']
        generalInfo[2] = request.form['cfname']
        generalInfo[3] = request.form['clname']
        generalInfo[4] = request.form['cemail']

        # Save it to the appropriate file
        write_list("generalInfo.json",generalInfo)
 
    return render_template('index.html', emailChanged = True, scheduledChanged = False)

   


if __name__ == '__main__':
        
    app.run(debug=True, host='0.0.0.0') # Change host to your Raspberry Pi address
    print("Running")
