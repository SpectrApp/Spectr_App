# Spectr_App

## ✨ Инструкции по запуску

Чтобы запустить сайт, нужно выполнить следующие шаги:

### **Шаг #1** - Клонировать проект

Из гитхаба
```bash
$ git clone  https://github.com/SpectrApp/Spectr_App.git
``` 
Из гитлаба
```bash
$ git clone  https://gitlab.fintechhub.ru/dm1trykrylov/Spectr_App.git
``` 

<br />

### **Шаг #2** - Активировать виртуальное окружение для установки библиотек

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

### **Шаг #3** - Установить зависимости

```bash
$ pip install -r requirements.txt
```

<br />

### **Шаг #4** -  Создать и настроить локальную базу данных

```bash
$ flask db upgrade
```
Папка instance нужна для сохранения временных файлов
```bash
$ mkdir instance
```


<br />

### **Шаг #5** - Настройка команды `flask`

```bash
$ export FLASK_APP=main.py
$ export FLASK_ENV=development
```

 Для **Windows-based** систем

```powershell
$ (Windows CMD) set FLASK_APP=main.py
$ (Windows CMD) set FLASK_ENV=development
$
$ (Powershell) $env:FLASK_APP = ".\main.py"
$ (Powershell) $env:FLASK_ENV = "development"
```

### **Шаг #6** - Запуск сервера по адресу `localhost:5000`

```bash
$ flask run
```

