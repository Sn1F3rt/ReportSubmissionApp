import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from quart import request, render_template, redirect, url_for, flash

from blueprints.meta import meta_bp

import config
from forms import SendReportForm


def send_email(email: str, message: str, files: list):
    sender_email = config.SMTP_USERNAME
    receiver_email = email

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Report Submission"

    body = f"Message: {message}"
    msg.attach(MIMEText(body, "plain"))

    for file in files:
        media_attachment = MIMEApplication(file.read(), "octet-stream")
        media_attachment.add_header(
            "Content-Disposition", "attachment", filename=file.filename
        )
        msg.attach(media_attachment)

    with smtplib.SMTP(config.SMTP_HOST, config.SMTP_PORT) as server:
        server.starttls()
        server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
        server.sendmail(sender_email, receiver_email, msg.as_string())


@meta_bp.route("/", methods=["GET", "POST"])
async def _index():
    form = await SendReportForm().create_form()

    if await form.validate_on_submit():
        email = form.email.data
        message = form.message.data

        files = (await request.files).getlist("media")

        send_email(email, message or "None", files)

        await flash("Email sent.", "success")

        return redirect(url_for("meta._index"))

    return await render_template("meta/index.html", form=form)
