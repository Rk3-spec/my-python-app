from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>আসসালামু আলাইকুম শামীম ভাই!</h1><p>আপনার প্রথম পাইথন অ্যাপ এখন লাইভ।</p>'

if __name__ == "__main__":
    app.run()
