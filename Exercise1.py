"""

Exercise 1 

1. Initialize git and dvc.
2. Track the data/ folder with DVC.
3. Commit the tracking the pointer file to git.
4. Add the local directory S3 as your default dvc remote 
5. Push data to that remote.

"""

"""
Commands 

1. Initiliaze Git and DVC in project
git init
dvc init - creates .dvc folder and .dvc ignore.


2. Track the data/ folder with DVC.
dvc add data

3. Stage and commmit the tiny pointer file and .gitignore to Git.
git add dataset.dvc .gitignore
git commit -m "Add dataset tracking pointer"

4. Add the local folder as remote storage
dvc remote add -d local C:\Users\venne\Videos\DVC-Practice\S3

5. Save the new remote configuration in git
git add .dvc/config
git commit -m "Configuring local DVC remote storage

6. Push the file into local remote
dvc push

"""