from flask import Flask, render_template

app = Flask(__name__)  # '__main__'
app.secret_key = "my secret key"

@app.route('/')
def load_welcome():
    return render_template("home_page.html")





if __name__ == '__main__':
    app.run(port=4995, debug=True)