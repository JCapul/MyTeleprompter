venv:
	python3.6 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install -r requirements.txt

run:
	FLASK_APP=app.py .venv/bin/flask run
