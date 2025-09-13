from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Frozen Shop</title>
        </head>
        <body>
            <h1>Welcome to Frozen Shop</h1>
            <p>Here you will find Fortnite accounts for sale.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
