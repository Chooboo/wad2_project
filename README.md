# How to run the project:
Create a virtual environment first

Install the required packages: pip install -r requirements.txt

Download the repo: git clone https://github.com/Chooboo/wad2_project.git

Set up the database: python manage.py makemigrations musicquiz
                     python manage.py migrate
                     
Populate the database to get a working page: python populate_wad.py



# Git guide on how to collab:
source: https://medium.com/@jonathanmines/the-ultimate-github-collaboration-guide-df816e98fb67

## Before you start coding:

git pull - makes sure you have the up-to-date code on your computer


## During coding:

### Branching

First create your own branch so that when you accidentally mess up it won't propagate to the main branch and affect everyone:

#### Examples:

git checkout -b handle_registration

git checkout -b ...

This will create a new branch AND switch you to it.

Try typing git branch to see whether you are on your branch or on main.

### Commiting:

You should be now use the usual commands:

git add *

git commit -m "added a new feature"

Don't use git push unless you have everything working on your side please.


## After you finish coding and everything's working:

git push

Now go to https://github.com/Chooboo/wad2_project. 
You should see the branch you pushed up in a yellow bar at the top of the page with a button to “Compare & pull request”.
Click “Compare & pull request”. This will take you to the “Open a pull request” page. 
From here, you should write a brief description of what you actually changed. 
And you should click the “Reviewers” tab and select Chooboo (I can do the merging). When you’re done, click “Create pull request”.
