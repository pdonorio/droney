
# droney

Project currently tested locally on `Python 3.7+`


## instructions


```bash

export PROJECT=droney

# setup libs
pip3 install --upgrade -r requirements.txt

# check type hints
mypy --ignore-missing-imports $PROJECT

# format code
black -S $PROJECT

# run tests
pytest -s -x tests

# use it from __main__.py
python -m $PROJECT

```


## modes


- [cli](https://github.com/fwkz/riposte#example-usage)
- [telegram chat](https://python-telegram-bot.org)
- slack?
- discord?
- messenger?
