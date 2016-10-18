# Install for development
At the moment, the instructions below assume a *Windows OS*, Python installed and set in 
your PATH environmental variable a command prompt (for PowerShell, 
change the activate script you run below to .\env\Scripts\Activate.ps1) open to the path 
where you cloned or unzipped this project, and a few .jpg images to play with. Run the 
following four commands:

<code>
python -m venv env

.\env\Scripts\activate.bat

pip install -r requirements.txt

pyinstaller rotate.py --onefile
</code>

The application **rotate.exe** should be located in a new folder called **dist**.