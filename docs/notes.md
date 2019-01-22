#AirDnD the API
This file will serve as my own notes to myself, though I cannot vouch for the applicability to other developers.

This project is built in python using the Flask framework. But first, a virtual environment was setup so all the dependencies would be included in one environment.

  * to get the dependencies at any time, run the command `pip freeze > requirements.txt`
  * can run `pip install -r requirements.txt` inside of python interpreter to get the same virtual environment
  * `deactivate` can also get out of the virtualenv with a folder holding all the settings


In development, when you want to run a flask app you must run `export FLASK_APP=<your_py_file_here>` at least once. From there, you can execute `flask run` and it will create your server

### Atom Text Editor Integration

Why not complicate things by learning multiple processes at once?
I started using the Atom editor, which is really nice actually. It has built in git support (or maybe it is github specific, idk yet). It can give you a more GUI approach to version control and seems nice. It can even push to your repo when you click a button. However, it needs to be authenticated of course.

I've set up multi-factor or SSH for my GitHub account, so it wont accept just a username and password over https. Instead, i needed to create a user access token and provide that as a password. It saved, nothing else needed, done!

 > edit: that turned out to be a lie, Atom forgets the token every time that i close and re open it. For now, push/pulling via command line anyway
