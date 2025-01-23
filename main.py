from flask import Flask, request
from decode import decode_pdf, remove_file

app = Flask(__name__)

@app.route('/')
def home():
	return {"message": "OK", "author": "SRM-TRG 2025", "endpoints": [{"get": "/", "post": "/decode-factus"}]}

@app.route('/decode-factus', methods=['POST'])
def decode_factus():
	body = request.get_json()
	return {"ok":True, "status":200, "file_path": decode_pdf(body['pdf_b64'], body['number_factus'])}

@app.route('/del-file/<path>', methods=['DELETE'])
def del_file(path):
	remove_file(path)
	return {"ok": True, "status": 200}


if __name__ == '__main__':
	app.run(debug=True)