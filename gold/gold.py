from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('dashboard.html')

if __name__ == '__main__':
  app.debug = True
  app.run(host='localhost', port=8000)