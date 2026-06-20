from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)
def init_db():
    conn = sqlite3.connect("unmute.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        location TEXT NOT NULL,
        date TEXT,
        time TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/clubs_login')
def club_login():
    return render_template('clubs_login.html')
@app.route("/student_feed")
def student_feed():
    conn = sqlite3.connect("unmute.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT title, category, location,date,time,description
    FROM events
    """)

    rows = cursor.fetchall()

    conn.close()

    events = []

    for row in rows:
        events.append({
            "title": row[0],
            "category": row[1],
            "location": row[2],
            'date':row[3],
            'time':row[4],
            'description':row[5]
        })

    return render_template(
        "student_feed.html",
        events=events
    )

@app.route('/create_posts', methods=['GET', 'POST'])
def create_posts():


    if request.method == 'POST':
      title = request.form['title']
      category = request.form['category']
      location = request.form['location']
      date = request.form['date']
      time = request.form['time']
      description = request.form['description']




      conn = sqlite3.connect("unmute.db")
      cursor = conn.cursor()

      cursor.execute("""
      INSERT INTO events(title, category, location,date,time,description)
      VALUES (?, ?, ?,?,?,?)
      """,(title, category, location,date,time,description)
                    )

      conn.commit()
      conn.close()
    return render_template('create_posts.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
