from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/student_feed")

def student_feed():

    events = [
        {
            "title": "Drama Club Recruitment",
            "date": "25 June",
            "location": "Auditorium"
        },
        {
            "title": "Movie Screening",
            "date": "27 June",
            "location": "Seminar Hall"
        }
    ]

    return render_template("student_feed.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)