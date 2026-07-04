.\.venv\Scripts\activate
Pyinstaller -F .\nbsfix.py -i ./icon/icon.ico  --clean --console -n NBS-Ansi-Fix
pause
python ./clean_build.py