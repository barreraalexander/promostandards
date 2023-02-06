👉 HOW TO AUTOMATICALLY BUILD THE APP
*all of these commands are to be run from the root directory, and without the `quotes`

1. open the env.sample file and fill in the credentials as needed.
2. run the command `docker-compose up --build`
3. the app will automatically run on port 5085, e.g. http://localhost:5085/api/media_content (needs to be a POST request)



<------------------------------------------------------>
👉 HOW TO MANUALLY BUILD THE APP
*all of these commands are to be run from the root directory, and without the `quotes`

1. copy the env.sample file and rename it .env. Fill in the necessary credentials.

2. create virtual enviroment with the command `python -m venv promo_venv` (note i had to create an alias from python3 to python)

3. update pip `python -m pip install --upgrade pip`

4. source the new virutal environment `source promo_venv/bin/activate` - should be indicated in your terminal path

5. install requirements with the command `pip install -r requirements.txt`

6. run the application with the command `python run.py`

7. ctrl+c to stop the app, and deactivate environment with `deactivate`

<------------------------------------------------------>


👉 HOW TO RUN UNIT TESTING
*all of these commands are to be run from the root directory, and without the `quotes`

1. `pytest -v -s` will run the unit test

<------------------------------------------------------>

👉 HOW TO USE AUTH
*all of these commands are to be run from the root directory, and without the `quotes`

1. create a new user on the route '/auth/register' by POSTing raw json in the format:
{
    "username" : "your_username",
    "password" : "your_password"
}

2. after creating a user, get your access code on the route '/auth/login' by POSTing a form with 2 field: username and password.
3. bearer token is to be returned. 


<------------------------------------------------------>

👉 HOW TO USE JSON AUTH

1. In the .env.sample file you will notice an environment variable called use_json_auth. 

2. Setting this to true will use json auth rather than jwt tokens.

3. To use the routes, you will need to make sure that id and password are in the users.json. 