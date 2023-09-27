from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Paris, France',
        'salary': ' 100K €'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Paris, France',
        'salary': ' 1000000 €'
    },
    {
        'id': 3,
        'title': 'Back-end Engineer',
        'location': ' Remote',
    },
    {
        'id': 4,
        'title': 'Front-end Engineer',
        'location': 'Remote',
        'salary': ' 100K £'
    }
]


@app.route("/") ##path after the domain name
def hello_world():
    return render_template('home_bootstrap.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)