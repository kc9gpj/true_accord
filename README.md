###Over

## Setup Environment (Mac)

##### [Homebrew](brew.sh)
  * `brew install pyenv pyenv-virtualenv postgresql memcached redis`

##### pyenv (see [Pipfile](Pipfile) for `[version]`)
  * `pyenv install 3.7.2`
  * `pyenv virtualenv 3.7.2 bowser`
  * `pip install pipenv`
  * `pipenv sync`

## Setup (Ubunutu, or non-virtualenv)
  * `Utilize pip3 and python3 if not defualt`
  * `Install requirements, pip (pip3 if not default) install -r requirements.txt`

## To Run
  * `In terminal, run python debt.py`

## Tests
  * `In terminal, run python -m unittest`
