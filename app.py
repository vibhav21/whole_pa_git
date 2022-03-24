from flask import Flask,render_template
import time 
app = Flask(__name__)



@app.route('/')
def route():
    return {"Status":200}
@app.route('/data')
def route2():
    return render_template("base.html")
@app.route('/time')
def time ():
    return (time.now())
if __name__ == "__main__":
    app.run()
