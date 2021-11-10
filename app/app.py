from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Demo Flask & Docker application is up and running! This is the initial version 5 with awesome changes"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
