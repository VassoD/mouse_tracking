# Description: A program that tracks the mouse and plots the coordinates on a graph
import numpy as np
import matplotlib.pyplot as plt
import json
from flask import Flask, render_template, request
app = Flask(__name__)
import csv
import atexit

def clear_data():
    with open("data.csv", "w") as file:
        file.write("")

atexit.register(clear_data)

@app.route("/save_data", methods=["POST"])
def save_data():
    data = json.loads(request.form.get("data"))
    if data:
        with open("data.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["x", "y"])
            for item in data:
                writer.writerow([item["x"], item["y"]])
        return "Data saved."
    else:
        return "No data received."

@app.route("/graph_data")
def graph_data():
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return json.dumps(data)

@app.route("/update_data")
def update_data():
    x = request.args.get('x')
    y = request.args.get('y')

    with open("data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([x, y])

    return 'Data updated successfully'

@app.route("/graph")
def graph():
    data = np.genfromtxt("data.csv", delimiter=",")
    data = data.reshape(-1, 2)
    x = data[:,0]
    y = data[:,1]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='X', ylabel='Y', title='Line Plot of X and Y')
    ax.grid()
    
    filepath = "static/plot.png"
    plt.savefig(filepath)
    return render_template("graph.html", filepath=filepath)
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        if data in data:
            return "data received."
        else:
            return "No data received."
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)