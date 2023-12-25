<h1 align="center">risk m8t</h1>
<p align="center">
    <em>Django framework, risk management portal</em>
</p>

---

## Table of Contents
1. [Getting Up and Running Locally](#getting-up-and-running-locally)
   1. [Running Test and Coverage Report](#running-test-and-coverage-report)
   2. [Existing Coverage Report in this REPO](#existing-coverage-report-in-this-repo)
2. [Getting Up and Running Locally With Docker](#getting-up-and-running-locally-with-docker)

---

## Getting Up and Running Locally

Prerequisites:

- Python 3.11

sqlite3 database will be used for simplicity of setting up and running locally.

1. Create a virtualenv:
```bash
$ python -m venv <virtual env path>
```

2. Activate the virtualenv you have just created:
```bash
$ source <virtual env path>/bin/activate
```

3. Install local requirements:
```bash
$ pip install -r requirements/local.txt
```

4. Install pre-commit (optional - for development):
```bash
$ pre-commit install
```

5. Apply migrations:
```bash
$ python manage.py migrate
```

6. Run django server:
```bash
$ python manage.py runserver
```

Now that the server's running, visit http://127.0.0.1:8000/ with your web browser. You'll be redirected to the swagger
api docs page.

![API Docs](https://mybucketla.s3.ap-southeast-1.amazonaws.com/Screenshot+2023-11-30+at+8.12.54%E2%80%AFAM.png)

### Running Test and Coverage Report

This project uses the [Pytest](https://docs.pytest.org/en/latest/example/simple.html) for testing. After you have set up
to run locally, run the following commands for testing result:

```bash
$ pytest
```

You can run the `pytest` with code `coverage` by following commands:
```bash
$ coverage run -m pytest
```

Once the tests are complete, run the following commands to see the code coverage:
```bash
$ coverage report
```

### Existing Coverage Report in this REPO
```
Name                                                                           Stmts   Miss  Cover
--------------------------------------------------------------------------------------------------
risk/__init__.py                                                                   0      0   100%
risk/admin.py                                                                      5      0   100%
risk/apps.py                                                                       4      0   100%
risk/forms/__init__.py                                                             1      0   100%
risk/forms/risk_form.py                                                           10      0   100%
risk/migrations/0001_initial.py                                                    7      0   100%
risk/migrations/0002_risk_created_datetime_risk_updated_datetime_and_more.py       5      0   100%
risk/migrations/__init__.py                                                        0      0   100%
risk/models/__init__.py                                                            4      0   100%
risk/models/project.py                                                             9      1    89%
risk/models/project_manager.py                                                     9      0   100%
risk/models/risk.py                                                               10      1    90%
risk/models/risk_scenario.py                                                      16      1    94%
risk/templatetags/template_tag.py                                                  5      1    80%
risk/tests/__init__.py                                                             0      0   100%
risk/tests/conftest.py                                                            28      0   100%
risk/tests/factories.py                                                           37      0   100%
risk/tests/test_forms.py                                                           5      0   100%
risk/tests/test_models.py                                                         13      0   100%
risk/tests/test_urls.py                                                           29      0   100%
risk/tests/test_views.py                                                          17      0   100%
risk/urls.py                                                                       4      0   100%
risk/views/__init__.py                                                             7      0   100%
risk/views/dashboard_htmx_view.py                                                 38      0   100%
risk/views/login_required_template_view.py                                         4      0   100%
risk/views/project_htmx_view.py                                                   13      4    69%
risk/views/risk_delete_view.py                                                    11      3    73%
risk/views/risk_htmx_view.py                                                      12      3    75%
risk/views/risk_scenario_htmx_view.py                                             28     13    54%
risk/views/risk_table_htmx_view.py                                                10      3    70%
website/__init__.py                                                                0      0   100%
website/settings/base.py                                                          26      0   100%
website/settings/test.py                                                           1      0   100%
website/urls.py                                                                    7      0   100%
--------------------------------------------------------------------------------------------------
TOTAL                                                                            375     30    92%
```

---

## Getting Up and Running Locally With Docker

Prerequisites:

- Docker
- Docker Compose

1. Configuring the Environment

You'll need to configure 2 env_file `.django` and `.postgres` in folder .envs/ . Reference can be made from sample folder .envs/.sample .
```
.envs
├── .sample
│   ├── .django
│   └── .postgres
├── .django
└── .postgres
```

2. Build and Run the Stack
```bash
$ docker-compose up -d --build
```

Now that the server's running, visit http://127.0.0.1:8000/ with your web browser. You'll be redirected to the swagger
api docs page.

![API Docs](https://mybucketla.s3.ap-southeast-1.amazonaws.com/Screenshot+2023-11-30+at+8.12.54%E2%80%AFAM.png)
