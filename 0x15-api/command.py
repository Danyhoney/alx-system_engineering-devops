# To Install AutoPep8
pip install autopep8 

# To install Pycodestyle
pip install pycodestyle
pip install --upgrade pycodestyle
pip uninstall pycodestyle

# To run Pycodestyle
pycodestyle --show-source --show-pep8

# To fix all Pycode errors
autopep8 --in-place --aggressive --aggressive --max-line-length 79 --ignore=E262,E265,E266 *.py 
