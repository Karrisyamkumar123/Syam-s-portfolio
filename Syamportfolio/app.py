from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["subject"]
        email = request.form["email"]
        message = request.form["message"]

        print("Message received:")
        print("Name:", name)
        print("Subject:", subject)
        print("Email:", email)
        print("Message:", message)

        return render_template("index.html", success=True)

    return render_template("index.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)