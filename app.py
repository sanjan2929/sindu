from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/panic', methods=['POST'])
def panic_button():
    try:
        subprocess.run(['python', 'call.py'], check=True)
        subprocess.run(['python', 'sms.py'], check=True)
        subprocess.run(['python', 'location.py'], check=True)
        return jsonify({"message": "Panic Button Clicked: We will help you!"})
    except subprocess.CalledProcessError as e:
        error_message = f"An error occurred: {e}\n\nCheck location.log for details."
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
