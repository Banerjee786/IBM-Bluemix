# IBM-Bluemix
Experiment with IBM Bluemix cloud provider, VCAP_SERVICES, and clustering earthquake data using IBM DB2 on cloud. Used Cloud Foundry (cf)
as CLI for deploying and checking the logs from the terminal.

This code reads the csv data put into IBM DB2 (database) and writes appropriate query to cluster the earthquake information based 
on their location.

How to Run the App :
* Clone the app to local drive using the command : git clone https://github.com/Banerjee786/IBM-Bluemix.git
* Navigate to the local path and open terminal (even Powershell will do). To start deployment type in : cf push PriyamSampleApp 
* After deployment, to check in the App URL, type in : cf apps
* Select the URL for PriyamSampleApp and open it in your favorite browser.

Tada ! The App works :)

