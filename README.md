# Setup
To install the required packages use the command
```bash	
pip install -r requirements.txt
```
Then you can run the project using the command
```bash
python app.py
```

# Remarques
within the code itself to change the waiting time between every two requests you have to change the variable
```python
WAIT_TIME = 60
```

# Compiling
To compile the python script to a `.exe` file I used the `pyinstaller` module
```bash
pyinstaller -i icon/exe-icon.ico -F -w app.py
```
as a remarque there's no benifit to compiling it, I just wanted to experiment a bit ;)