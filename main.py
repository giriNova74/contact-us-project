from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
#import email_validator

app = Flask(__name__)
app.secret_key = "this-is-app-secret-key"

class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = StringField(label='Message')
    submit = SubmitField(label="Log In")

@app.route("/", methods=["GET", "POST"])
def home():
    cform = contactForm()
    if cform.validate_on_submit():
        print(f"Name: {cform.name.data},E-mail: {cform.email.data},message: {cform.message.data}")
        
    else:
        print("Invalid Credentials")

    return render_template("contact.html", form=cform)

if __name__ == '__main__':
    app.run(debug=True)