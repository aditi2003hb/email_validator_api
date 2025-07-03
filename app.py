from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def is_valid_email(email):
    return len(email) == 6

def is_valid_password(password):
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_+=<>?/|\\{}[]:;" for c in password)
    return has_upper, has_digit, has_special

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        if not is_valid_email(email):
            message = "Email must be exactly 6 characters long."
        else:
            has_upper, has_digit, has_special = is_valid_password(password)
            if not (has_upper and has_digit and has_special):
                message = "Password must have 1 uppercase, 1 digit, and 1 special character."
            elif password != confirm_password:
                message = "Passwords do not match."
            else:
                message = "✅ All fields are valid."

    return render_template("index.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)
