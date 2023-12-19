# CORE

### Getting Started

Checkout to **core** directory

```bash
cd ./core
```

Activate virtual environment

```bash
python -m  venv venv
# and then
source ./venv/bin/activate
```

After that instal all the packages from requirements.txt

```bash
pip install -r requirements.txt
```

### Tests

Before commit any changes make sure you did not brake existing functionality.
For this you can run test with following command in terminal

```bash
make test
```
or
```bash
pytest -v
```

### Linter

It is important to follow code style rules, nobody likes ugly formatted code.  
You can automatically lint the code by running next commands:

```bash
make lint
```
or 
```bash
python -m isort **/*.py
python -m black **/*.py
```

### How to open Pull Request?

Before creating pull request make sure all test are passed and code is formatted properly.
For this view sections below. In any case, github actions will not allow you to merge pull request before you did all this actions.

More instruction on huw to open pull request you can find here: https://www.youtube.com/watch?v=jRLGobWwA3Y