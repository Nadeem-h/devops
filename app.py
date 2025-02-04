from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
        # Get the secret from the environment variable (injected by Kubernetes)
            my_secret = os.environ.get("MY_SECRET")
                if my_secret:
                          return f"Hello, World! My secret is: {my_secret}"
                          else:
                                    return "Hello, World! (No secret found)"

                                if __name__ == "__main__":
                                        app.run(debug=True, host="0.0.0.0", port=8080)
