
## Python

```python
print('Hello World')
```

## Powershell

```powershell
& "C:\Users\zatloukal\Desktop\hello-world.ps1"
```

## TestResults

```python
# Get test results
# Parse you test results here
version_number = '1.0.1.4'
passed = 4
failed = 1
skipped = 1

# Save to results to Markdown file
from datetime import datetime
test_results = r'[PATH]\TestResults.md'
with open(test_results, 'a+') as file:
	timestamp = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
	file.write(f'\n|{version_number}|{timestamp}|{passed}|{failed}|{skipped}|')
	file.close()

# Create a task
import os
today_journal_folder = r'[PATH]\Daily'

today_journal_file = f'{datetime.today().strftime("%Y-%m-%d")}.md'

with open(os.path.join(today_journal_folder, today_journal_file), 'a+', encoding='utf8') as file:
	timestamp = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
	file.write(f'\n- [ ] Check test results for version {version_number} 📅 {datetime.today().strftime("%Y-%m-%d")} 🔼 ')
	file.close()

```