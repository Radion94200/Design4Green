# Backend API

## Install
```bash
virtualenv venv -p $(which python3)
pip install -r requirements.txt
scp debian@vps-2ea52359.vps.ovh.net:~/db.sqlite3 .
```
The DB should be in Design4Green/backend folder
## Launch the app

Source the requirements in the backend folder.  
Once done, you cqn execute:  
```
python3 manage.py runserver
```

Follow the link to access the bdd.
