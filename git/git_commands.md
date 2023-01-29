## Overview
![](clone-workflow.jpg)

## Getting started

### create a new local repo inside a project directory
```
git init
```
your project directory contains
- working tree: location on your computer that contains the directories and files **of a single commit**
- staging area: (index) changed files planned to be included in the next commit
- local repository: all commits of the project on the computer


### configure your user name and email for comitting changes
```
git config --global user.name "myname"
git config --global user.email "my@email.com"
```
### change the default editor
```
git config --global core.editor nano
```

## Do the basics
### create and add files to the local repo 
```
git add .
git add *
```
use "* " to add all changes or use "." to add all files in current directory

### check the status of files changed or untracked
```
git status
```

### commit changes to staging area 
```
git commit -m "commit message"
```

### review recent commits
```
git log --oneline --graph [--all]
```

## Work with branches
Create a branch using and switch to it
```
git checkout -b feature1 
```
Get a list of branches and the active branch. Use --all to include tracking branch labels (see below).
```
git branch [--all]
```
Checkout a branch to switch and work on it.
```
git checkout master
```

revert changes using **git revert**

## Merging branches
Merge changes in your *active* branch with another branch using git merge.

### fast forward merge
The master label can be set to the branch head label. The feature branch was a streight continuation of the base branch. No other commits were made to the base branch after the feature branch.
![](gitfastforward-merge.jpeg)
Here are the steps
```
git checkout master
git merge <featurebranch>
git branch -d <featurebranch>
```

### merge commit
The master branch and the feature branch contain both changes, i.e. commits, after branching. A fast forward merge is not possible. The merge combines the commits at the tip of the branches and places it into a new (merge) commit in the master branch. This commit has then two parents. The merge can lead to a **merge conflict**, if both branches contain conflicting changes on the same thing. The merge base, "ours" commit (from master) and "theirs" commit (the feature branch) are used for the merge.
![](gitmerge_commit.jpeg)
```
git checkout master
git merge <featurebranchlable>
git branch -d <featurebranchlabel>
```
You can force a merge commit with the **--no-ff** flag, even if a fast forward commit would be possible. This allows to see the branching in the commit history.
```
git checkout master
git merge --no-ff <featurebranchlabel>
git branch -d <featurebranchlabel>
```
![](gitmerge_commit_noff.jpeg)

### merge conflict
Checkout master. Execute merge command. Git detects a conflict and modifies the file(s), for a human to make the decision for what to keep/change. Git markes the hunks in the file with <<<< >>>>. It shows ours and theirs. Update the file and add and commit the file.
```
git checkout master
git merge <featurebranchlabel>
# handle conflict e.g. update feature.py
git add feature.py
git commit
git branch -d <featurebranchlabel>
```
![](gitmergeconflict.png)

## sqash merge (rewrite commit history)

## rebase (rewrite commit history)

## Tracking branch (label)

A tracking branch label is a label to a local branch that represents represents the remote branch (at the last network command, like clone). It's used to keep remote and local repositories in synch. 

E.g. cloning creates a local copy of the remote master branch and it's labels HEAD and master. An additional tracking branch label is created for the default branch e.g. **origin/master**. origin is an alias for the remote repository url. master is the default branch. origin can be used in git commands instead of the origin/master or repo_url/master.
![](gittrackingbranchlabel.jpeg)
The tracking branch label is only updated with network commands. I.e. local commits and commits in the remote repo are not automatically changing the trancking branch label. 
![](gittrackingbranchoutofsynch.jpeg)




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

- upstream == remote 

- remote repository == all commits of the project in the cloud (single source of truth)
```
git remote --verbose
```

- git id == object id == object name ... is a sha-1 hash, that identifies a object (commit).
- HEAD and main are **references** to a git commit object. Can be used instead the id. You can use the first 4+ characters of an id, instead the full id.
- **HEAD** is normally a reference to a branchlabel that points to the last commit of a branch - e.g. master, featureX ... 
- A **detached HEAD** references a specific commit directly (instead a branch label). So - checkout the branch with new branchlabel ... will make HEAD pointing to the label i.e. the last commit of that branch

You can show the last n commits by specifying, how many commits you are interested in-
```
git log --oneline -1
```
results in
```
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

## Help

### get help for a command

```
git help branch
git help commit
git help add
```
