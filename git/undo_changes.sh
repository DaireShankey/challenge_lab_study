]# Undo changes in the working directory (before staging)
git checkout -- filename
# Discards changes in 'filename' and restores the last committed version.

# Unstage a file (remove from the staging area)
git reset filename
# Removes 'filename' from the staging area but keeps changes in the working directory.

# Undo the last commit (before pushing to remote)
git reset --soft HEAD~1
# Moves the last commit back to the staging area.

# Revert a specific commit by creating a new commit
git revert <commit-hash>
# Creates a new commit that undoes the specified commit (useful for shared repos).

# Reset repository to a specific commit (destructive - be careful)
git reset --hard <commit-hash>
# Resets the working directory and staging area to the specified commit.

