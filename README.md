# ml-intro
Code for introductory machine learning workshop


# Prerequisites
:heavy_check_mark: [Python 3.7](https://www.python.org/downloads/)

:heavy_check_mark: [Pipenv](https://docs.pipenv.org/en/latest/install/#installing-pipenv)

:heavy_check_mark: Favourite IDE ([PyCharm](https://www.jetbrains.com/pycharm/) is recommended)


# Dependencies setup
Navigate into project's main directory to run commands bellow:
## Installing dependencies
```
pipenv install
```
*NOTE: PyCharm should indentify `Pipfile.lock` and suggest you installing all packages with one click instead.*

## Activating virtual environment
```
pipenv shell
```
*NOTE: PyCharm should activate your virtual environment automagically, so you can use it via IDE's Terminal.*


# Dependencies check

To check whether installation went correctly, run following script within activated environent:

```
python check_dependencies.py
```
*NOTE: In PyCharm you can just right-click `check_dependencies.py` file and choose "Run 'check_dependencies'"*

If you see following output, you're all set up. Congratulations :tada: !
 
```
Sklearn is installed ✓
Matplotlib is installed ✓
Skimage is installed ✓
You're ready for ML hacking!
```
