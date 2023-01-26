## Getting started
create a new local repository using **git init**

create and add a file to the repo using **git add** (add * adds all changes)

commit changes using **git commit**

## Work with branches
create a branch using **git branch**

switch to a branch using **git checkout**

check the status of files changed using **git status**

review recent commits using **git log**

revert changes using **git revert**

get a list of branches and active branch using **git branch**

merge changes in your active branch into another branch using **git merge**

## Synchronize repository

create a local copy (and keep in synch with central repo) using **git clone \<url\>**

add all files to staging area by using **git add**

commit the changes by using **git commit -m 'comment'**

move local changes to remote repository by using **git push** 

for example: 
```
git push -u origin bug-fix-typo
```
in order to push changes and a branch

get remote changes locally by using **git fetch** (not merged yet)

get remove changes locally and merge automatically with **git pull**

## Terminology

- origin == my fork
- upstream == remote 

project directory:
- working tree == location on your computer that contains the directories and files of a single commit
- staging area == index == changed files planned to be included in the next commit
- local repository == all commits of the project on the computer

- remote repository == all commits of the project in the cloud (single source of truth)
````
git remote --verbose
'''

## Help and config

configure your user name and email for comitting changes by **git config --global**
````
git config --global user.name "myname"
git config --global user.email "my@email.com"
git config --global core.editor nano
```

get help for a command by using **git help**

```
git help branch
```

