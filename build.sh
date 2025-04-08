
brew install python-setuptools
rm -rf dist/
rm -rf build/
rm -rf *.egg-info
pip install -r requirements.txt

pip install build
python -m build
