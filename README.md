# Spectr_App

## Инструкции по запуску

Страница для аналитика - Simulator на верхней панели

## ✨ How to use the code

> **Step #1** - Clone the project

```bash
$ git clone https://github.com/SpectrApp/Spectr_App.git
```

<br />

> **Step #2** - create virtual environment using python3 and activate it (keep it outside our project directory)

```bash
$ # Virtualenv modules installation (Unix based systems)
$ python3 -m venv venv
$ source venv/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> **Step #3** - Install dependencies in virtualenv

```bash
$ pip install -r requirements.txt
```

<br />

> **Step #4** - setup `flask` command for our app

```bash
$ export FLASK_APP=main.py
$ export FLASK_ENV=development
```

 For **Windows-based** systems

```powershell
$ (Windows CMD) set FLASK_APP=main.py
$ (Windows CMD) set FLASK_ENV=development
$
$ (Powershell) $env:FLASK_APP = ".\main.py"
$ (Powershell) $env:FLASK_ENV = "development"
```

<br />

> **Step #6** - start test APIs server at `localhost:5000`

```bash
$ flask run
```

