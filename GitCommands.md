git status #check status


git add filename        # stage a specific file
git add .                # stage everything
git commit -m "message"  # commit with a message
git push                 # push to GitHub
git pull                 # pull latest from GitHub

git branch                    # list branches
git branch branch-name        # create a branch
git checkout branch-name      # switch to it
git checkout -b branch-name   # create + switch in one step

git log                  # see commit history
git log --oneline        # compact version
git diff                 # see unstaged changes

git remote -v             # see current remotes
git remote add origin URL # add a remote
git remote remove origin  # remove one