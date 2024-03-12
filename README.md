# Installation

Run the following commands to setup the project:

1. Install the virtual env by running the following command in the root folder:

```
python -m venv .venv
```

2. Activate the virtual environment

This step must be executed each time you try to run a laboratory project

```
.\.venv\Scripts\activate - in the root folder (Windows)
./.venv/Scripts/activate - in in the root folder (Linux or Mac)
``` 

3. Install the dependencies (make sure to have the venv activated)

Make sure to be in the root folder

```
pip install -r requirements.txt
```

4. Choose the desired env and run the main script

Example: 

```
cd L1
python main.py
```

## Contribuiting (or writing your own code)

Create a new folder for the current application, create a new file with the `.py` extension and run it using the `python <path_to_python_file>` command.