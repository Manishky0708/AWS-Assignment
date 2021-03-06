# Importing necessary libraries

from flask import Flask
import boto3
from boto3.session import Session
from flask import Flask, request, render_template 

# Constructor
app = Flask(__name__)

# Setting app route
@app.route("/", methods =["GET","POST"])

# Index Fuction
def index():
    results = []
    if request.method == "POST":
        dir = request.form.get("fname")
        results=list_files(dir)
    return render_template("index.html",results=results)  

# Function to get the filenames in the folders of AWS Bucket
def list_files(dir):
    # AWS Credentials
    AWS_STORAGE_BUCKET_NAME='tiger-empid'
    AWS_S3_REGION_NAME='ap-south-1'
    bucket_name='tiger-empid'

    file_list=[]
    session = Session()
    s3 = session.resource('s3')
    for obj in s3.Bucket(bucket_name).objects.filter(Prefix=dir).all():
        file_name=obj.key.split(dir + "/")[1]
        print(file_name)
        if len(file_name)>0:
            file_list.append(file_name)
    return file_list

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8085)
