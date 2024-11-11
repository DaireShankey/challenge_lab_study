# Step 1: Initialize a new Git repository
git init
# Initializes a Git repository in the current directory.

# Step 2: Set user name and email (only needed once per repository)
git config user.name "Your Name"
git config user.email "your.email@example.com"
# Configures your Git identity for this repository.

# Step 3: Add files to the staging area
git add .
# Adds all files in the current directory to the staging area.

# Step 4: Commit changes to the repository
git commit -m "Initial commit"
# Creates a commit with a message describing the changes.

# Optional Step: Connect to a remote repository (replace URL with your GitHub repo)
git remote add origin https://github.com/your-username/your-repo.git
# Adds a remote repository named 'origin'.

# Optional Step: Push the initial commit to the remote repository
git push -u origin main
# Pushes changes to the 'main' branch on the remote repository and sets up tracking.
