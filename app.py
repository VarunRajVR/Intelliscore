from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
from datetime import datetime, timedelta
from functools import wraps
import uuid
secret_key = uuid.uuid4().hex


app = Flask(__name__)

role = "Teacher"

@app.route('/teacher')
def home_teacher():
    return render_template('teacher.html')

@app.route('/upload_test', methods=['POST'])
def upload_file():
	test_id = uuid.uuid4().hex
	test_name = request.form['test_name']
	eligibility = request.form['eligibility']
	uploaded_files = request.files.getlist("file[]") 
	for uploaded_file in uploaded_files:
		if uploaded_file.filename != '':
			uploaded_file.save(f"./Users/{uploaded_file.filename}") # Use database to store files
			if uploaded_file.filename.endswith('.csv'):
				question_bank_name = uploaded_file.filename
	            
	test = {
	        "test_id": test_id,
            "test_name": test_name,
            "eligibility": eligibility,
    }
	
	return render_template('report.html') 

@app.route('/student')
def home_student():
	    return render_template('student.html')
        

if __name__ == "__main__":
    app.run(debug=True)