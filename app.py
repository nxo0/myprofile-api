from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False


@app.route('/')
def root():
    return render_template("index.html")


@app.route("/all")
def all():
    data = [
        {"name": "Ninomiya Kan"},
        {"name_ja": "二宮貫"},
        {"nickname": "にくそ"},
        {"characteristic": "あほ"},
        {"age": 15},
        {"birthday_year": 2005},
        {"birthday_month": 10},
        {"birthday_day": 11}
    ]
    return jsonify({
        'status': 'OK',
        'data': data
    })


@app.route("/name")
def name():
    return jsonify({
        'status': 'OK',
        'data': "Ninomiya Kan"
    })


@app.route("/name-ja")
def name_ja():
    return jsonify({
        'status': 'OK',
        'data': "二宮貫"
    })


@app.route("/nickname")
def nickname():
    return jsonify({
        'status': 'OK',
        'data': "にくそ"
    })


@app.route("/age")
def age():
    return jsonify({
        'status': 'OK',
        'data': "15"
    })


@app.route("/birthday-year")
def birthday_year():
    return jsonify({
        'status': 'OK',
        'data': "2005"
    })


@app.route("/birthday-month")
def birthday_month():
    return jsonify({
        'status': 'OK',
        'data': "10"
    })


@app.route("/birthday-day")
def birthday_day():
    return jsonify({
        'status': 'OK',
        'data': "11"
    })


if __name__ == '__main__':
    app.run()
