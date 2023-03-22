import urllib.request
import os

python_version = "3.10.0"

url = f"https://www.python.org/ftp/python/{python_version}/python-{python_version}-amd64.exe"
filename = f"python-{python_version}-amd64.exe"

urllib.request.urlretrieve(url, filename)

os.system(filename)
