#!/usr/bin/python2.7
##!flask/bin/python
from app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000, debug=True)

#note that the local virtual environment cannot install pandas for some yet to be established reason
#therefore the central python environment is used
