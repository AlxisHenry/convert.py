# Install dependencies
for dependence in $(cat dependencies.txt); do
	pip install -r $dependence
done

# Unit Tests
pytest tests/

# Build (.exe for Windows only)
python setup.py build