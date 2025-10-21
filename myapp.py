#import
from flask import Flask, render_template
from flask_mysqldb import MySQL

#main app
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskmysql'

mysql = MySQL(app)

#set route untuk /
@app.route("/")

def index():
    cur = mysql.connection.cursor ()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall ()
    cur.close()
    #render halaman layout beserta konten index
    return render_template("index.html", users=data)

@app.route("/login")
def index():
    cur = mysql.connection.cursor ()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall ()
    cur.close()
    #render halaman layout beserta konten index
    return render_template("index.html", users=data)

#debug, untuk update server dev otomatis
if __name__ == "__main__":
    app.run(debug=True)