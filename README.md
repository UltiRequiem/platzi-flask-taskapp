# Taskapp made with Flask

<p>
<a href="https://github.com/UltiRequiem/Flask-Taskapp/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://github.com/UltiRequiem/Flask-Taskapp"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/UltiRequiem/Flask-Taskapp"><img alt="Code style: black" src="https://img.shields.io/tokei/lines/github.com/UltiRequiem/Flask-Taskapp?color=blue&label=Total%20Lines"></a>
</p>

![Cover](./assets/cover.png)

A taskapp that uses [Firebase](https://firebase.google.com).

## Development setup

1. Install Google Cloud SDK: Instructions
   [here](https://cloud.google.com/sdk/docs/install).

2. Create a project in google cloud: You can do this
   [here](https://console.cloud.google.com/projectcreate).

3. Clone the proyect

```bash
git clone https://github.com/UltiRequiem/Flask-Taskapp.git ; cd Flask-Taskapp
```

4. Create a virtual environment

```bash
python3 -m venv env;source env/bin/activate
```

5. Install the dependencies

```bash
pip install -r requirements.txt
```

6. Initialize Gcloud

```bash
gcloud init
```

7. Login Gcloud

```bash
gcloud auth login
```

8. Select the proyect

The project you created in step 2

9. Run

```bash
python3 main.py
```

## Demo

Here is a working live demo: https://flask-platzi.ultirequiem.repl.co/auth/login

At the moment it is running version
[v0.7-alpha](https://github.com/UltiRequiem/Flask-Taskapp/releases/tag/v0.7-alpha),
which did not implement a database yet. This is because I can't find a way to
deploy it anywhere else without a credit card.

**Current version: v1.0**

It runs in [Repl.it](https://repl.it).

## License

[MIT](./LICENSE)
