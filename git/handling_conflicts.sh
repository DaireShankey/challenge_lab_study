# Step 1: Make sure you are on the main branch and pull latest changes
git checkout main
git pull origin main

# Step 2: Create a new branch and make changes
git checkout -b conflict-branch
# Edit a file (e.g., example.txt) and commit the changes
git add example.txt
git commit -m "Edit example.txt on conflict-branch"

# Step 3: Switch back to main branch, edit the same file, and commit
git checkout main
# Make different changes to example.txt and commit
git add example.txt
git commit -m "Edit example.txt on main"

# Step 4: Attempt to merge conflict-branch into main
git merge conflict-branch
# This will likely cause a conflict if the same lines were edited differently.

# Step 5: Open the conflicting file and resolve conflicts
# Conflicted lines are marked with <<<<<<<, =======, and >>>>>>>

# Step 6: After resolving conflicts, add and commit the resolved file
git add example.txt
git commit -m "Resolve merge conflicts in example.txt"
