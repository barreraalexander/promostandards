👉 HOW TO MANUALLY BUILD THE APP
*all of these commands are to be run from the root directory, and without the `quotes`

1. copy the env.sample file and rename it .env. Fill in the necessary credentials.

2. create virtual enviroment with the command `python -m venv promo_venv` (note i had to create an alias from python3 to python)

[NOTE: need to update pip: `python -m pip install --upgrade pip`]

3. source the new virutal environment `source promo_venv/bin/activate` - should be indicated in your terminal path

4. install requirements with the command `pip install -r requirements.txt`

5. run the application with the command `python run.py`

6. deactivate a virtaul environment `deactivate`

<------------------------------------------------------>


👉 HOW TO RUN UNIT TESTING
*all of these commands are to be run from the root directory, and without the `quotes`

1. `pytest -v -s` will run the unit test
2. `command-still-not-available` will run the unit test and log the results into a file 

<------------------------------------------------------>


👉
