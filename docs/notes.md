#AirDnD the API
This file will serve as my own notes to myself, though I cannot vouch for the applicability to other developers.

This project is built in python using the Flask framework. But first, a virtual environment was setup so all the dependencies would be included in one environment.

  * to get the dependencies at any time, run the command `pip freeze > requirements.txt`

In development, when you want to run a flask app you must run `export FLASK_APP=<your_py_file_here>` at least once. From there, you can execute `flask run` and it will create your server
