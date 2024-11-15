import re

def email_validation(email):
    error_msg = ""
    email_re = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not email:
        error_msg = "*Please provide your email address!"
    elif (re.fullmatch(email_re, email)):
        error_msg = "*Invalid email address!"
   

    return error_msg

def full_name_validation(name):
    error_msg = ""

    if not name:
        error_msg = "*Please provide your full name!"
    elif len(name) < 6:
        error_msg = "*Full name must have minimum of 6 characters"
    elif len(name) > 30:
        error_msg = "*Full name must not exceed 30 characters!"
    elif re.search(r"[^A-Za-z\s]",name):
        error_msg = "*Full name must not any number and special symbols!"

    return error_msg

def password_validation(password):
    error_msg = ""

    if not password:
        error_msg = "*Password cannot be empty!"
    elif len(password) < 6:
        error_msg = "*Password must have minimum of 6 characters!"
    elif not re.search(r"[A-Z]",password):
        error_msg = "*Password must contain at least one uppercase letter!"
    elif not re.search(r"[a-z]",password):
        error_msg = "*Password must contain at least one lowercase letter!"
    elif not re.search(r"[0-9]",password):
        error_msg = "*Password must contain at least one number!"
    elif not re.search(r"[^A-Za-z0-9]",password):
        error_msg = "*Password must contain at least one special symbols (E.g @#$%^&?)!"
    elif re.search(r"\s", password): 
        error_msg = "*Password cannot contain spaces!"

    return error_msg

def current_old_password_validation(old_password, entered_password):
    error_msg = ""
    if not old_password:
        error_msg = "*Current password cannot be empty!"
    elif old_password != entered_password:
        error_msg = "*Entered current password does not match with your old password!"

    return error_msg

def confirm_password_validation(password, confirm_password):
    error_msg = ""

    if not confirm_password:
        error_msg = "*Confirm password cannot be empty!"
    if password != confirm_password:
        error_msg = "*Your password does not match with your confirm password!"

    return error_msg