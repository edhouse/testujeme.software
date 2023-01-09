$TIMESTAMP = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"

.\venv\Scripts\activate
pip install -r requirements.txt
py -m pytest .\tests.py > "result_$TIMESTAMP.txt"