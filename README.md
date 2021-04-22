# AWS-Assignment

# Create S3 bucket tiger-empid (Please ensure not to open the bucket to public)
![Screenshot (1)](https://user-images.githubusercontent.com/74641501/115660278-66f9dd00-a359-11eb-93af-22f7cc3a4753.png)

# Create files inside the buckets A,B,C.
## Putting file1.py in A, file2.py in B, file3.py in C folders
![Screenshot (2)](https://user-images.githubusercontent.com/74641501/115660657-facba900-a359-11eb-9701-bf8f8c3c0845.png)

# Creating a flask app that gets the folder name and lists the filename present in the corresponding folder. (Use Boto3 for reading the contents of the folder) and test the code in local
# Steps
a. Install awscli b. Open the terminal and enter the following command aws --configure c. Install flask
d. Clone the repository and go to the directory e. Run the app in local using command python3 app.py


# Open an ec2-instance and while creating the instance keep ssh port as it is and add new rule as custom TCP and port 8085 to allow traffic
![Screenshot (3)](https://user-images.githubusercontent.com/74641501/115661083-8e9d7500-a35a-11eb-8f31-924577539b3a.png)


# You can use this ssh command to login into ec2 instance using your local machine
![Screenshot (4)](https://user-images.githubusercontent.com/74641501/115661383-fce23780-a35a-11eb-870f-79242f0b2851.png)

# After that install all the required packages python,flask,boto3,nginx,gunicorn and then copy the file content of your local app into ec2 instance

# Then run python3 app.py

@Your url will be public ip adress:8085. This url will show your flask application

# Billing information
![Screenshot (5)](https://user-images.githubusercontent.com/74641501/115662067-12a42c80-a35c-11eb-922d-ec068c30e8eb.png)

![Screenshot (6)](https://user-images.githubusercontent.com/74641501/115662337-76c6f080-a35c-11eb-9758-3b38f73ffb99.png)
