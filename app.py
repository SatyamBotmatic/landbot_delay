from flask import Flask, request

import time

app = Flask(__name__)

@app.route("/webhook",methods=["POST"])
def webhook():
    #delay for 300 seconds
    time.sleep(300)
    message = request.json["message"]
    return message

if __name__ == '__main__':
    app.run(debug=True)