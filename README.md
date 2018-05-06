## COMAND LINE TOOL AND WEB SERVICE FOR READING PALINDROMES FROM A FILE

### INSTALLATION

#### 1.- Create a virtualenv with Python 3.5:
```
$ virtualenv -p /usr/bin/python3.5 <some_name>
```

#### 2.- Install all required packages:
```
$ cd palimservice
$ pip install -r requirements.txt
```

### RUN TESTS
```
$ cd palimservice
$ python tests.py
```

### Execute the command line tool
```
$ cd palimservice
$ python palindrome.py /path/to/a/file/with/palindromes
```

### Execute the web service
```
$ cd palimservice
$ export FLASK_APP=web.py
$ export FLASK_INPUT_FILE_PATH=/path/to/a/file/with/palindromes
$ flask run
```
