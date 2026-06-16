from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/events')
def events():
    return render_template('events.html')
@app.route('/clubs')
def clubs():
    return render_template('clubs.html')
app.run(debug=True)