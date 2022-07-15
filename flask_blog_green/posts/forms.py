from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed


class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Текст', validators=[DataRequired()])
    picture = FileField('Добавить фото к посту.', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Сохранить')


class CommentForm(FlaskForm):
    comment = StringField('Комментарий', validators=[DataRequired()])


