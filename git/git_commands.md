## Getting started
create a new local repository using **git init**

create and add a file to the repo using **git add** (add * adds all changes)

commit changes using **git commit**

## Work with branches
create a branch using **git branch**

switch to a branch using **git checkout**

check the status of files changed using **git status**

review recent commits using **git log**
```
git log --oneline --graph
```

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

- origin == alias for the remote repository (can be used in git commands instead of the url)
- upstream == remote 

project directory:
- working tree == location on your computer that contains the directories and files of a single commit
- staging area == index == changed files planned to be included in the next commit
- local repository == all commits of the project on the computer

- remote repository == all commits of the project in the cloud (single source of truth)
```
git remote --verbose
```

- git id == object id == object name ... is a sha-1 hash, that identifies a object
- HEAD and main are **references** to a git object. Can be used instead the id. You can use the first 4+ characters of an id, instead the full id.
- HEAD is normally a reference to a branchlabel, which points to the last commit - e.g. master, featureX ... A detached HEAD references a specific commit directly (instead a branch label). So - checkout the branch with new branchlabel ... will make HEAD pointing to the label i.e. the last commit of that branch
```
git log --oneline -1
```
results in 
23e343 (HEAD -> master) commit text
```

- branch == a unique path of commits ... The default branch is called **master**
- branch label == is also reference to the last commit in the path ("**tip of the branch**"), i.e. implements a reference. Deleting a branch label only deletes the label - not the commits/the branch.

- tags can be leightweight or **annotated** (recommended). Tags are a reference to a specific commit. They are not automatically pushed to the remote repo. Use:
```
git tag -a -m "Version 1.0" v1.0 HEAD
git push --tags
git push v1.0
```

## Help and config

configure your user name and email for comitting changes by **git config --global**
```
git config --global user.name "myname"
git config --global user.email "my@email.com"
git config --global core.editor nano
```

get help for a command by using **git help**

```
git help branch
```
