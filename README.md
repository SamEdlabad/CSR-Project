# CSR-Project
Computer Science Project


1. Create a virtual environment 
use command : python3 -m venv <virtualenvname>

2. Download django without using sudo as it might cause huge errors
use command : pip3 install django
              pip install django-crispy-forms
  
3. Connect your project with mysql
use command: pip3 install mysqlclient
Only if the above doesn't work, follwo below procedure
use commands: pip3 install pymysql
              pip3 install cryptography
Edit the __init__.py file of your root project folder
write:
...
import pymysql
pymysql.install_as_MySQLdb()
...

then run the file once to install MySQLdb to your site packages.

Import py3dns and validate_email:
pip install py3dns
pip install validate_email