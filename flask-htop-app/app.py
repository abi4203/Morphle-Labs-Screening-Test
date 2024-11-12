from flask import Flask
import subprocess
from datetime import datetime
import getpass

app = Flask(__name__)

# Root route
@app.route('/')
def index():
    return """
    <h1>Welcome to the System Stats App</h1>
    <p>Visit <a href="/htop">/htop</a> for system stats.</p>
    """

# htop route
@app.route('/htop')
def htop():
    # Your full name and system username
    full_name = "Your Full Name"
    username = getpass.getuser()

    # Server time in IST
    ist_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')

    # Run 'top' command to get the output in a batch mode (non-interactive)
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    # Format the output in HTML with <pre> for preserving whitespace
    response = f"""
    <h1>System Stats</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <p><strong>Top Output:</strong></p>
    <pre>{top_output}</pre>
    """
    return response

# Favicon route (to avoid 404 errors for /favicon.ico)
@app.route('/favicon.ico')
def favicon():
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
