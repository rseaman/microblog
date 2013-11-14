CSRF_ENABLED = True
skfile = open('../flaskkey')
SECRET_KEY = skfile.read()
