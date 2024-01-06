##DRF Installations and Configuration
#Setup
Creating the Project and Virtual Environment
Do not copy all of these at once and paste them into your terminal. Copy and run each one separately.

cd ~/workspace # go to your workspace
mkdir <project_name>-server # create a new directory
cd <project_name>-server # cd into that directory
code . # open VSCode
pipenv shell # initialize a new virtual environment
Next, install these third-party packages for use in your project.

pipenv install django=='4.1.3' autopep8=='2.0.0' pylint=='2.15.5' djangorestframework=='3.14.0' django-cors-headers=='3.13.0' pylint-django=='2.5.3'
Then you can create your very first Django project with the following command. Make sure you are in the ~/workspace/levelup-server directory by running pwd.

Don't forget the . at the end of the command below. Pro-tip: Use the copy button to grab all of the code.

django-admin startproject <project_name> .
After running this command, you will notice that you now have a directory called <project_name> in your project. It includes several .py files.

#Controlling Lint Errors
Add Pylint file
The pylint package is very good at ensuring that you follow the community standards for variable naming, but there are certain times that you want to use variable names that are short and don't use snake case. You can put those variable names in a .pylintrc file in your project.

Without this configuration, your editor will put orange squiggles under those variable names to alert you that you violated community standards. It becomes annoying, so you override the default rules.

echo '[FORMAT] \n  good-names=i,j,ex,pk\n\n[MESSAGES CONTROL]\n  disable=broad-except,imported-auth-user,missing-class-docstring,no-self-use,abstract-method\n\n[MASTER]\n  disable=C0114,\n' > .pylintrc
Select Python Interpreter
Open VS Code and press ⌘SHIFTP (Mac), or CtrlSHIFTP (Windows) to open the Command Palette, and select "Python: Select Interpreter".

Find the option that has:

<YOUR_FOLDER_NAME>-<RANDOM_STRING>

Pylint Settings for Django
There should now be a .vscode folder in your directory. If there is not one, create it. Create/open the settings.json file and add the following lines:

<project_name>-server/.vscode/settings.json

{
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
        "--django-settings-module=<folder name>.settings",
    ],
}
Notice that <folder name> should be the name of the folder that has the settings.py file, in this case it will be <project_name>.settings
Create API Application
Now that the project is set up and has some initial configuration, it's time to create an application for the <Project_Name> API project. Django projects are containers for one, or more, applications. Right now, we only need one application in this project.

Make sure you are in your <project_name> directory when you run this command.
python manage.py startapp <project_name>api
Add Content To .gitignore File
Create a .gitignore file and generate the content for it by running this command

curl -L -s 'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore' > .gitignore
Uncomment out the Pipfile.lock line to make sure this gets ignored (line 95 when this was written)

Add .vscode to the .gitignore file.

#Setting Up Package Directories
Run the following commands to remove some boilerplate files that you won't be using, and create directories that will contain the code for your application.

rm <project_name>/models.py <project_name>/views.py
mkdir <project_name>/models <project_name>/views
touch <project_name>/models/__init__.py <project_name>/views/__init__.py

#Update Settings
Below, there are four sections of your project's settings.py module. Replace your existing sections with the code below.

These settings changes will be needed for any REST API application that you make. The only thing that will differ between applications is the name of the application itself.

Below, you can see levelupapi in the list of installed apps. Whatever project you create in the future, your application names in that project will go there instead.

levelup-server/levelup/settings.py

# UPDATE THIS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    '<project_name>',
]

# THIS IS NEW
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://127.0.0.1:3000'
)

# UPDATE THIS
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#Create Base Django Tables
Django gives a built-in migration file that makes the tables in a SQLite database for you. Go ahead and run that migration to set up the initial tables.

python manage.py migrate


#Running the Django Server With VS Code Debugger

Inside the .vscode create a file called launch.json. Paste the following code in that file.

<project_name>/.vscode/launch.json

{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": ["runserver"],
            "django": true,
            "autoReload":{
                "enable": true
            }
        }
    ]
}
Run your server in the terminal (You can also use F5)
python manage.py runserver
