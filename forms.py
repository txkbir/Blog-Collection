from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()], render_kw={"autofocus": True, "autocomplete": "off"})
    subtitle = StringField(label="Subtitle", validators=[DataRequired()], render_kw={"autocomplete": "off"})
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()], render_kw={"autocomplete": "off"})
    body = CKEditorField(label="Blog Content", validators=[DataRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField(label="SUBMIT POST")


# WTFrm to register new users
class RegisterForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()], render_kw={"autofocus": True, "autocomplete": "off"})
    password = PasswordField(label="Password", render_kw={"autocomplete": "off"})
    name = StringField(label="Name", validators=[DataRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField(label="SIGN ME UP!")


# WTForm to login existing users
class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()], render_kw={"autofocus": True, "autocomplete": "off"})
    password = PasswordField(label="Password", render_kw={"autocomplete": "off"})
    submit = SubmitField(label="LET ME IN!")    

# WTForm for users to leave comments below posts
class CommmentForm(FlaskForm):
    comment = CKEditorField(label="Comment", render_kw={"autocomplete": "off"})
    submit = SubmitField(label="POST COMMENT")
