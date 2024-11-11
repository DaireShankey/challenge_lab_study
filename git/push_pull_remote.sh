# Step 1: Push the current branch to the remote repository
git push origin main
# Pushes the main branch to the remote repository named 'origin'.

# Step 2: Pull updates from the remote repository
git pull origin main
# Fetches and integrates changes from the remote main branch to your local main branch.

# Step 3: If you encounter merge conflicts, Git will notify you.
# Open the conflicting files, resolve conflicts, then add and commit.

# Step 4: After resolving conflicts, commit the merge
git commit -m "Resolve merge conflicts"
