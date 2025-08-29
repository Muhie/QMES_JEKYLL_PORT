# QMULES webpage
This is a codebase for the [qmules.tech](https://qmules.tech) webpage. We are using Flask with Apache webserver in order to implement it.

## Architecture
Let's first talk about the structure of project's root:

`webapp.wsgi` - wsgi connection of flask application to apache server\
`app/` - actual source code of the webpage\
`app/website.py` - contains views for the site, is an entry point, intialises flask application\
`app/models.py` - contains sqlalchemy models\
`app/tools.py` - contains useful admin tools for the server, see [admin scripts](#admin-scripts)

All the logic of the website is located in app module, with the entry point of `website.py`. `static/` folder houses static files like images, css, or javascript, while `template/` is used for storing jinja html templates.

Because databases are frequently updated by the website they shouldn't be stored in the repo, instead existing only on the server. Flask will generate `instance/` folder where all live information, including any databases will be written. 
Additionaly, it's best not to keep any sensitive information on the repo either, storing it on the server directly.

## Testing & Deployment
### Getting started with development
In order to set up your development environment run the following in the root of the project:
```bash
# set up virtual environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# set up flask project
./setup.sh
```

This should create python virtual environment, and initialise dummy flask database in `instance/` folder.\
In order to run flask application execute following while in the project's root:
```bash
flask run
```

### Admin scripts
There are multiple useful scripts defined in `app/tools.py` file. They are implemented using `flask.cli` functionality, so in in order to evoce them use:
```bash
flask [command-name]
```
There is no clear helpfile but you are welcomed to glance over function declarations and comments in `app/tools.py` file.
Some useful functions are:
```bash
flask setup-db
flask add-users
```

### Deployment
Sadly, there are no automatic deployment systems set up \*yet\*, so for now everything has to be done manually.

```bash
# log in to the production server
ssh root@qmules.tech
# navigate to `/var/www/webApp`
cd /var/www/webApp
# pull the latest version of the code
git pull
# restart apache
apache2ctl restart
```
