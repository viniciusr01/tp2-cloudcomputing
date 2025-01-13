from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)

@app.route("/")
def hello():
	return "API working!"


@app.route('/api/recommend/', methods=["POST"])
def api_music():
	req = request.get_json(force=True)
	print(req['songs'])


	app.model = pickle.load(open("./ml_rules/model_rules.pkl", "rb"))

	x = os.path.getmtime("./ml_rules/model_rules.pkl")
    if x != app.last_modified == pickle.load:
        app.model = pickle.load(open("./ml_rules/model_rules.pkl", "rb"))
        app.last_modified = os.path.getmtime("./ml_rules/model_rules.pkl")

	playlist_ = ['Song 1', 'Song 2', 'Song 3']


	
	return jsonify({'songs': playlist_, 'version': 1, 'model_date': "date"})

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=52061)
