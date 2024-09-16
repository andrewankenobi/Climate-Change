from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Carbon Footprint Estimator</title>
        <link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap" rel="stylesheet"> 
        <style>
          body {
            background-color: #FBBD05;
            font-family: 'Poppins', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
          }

          h1, p {
            text-align: center;
          }

          img {
            width: 200px; 
            border-radius: 18px;
            margin-bottom: 20px; 
          }

          df-messenger {
            z-index: 999;
            position: fixed;
            --df-messenger-font-color: #777777;
            --df-messenger-font-family: 'Poppins', sans-serif;
            --df-messenger-chat-background: #f3f6fc;
            --df-messenger-message-user-background: #d3e3fd;
            --df-messenger-message-bot-background: #fff;
            bottom: 16px;
            right: 16px;
          }
        </style>
    </head>
    <body>
        <img src="{{ url_for('static', filename='logo.png') }}" alt="Logo"> 
        <h1>Welcome to the Carbon Footprint Estimator</h1>
        <p>Use the chat to the right to interact with our AI assistant.</p>
        
        <link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
<script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
<df-messenger
  oauth-client-id="222594707808-2mi8qavcli7cvqjgkt9trmdjq44kd7uv.apps.googleusercontent.com"
  location="us-central1"
  project-id="argon-zoo-413112"
  agent-id="63c7e607-a4ae-45f1-8096-688f2143901a"
  language-code="en"
  max-query-length="-1">
 <df-messenger-chat
   chat-title="Carbon Footprint">
  </df-messenger-chat>
</df-messenger>
<style>
  df-messenger {
    z-index: 999;
    position: fixed;
    bottom: 0;
    right: 0;
    top: 0;
    width: 450px;
  }
</style>

    </body>
    </html>
    """
    return render_template_string(html_content)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
