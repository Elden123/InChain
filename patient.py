class patient:
    def __init__ (self, data):
        self.doctorFirstName = data['doctorfirstname']
        self.doctorLastName = data['doctorlastname']
        self.patientFirstName = data['patientfirstname']
        self.patientLastName = data['patientlastname']
        self.diagnosis = data['diagnosis']
        self.diagnosisDate = data['diagnosisdata']
        self.conditionStart = data['conditionstart']
        self.html = {}

    def getDoctorFirstName():
        return(self.doctorFirstName)

    def getDoctorLastName():
        return(self.doctorLastName)

    def getPatientFirstName():
        return(self.patientFirstName)

    def getPatientLastName():
        return(self.patientLastName)

    def getDiagnosis():
        return(self.diagnosis)

    def getDiagnosisDate():
        return(self.diagnosisDate)

    def getConditionStart():
        return(self.conditionStart)

    def getDoctorPhone():
        return(self.getDoctorPhone)

    def getPatientPhone():
        return(self.getPatientPhone)

    def createHTML():
        self.html[str(getPatientFirstName())] =  "<!doctype html> <html> <head> <meta charset='UTF-8'> <title>InChain</title> <script> function handleThings() {var xmlHttp = new XMLHttpRequest();xmlHttp.open( 'GET', 'http://35.196.237.62/okay', false );xmlHttp.send( null );return xmlHttp.responseText;
 } </script> </head> <body> <div id='form' onsubmit='return false'> <h1 class='mdc_typography--display3' id='data'> Form </h1> <form> <div id='doctorfirstname'> First Name of Doctor: " + getDoctorFirstName() + " <input type='text' name = 'doctorfirstname'><br> </div> <div id='doctorlastname'> Last Name of Doctor: " + getDoctorLastName() + " <input type='text' name = 'doctorlastname'><br> </div> <div id='patientfirstname'> First Name of Patient: " + getPatientFirstName() + " <input type='text' name = 'patientfirstname'><br> </div> <div id='patientlastname'> Last Name of Patient: " + getPatientLastName() + " <input type='text' name = 'patientlastname'><br> </div> <div id='diagnosis'> " + getDiagnosis() + " Diagnosis: <input type='text' name = 'diagnosis'><br> </div> <div id='diagnosisdate'> Date of Diagnosis: " + getConditionStart() + " <input type='text' name = 'diagnosisdate'><br> </div> <button onclick='handleThings()' type='submit'>Submit</button> </form> </div> </body> </html> "

    def getHTML():
        return(self.html)

    def handler(self, namefirst):
        for key in self.html:
            if key == namefirst:
                return (self.html[key])
