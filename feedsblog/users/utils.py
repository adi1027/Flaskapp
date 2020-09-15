import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from feedsblog import mail


def save_picture(img):
    rand=secrets.token_hex(9)
    _,file_ext=os.path.splitext(img.filename)
    picture=rand+file_ext
    pic_path=os.path.join(current_app.root_path,'static/profile_pics',picture)
    out_size=(125,125)
    i=Image.open(img)
    i.thumbnail(out_size)
    i.save(pic_path)
    return picture

def send_reset_password(user):
    token=user.get_reset_token()
    msg=Message('Message for password reset',sender='noreply@demo.com',recipients=[user.email])
    msg.body=f'''To reset password visit the link 
    {url_for("users.reset_password",token=token,_external=True)}'''
    mail.send(msg)
