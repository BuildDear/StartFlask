from flask import Flask
from urls import urls

app = Flask(__name__)

for url, view in urls:
    app.add_url_rule(url, view_func=view)

if __name__ == '__main__':
    app.run(debug=True)
