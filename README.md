# Totally worthwhile coffee bot

## Install dependencies
```python
python -m venv myenv  # Create a new virtual environment (if needed)
source myenv/bin/activate  # Activate the virtual environment on Unix-based systems
pip install -r requirements.txt  # Install dependencies from the requirements file
```

## Usage:
```python
python coffeebot.py name email_prefix email_domain password duration [--bitwarden]
```
Add the `--bitwarden` flag to store the accounts details in a csv ready to import to Bitwarden vault.
- `duration` : number of days in the future you would like accounts for (starting from tomorrow)
