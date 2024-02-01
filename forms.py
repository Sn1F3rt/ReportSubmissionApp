from quart_wtf import QuartForm
from quart_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import Length, Email, DataRequired


class SendReportForm(QuartForm):
    email = StringField(
        "Email: ",
        validators=[Email(), DataRequired()],
    )

    # noinspection PyTypeChecker
    image = FileField(
        "Image",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "png"], "Images only!"),
        ],
    )

    message = TextAreaField(
        "Message: ",
        validators=[Length(max=1000)],
    )
