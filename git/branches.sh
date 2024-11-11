# Step 1: Create a new branch named "feature-branch"
git branch feature-branch
# Creates a new branch but doesn’t switch to it.

# Step 2: Switch to the new branch
git checkout feature-branch
# Alternatively, you can use: git switch feature-branch (in newer Git versions).

# Step 3: Make changes and add them to the staging area
# (e.g., edit a file named example.txt)
git add example.txt

# Step 4: Commit changes in the feature branch
git commit -m "Add feature to example.txt"
# Commits changes to the feature branch.

# Step 5: Switch back to the main branch
git checkout main

# Step 6: Merge the feature branch into the main branch
git merge feature-branch
# Merges changes from feature-branch into main.

# Step 7: Delete the feature branch if it's no longer needed
git branch -d feature-branch
# Deletes the branch to keep the repository clean.
