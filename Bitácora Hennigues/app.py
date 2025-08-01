from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Renderiza templates/index.html
    return render_template("index.html")

if __name__ == "__main__":
    # python app.py  →  http://127.0.0.1:5000
    app.run(debug=True, port=5000)
