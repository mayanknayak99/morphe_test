from flask import Flask, send_from_directory, Response
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
   
    username =  "mayanknayak99"

    
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    ist_time_str = ist_time.strftime("%Y-%m-%d %H:%M:%S IST")

    
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        top_output = str(e)

    
    return f"""
    <html>
    <head><title>HTOP Endpoint</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> Mayank Nayak</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time_str}</p>
        <h2>Top Command Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """


@app.route('/favicon.ico')
def favicon():
    return Response(status=204)  


@app.route('/apple-touch-icon.png')
@app.route('/apple-touch-icon-precomposed.png')
def apple_icon():
    return Response(status=204)  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
