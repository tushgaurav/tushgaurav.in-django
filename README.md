# Personal Website (Remake in Django)

Personal full-stack website made with Django, HTML, CSS and JavaScript(vanilla).
This website have the following features -

- Bloging support, can view and search blogs.
- Profile support, users can signup, login and view other user's profiles (still in development)
- Contact form
- About, Skills and Experience pages
- A hidden **easter egg** game (hint: open console)

Visit this website [here](https://beta.tushgaurav.in)

### Screenshots

This is the recent latest look of the website -
![Latest Animated Screenshot](https://i.ibb.co/qymrJxD/Animated-Screenshot.gif)

This is the older design of the website -
![Screenshot](https://i.ibb.co/WPbPPwd/image.png)

## Installation Guide

1. Make sure you have [Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads) installed on your system and then clone this repository to your system.

```bash
git clone https://github.com/tushgaurav/tushgaurav.in-django.git
cd tushgaurav.in-django
```

2. Install [pipenv](https://pipenv.pypa.io/en/latest/) on your system.
   Then start a virtual environment and install all the neccassary packages on your system.

```bash
pip install pipenv
```

```bash
pipenv shell
pipenv install
```

3. After installation of all the required packages, run the following command to launch a developement server to view the website locally -

```bash
python manage.py runserver
```

> Note: You may need to set up a local database and run the migrations in order for the website to function properly.

##### There can be bugs, still in development.
