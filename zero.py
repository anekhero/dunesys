# zero.py
import os
from flask import Flask
from threading import Thread

# Flask web server to keep bot alive
def keep_alive():
    app = Flask('')

    @app.route('/')
    def home():
        return "I'm alive!"

    def run():
        app.run(host='0.0.0.0', port=8080)

    Thread(target=run).start()

# Run everything
keep_alive()
