from quart_wtf import QuartForm
from quart_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from wtforms import StringField, TextAreaField
from wtforms.validators import Length, Email, DataRequired


class SendReportForm(QuartForm):
    email = StringField(
        "Email: ",
        validators=[Email(), DataRequired()],
    )

    message = TextAreaField(
        "Message: ",
        validators=[Length(max=1000)],
    )

    # noinspection PyTypeChecker
    media = FileField(
        "Media",
        validators=[
            FileRequired(),
            FileAllowed(
                ["jpg", "jpeg", "png", "mp4"], "Only images and videos are allowed."
            ),
            FileSize(100 * 1024 * 1024),
        ],
    )
