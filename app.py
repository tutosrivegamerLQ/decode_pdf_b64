from flask import Flask, request, send_from_directory
from decode import decode_pdf, remove_file
import os

if not os.access('./files', 0):
	os.mkdir('./files')
	
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['JSON_AS_ASCII'] = False

UPF = "files"
app.config['UPLOAD_FOLDER']=UPF

@app.route('/')
def home():
	return {"message": "OK", "author": "SRM-TRG 2025", "endpoints": [{"get": "/", "post": "/decode-factus"}]}

@app.route('/decode-factus', methods=['POST'])
def decode_factus():
	print(request.headers)
	print(request.content_type)
	body = request.get_json()
	print(body)
	if data is None:
		return {"ok":False, "status": 400}, 400
	else:
		return {"ok":True, "status":200, "file_path": decode_pdf(body['pdf_b64'], body['number_factus'])}

@app.route('/del-file/<path>', methods=['DELETE'])
def del_file(path):
	remove_file(path)
	return {"ok": True, "status": 200}

@app.route('/download/<fact_name>', methods=['GET'])
def download(fact_name):
	try:
		return send_from_directory(app.config['UPLOAD_FOLDER'], fact_name, as_attachment=True)
	except Exception as e:
		return {"message": "ERROR", "error":"Archivo no encontrado"}, 404



if __name__ == '__main__':
	app.run(debug=True)
