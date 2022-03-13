from flask import flash, Flask, jsonify, request, render_template, redirect, url_for
import csv

app = Flask(__name__)


def read_csv_file(filename):
    datos = []
    with open(filename) as fh:
        rd = csv.DictReader(fh, delimiter=",")
        for row in rd:
            datos.append(row)
    return datos


@app.route("/")
def main():
    datos = read_csv_file("datos.csv")

    return render_template(
        "index.html",
        datos=datos,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8800)
