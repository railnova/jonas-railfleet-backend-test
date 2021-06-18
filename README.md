# railfleet-backend-test
Test project for Railfleet Python Backend Job 2021

## Setup

Cloen this repository on your computer.

In the project's directory create a new virtual environment and activate it.
```bash
virtualenv --python=python3.8 venv
source venv/bin/activate
```
No big list of requirements here, just install Django:
```
pip install Django
```

You can now run the django application locally with:
```bash
python manage.py runserver
```

You can get access to the admin of the application with the following credentials:
- user: admin
- password: admin

For exercice 3 you will also need to have deno installed.
We will let you figure that out (https://deno.land/)

## Exercices

Create a single pull request for this repository with the following additional features (feel free to comment on your choices or difficulties in the PR).

### 1) Auto user for defects

The defect model can be found here: `./defect/models.py`.
We would like than when creating a new defect, the user foreign key would be automatically set to the user creating it.

### 2) Create an REST API for the Defect model

We want people to be able to interact through HTTP with the defect ressources.
We want to provide an endpoint `/api/defects`, to which people can:
- get a list of all defects (bonus point for pagination if there are too much defects (let's say above 200))
- create a new defect
- update an existing defect
- delete an existing defect (only if they created)

### 3) Broadcast

For this one you will need to run the following small deno server:
```bash
deno run --allow-net counters_server.js
```

Whenever a defect is created or deleted, we want to send asynchronously a request to our counter server with the action that was performed.

If a defect is created we want to send the following payload to the counter server:
```json
{
    "user": 1,
    "action": "create"
}
```

If a defect is deleted we want to send the following payload to the counter server:
```json
{
    "user": 1,
    "action": "delete"
}
```

Of course it needs to be the defect's user id and not always `1`.

### 4) Optional question (don't feel bad if you prefer to skip it)

Let's say the only requirement is that the app is a Django app. You can make any other choice you want (change database technology, run extra streaming services, ...) would you solve the third exercice differently and in that case what would be your suggested setup ?