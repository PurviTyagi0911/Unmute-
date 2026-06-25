from flask import Flask, render_template,request,session,redirect,url_for
import sqlite3

app = Flask(__name__)
app.secret_key='unmute_secret_key'
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
        description TEXT,
        image_url TEXT,
        
        club_name TEXT
    )
    """)

    conn.commit()
    conn.close()
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/clubs_login', methods=['GET', 'POST'])
def club_login():
   
        
    if request.method=='POST':
        club_name=request.form['club_name']
        session['club_name']=club_name
        return redirect(url_for('club_dashboard'))
    return render_template('clubs_login.html')
@app.route('/club_dashboard')
def club_dashboard():
    return render_template('club_dashboard.html')
@app.route("/student_feed")
def student_feed():
    conn = sqlite3.connect("unmute.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT title, category, location,date,time,description,image_url,club_name
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
            'description':row[5],
            'image_url': row[6],
            'club_name': row[7]
        })

    return render_template(
        "student_feed.html",
        events=events
    )
@app.route('/my_posts')
def my_posts():
    if 'club_name' not in session:
     return redirect(url_for('club_login'))
    conn=sqlite3.connect('unmute.db')
    cursor=conn.cursor()
    club_n=session['club_name']
    cursor.execute(
        """SELECT title, category, location,date,time,description,image_url,club_name FROM events WHERE club_name=?
    """,(club_n,)
    )
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
            'description':row[5],
            'image_url': row[6],
            'club_name': row[7]
        })
    return render_template('my_posts.html',events=events)

@app.route('/create_posts', methods=['GET', 'POST'])
def create_posts():
    if 'club_name' not in session:
        return redirect(url_for('club_login'))


    if request.method == 'POST':
      title = request.form['title']
      category = request.form['category']
      location = request.form['location']
      date = request.form['date']
      time = request.form['time']
      description = request.form.get('description')
      image_url=request.form.get('image_url')

      club_name=session['club_name']
      conn = sqlite3.connect("unmute.db")
      cursor = conn.cursor()

      cursor.execute("""
      INSERT INTO events(title, category, location,date,time,description,image_url,club_name)
      VALUES (?, ?, ?,?,?,?,?,?)
      """,(title, category, location,date,time,description,image_url,club_name)
                    )
      conn.commit()
      conn.close()

      return redirect(url_for('club_dashboard'))
    return render_template('create_posts.html')


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
