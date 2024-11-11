# Step 1: Clone the repository (only once)
git clone https://github.com/team-repo/team-project.git
cd team-project

# Step 2: Create a new branch for your task
git checkout -b task-branch

# Step 3: Make your changes, add, and commit
git add modified_file.py
git commit -m "Implement new feature in modified_file.py"

# Step 4: Pull any new changes from main to stay updated
git checkout main
git pull origin main
git checkout task-branch
git merge main

# Step 5: Push your branch to the remote repository
git push origin task-branch

# Step 6: Create a pull request on GitHub to merge your task-branch into main.
# After approval and merge, delete the task-branch.
