from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def signup_form():
    return render_template('signup.html')

@app.route('/', methods=['POST'])
def signup_submit():
    data = {
        "full_name": request.form['full_name'],
        "dob": request.form['dob'],
        "gender": request.form['gender'],
        "age": request.form['age'],
        "phone": request.form['phone'],
        "address": request.form['address'],
        "emergency_contacts": [
            {
                "name": request.form['ec1_name'],
                "relation": request.form['ec1_relation'],
                "phone": request.form['ec1_phone'],
                "address": request.form['ec1_address'],
                "age": request.form['ec1_age'],
            },
            {
                "name": request.form['ec2_name'],
                "relation": request.form['ec2_relation'],
                "phone": request.form['ec2_phone'],
                "address": request.form['ec2_address'],
                "age": request.form['ec2_age'],
            },
            {
                "name": request.form['ec3_name'],
                "relation": request.form['ec3_relation'],
                "phone": request.form['ec3_phone'],
                "address": request.form['ec3_address'],
                "age": request.form['ec3_age'],
            },
        ],
        "email": request.form['email'],
        "password": request.form['password']
    }

    with open('signup_data.json', 'a') as f:
        f.write(json.dumps(data) + '\n')

    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)

