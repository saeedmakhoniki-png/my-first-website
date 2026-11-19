
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>اولین سایت من</title>

        <style>
            body {
                margin: 0;
                font-family: Tahoma;
                background: #101827;
                color: white;
                text-align: center;
            }

            .container {
                padding: 60px 20px;
            }

            h1 {
                color: #38bdf8;
                font-size: 32px;
            }

            p {
                color: #cbd5e1;
                font-size: 18px;
            }

            button {
                background: #0284c7;
                color: white;
                border: none;
                padding: 14px 30px;
                border-radius: 10px;
                font-size: 17px;
                cursor: pointer;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>به سایت من خوش آمدید</h1>
            <h1>سایت سعید</h1)
            <p>اولین پروژه واقعی من با Python</p>
            <button onclick="alert('سلام! سایت من کار می‌کند')">
                شروع کنیم
            </button>
        </div>
    </body>
    </html>
    """

