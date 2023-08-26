# Spectr_App

## Инструкции по запуску

Страница для аналитика - Simulator на верхней панели

## ✨ How to use the code

> **Step #1** - Clone the project

**Актуальная версия:** 
```bash
$ git clone -b feature-upload-files https://github.com/SpectrApp/Spectr_App.git
```

~~Из ветки main:~~
```bash
$ git clone  https://github.com/SpectrApp/Spectr_App.git
``` 

<br />

> **Step #2** - create virtual environment using python3 and activate it (keep it outside our project directory)

```bash
$ # Virtualenv modules installation (Unix based systems)
$ python3 -m venv venv
$ source venv/bin/activate
```

 For **Windows-based** systems

```bash
$ # Virtualenv modules installation (Windows based systems), from cmd
$ python -m venv venv
$ venv\Scripts\activate.bat
```

<br />

> **Step #3** - Install dependencies in virtualenv

```bash
$ pip install -r requirements.txt
```

<br />

> **Step #4** - Create and setup database

```bash
$ flask db upgrade
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

**ВАЖНО!**
Сайт испольует API сервиса [dadata](https://dadata.ru/api/clean/address/#response).
Для его работы нужно установить environment variables:
* DADATA_API_KEY - api-ключ (токен)
* DADATA_SECRET_KEY - секретный ключ
Это делается теми же командами:

на Linux:
```bash
$ export DADATA_API_KEY=ваш_токен
$ export DADATA_SECRET_KEY=ваш_секретный_ключ
```
на Windows аналогично, см. команды выше.

<br />

> **Step #6** - start server at `localhost:5000`

```bash
$ flask run
```

