## Overview
    `This program is a command-line based debt calculation tool, and test suite. Debt.py contains the core logic,
     and it has been broken down into small re-usable methods to allow easier extendeability. Check out the steps
     below to install and run. With more time I would have liked to include a more intensive test suite with VCR
     recording, and I could have broken down core logic to be even more extendable and re-usable.`

## Setup Environment (Mac)

##### [Homebrew](brew.sh)
  * `brew install pyenv pyenv-virtualenv postgresql memcached redis`

##### pyenv (see [Pipfile](Pipfile) for `[version]`)
  * `Extract zip, navigate to folder in terminal`
  * `pyenv install 3.7.2`
  * `pyenv virtualenv 3.7.2 bowser`
  * `pip install pipenv`
  * `pipenv sync`

## Setup (Ubunutu, or non-virtualenv)
  * `Extract zip, navigate to folder in terminal`
  * `Utilize pip3 and python3 if not defualt`
  * `Install requirements, pip (pip3 if not default) install -r requirements.txt`

## To Run
  * `In terminal, run python debt.py`

## Tests
  * `In terminal, run python -m unittest`
