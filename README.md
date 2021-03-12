# wad2_project

You can see what packages you need to install into your virtualenv in requirements.txt file.

Guide on how to set up the project:
Create a virtual environment first
Download the repo: git clone https://github.com/Chooboo/wad2_project.git
Now you have git initialized in the folder you downloaded so you can just navigate into it and use all the git commands as usual.


Git guide on how to collab:
source: https://medium.com/@jonathanmines/the-ultimate-github-collaboration-guide-df816e98fb67

git pull - ALWAYS before you start working

When you start working - create a branch and name it after the feature you're working on.
For example:

git checkout -b handle_registration

git checkout -b add_quiz

git checkout -b ...

This will create a new branch AND switch you to it.

Try typing git branch to see whether you are on your branch or on main.

You should be now use the usual commands:

git add *

git commit -m "added a new feature"

Don't use git push unless you have everything working on your side please.

After you're done implementing the feature, use the command:

git push

Now go to https://github.com/Chooboo/wad2_project. 
You should see the branch you pushed up in a yellow bar at the top of the page with a button to “Compare & pull request”.
Click “Compare & pull request”. This will take you to the “Open a pull request” page. 
From here, you should write a brief description of what you actually changed. 
And you should click the “Reviewers” tab and select Chooboo (I can do the merging). When you’re done, click “Create pull request”.
