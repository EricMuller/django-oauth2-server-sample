# django-oauth2-server-sample
Django autorization oauth2 server


# Environment python3

virtualenv env  (centos7)

or virtualenv env --python=python3 (w10 bash ubuntu)

source ./env/bin/activate

# Django server

pip install -r requirements.txt

python manage.py migrate  ( if new base)

python manage migrate.py runserver 

default run on localhost:8000

# oauth-2 documentation


https://aaronparecki.com/oauth-2-simplified/


# Test Other Grant Types


1. create your oauth2 client  application http://localhost:8000/o/applications/
with Authorization grant type = resource owner password-based

connect with existing user oauth2 passwd=oauth2oauth2

2. get access_token

$curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=password&username=oauth2&password=oauth2oauth2&client_id=ckJc22BTTAk2eHWJfWebVs7OZmJh9NaoCZwsCDjW&client_secret=4kxUVc7LT4AOxaaDewgVzxrgV8SUkSHUp7rlAglzp2XngihepI8CxjQ4iDU0NfcxYDIP1fdE2b5skIaM1yRVRKy8g9FN7ryxd07i0xeYPJX8acNk4qf0muHDzZlFF5n5" http://127.0.0.1:8000/o/token/

{"token_type": "Bearer", "access_token": "OKPJIGWV1tKFSt88ahkdEzlwTvc5Jp", "expires_in": 432000, "refresh_token": 
"NLZwmYHm7EoHSxYT4vEMujKiiF86Hn", "scope": "write groups read"}

3. request api

$curl -X GET -H  "Authorization: Bearer OKPJIGWV1tKFSt88ahkdEzlwTvc5Jp" http://127.0.0.1:8000/api/v1/user/me/

{"username":"oauth2","id":3,"first_name":"","last_name":"","email":"","is_staff":false,"is_active":true,"date_joined":"2017-08-29T12:18:12Z"}


# test web applcation

1. create your oauth2 client  application http://localhost:8000/o/applications/

with Authorization grant type = Authorization code


2. In browser in private mode (ctrl n)
http://127.0.0.1:8000/o/authorize?response_type=code&client_id=zSOghQth8R1W4DksKvb4gTSGhRaguGnVo12ht1jQ&redirect_uri=http://127.0.0.1:8000/&scope=profile&state=1234zyx

connect with suer oauth2 pass oauth2oauth2

select authorize  button

3. you will redirect to http://127.0.0.1:8000/?code=authorization_code&state=1234zyx


http://127.0.0.1:8000/?code=7kVNt63jbjwidX36AMVxTDIjL0tKjL&state=1234zyx

4. get access_token

$curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=authorization_code&code=7kVNt63jbjwidX36AMVxTDIjL0tKjL&client_id=zSOghQth8R1W4DksKvb4gTSGhRaguGnVo12ht1jQ&client_secret=ib1uu9JE0rltEtng0jGqmV25NvKNd2zGRIbFKXfA6LitwZxt7AU03AaYOGzzdhu4qWiJ54i3OYRAhlJYTfWyy1zB4XrQ4kWcI6aBix2Fmsy9fXPkh0WvV1U6Yrc7y0El&redirect_uri=http://127.0.0.1:8000/" http://127.0.0.1:8000/o/token/

{"token_type": "Bearer", "refresh_token": "ujttOOdSlaQdsvtbQFaCUbcq0vDjBA", "scope": "read", "access_token": "PEfTEm78e9aIHvn2YuhTI87805eoXw", "expires_in": 432000}


5. request api

$curl -X GET -H  "Authorization: Bearer PEfTEm78e9aIHvn2YuhTI87805eoXw" http://127.0.0.1:8000/api/v1/user/me/












