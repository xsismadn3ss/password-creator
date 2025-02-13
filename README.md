# PASSWORD CREATOR
Use this cli to create random password or create a custom one. The output is the password hash in ``SHA256`` algorithm.

## CONFIGURE ENVIRONMENT
It is recommended to have Python installed and to create a virtual environment to install the dependencies so that they are not installed globally.

**Create a virtual environment:**
```python
python -m venv .venv
```
**Activate environment:**
```CMD
.venv/Scripts/activate
```

**Install dependencies**
```CMD
pip install -r requirements.txt
```

## CREATE .EXE
**Install ``pyinstaller`` package:**
```
pip install pyinstaller
```

**Build CLI:**
```CMD
pyinstaller --onefile --console .\cli.py
```

The created executable will be placed inside a folder called `dist`. To run it in the console, you should do the following:
```CMD
.\dist\cli.exe
```