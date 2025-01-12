from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
	return "API working!"


@app.route('/api/recommend/', methods=["POST"])
def api_music():
	req = request.get_json(force=True)
	print(req['songs'])

	return jsonify({'songs':['oi', 'tudo?'], 'version': 1})

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=52061)
