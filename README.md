# Git&Github

Git is a DevOps tool used for source code management. It is a free and open-source version control system used to handle small to very large projects efficiently. Git is used to tracking changes in the source code, enabling multiple developers to work together on non-linear development.

# Basic Command Line Skills:

2.1	Familiarity with the command line interface.
2.2	Basic navigation and file manipulation using the terminal or command prompt.
2.3	examples:
cd ,ls ,touch ,mkdir ,rm ,rmdir ,touch.

<img width="1090" height="463" alt="image" src="https://github.com/user-attachments/assets/7190bde4-e3db-44f9-b30e-441805a0f83a" />

# Important Topics in Git:

# 1.	Repository:

1.1	Understanding what a Git repository is.
1.2	Initialization of a new repository.

# 2.Committing Changes:

2.1	Git add, commit, and commit messages.
2.2	Committing changes to the local repository.

<img width="1090" height="883" alt="image" src="https://github.com/user-attachments/assets/7da1219d-f271-4280-9932-fbb40fad7ac9" />

# 3.Branching and Merging:

3.1	Basics of branching and merging in Git.
3.2	Creating branches for new features or bug fixes.
3.3	Merging changes back into the main branch.

<img width="1090" height="992" alt="image" src="https://github.com/user-attachments/assets/fa4a6cad-a421-4665-8c4f-4d18c9627d5f" />
<img width="1090" height="992" alt="image" src="https://github.com/user-attachments/assets/337c5fd6-9c6f-4dd4-bb06-d02a3e49e168" />

# 4.Remote Repositories:

Remote repositories are online versions of our local repositories.
They allow developers to share and collaborate on projects easily.
We can connect to a remote repo using git remote add origin <URL>.
We use git push to upload and git pull to download changes.
It helps keep our code safe and synced between team members.

<img width="1090" height="527" alt="image" src="https://github.com/user-attachments/assets/31702841-d2f6-4676-b39f-6dce1e50bf7c" />
<img width="1090" height="358" alt="image" src="https://github.com/user-attachments/assets/49c82c38-6727-408d-bafe-d271e91fccf3" />

# Collaborative Work:
5.1	Working with others on the same project.
5.2	Handling merge conflicts.
Collaborative work in Git allows many people to work together on the same project.
Each member creates their own branch, makes changes, and then merges it into the main branch.
It prevents conflicts and helps in teamwork and version control.
Commands like clone, branch, push, and pull are commonly used.
This makes Git a powerful tool for team collaboration.

<img width="1090" height="512" alt="image" src="https://github.com/user-attachments/assets/b725d2b0-cfc2-4f1d-84fd-7c87f6934511" />

# 6.Git Ignore:

A .gitignore file tells Git which files and folders to skip while tracking changes.
It is used to ignore unnecessary, temporary, or sensitive files in a project.
For example, we can ignore .env, .log, or __pycache__/ files.
We just list those names in a .gitignore file in the project folder.
This keeps the repository clean and safe from unwanted files.
6.1	Ignoring files and directories using. gitignore.

<img width="1090" height="644" alt="image" src="https://github.com/user-attachments/assets/fcfe959c-2f0a-4e5d-8060-cb740a7832af" />

# 7.Tagging:

Tagging in Git is used to mark important points in the project’s history, like version releases.
It helps us easily identify and return to specific commits.
We create a tag using git tag -a v1.0 -m "message".
Tags are helpful for version control and software releases.
In short, tags act as labels for special commits in a project.

<img width="1090" height="437" alt="image" src="https://github.com/user-attachments/assets/dda833f5-47a9-4812-88e5-ef096d014fae" />

# Daily_activity_3
# Undoing changes:
# Reset
git reset --soft moves to an earlier commit but keeps all your changes staged for the next commit.
git reset --mixed also moves back but keeps your file changes only in the working area, not staged.
git reset --hard removes every change and completely resets your files to match the older commit
# Revert
git revert is used to undo a specific commit without changing the project’s history.
It creates a new commit that reverses the changes made by the selected older commit.
This is a safe way to fix mistakes because it doesn’t delete or rewrite any past commits.

<img width="921" height="719" alt="Screenshot 2025-10-09 152718" src="https://github.com/user-attachments/assets/b3e36a04-f241-424b-8dc9-8a2ba2470766" />
<img width="908" height="343" alt="Screenshot 2025-10-09 152627" src="https://github.com/user-attachments/assets/8b0ab4c2-eec7-4c05-a6b2-ac6c64bde9ec" />

# Git hooks
Git hooks are small scripts that run automatically when we do actions like commit or push.
I went inside the `.git/hooks` folder and created a file called `pre-commit`.
In that file, I wrote a message to show before every commit and made it active using `chmod +x pre-commit`.
When I committed changes, my message appeared automatically in Git Bash.
Git hooks are useful to check code quality, show messages, or stop wrong commits before they are made.

<img width="957" height="665" alt="Screenshot 2025-10-09 155022" src="https://github.com/user-attachments/assets/ff191890-42d5-449a-ad6b-013e3aceecf9" />

# Git Submodules
A Git submodule is a repository inside another repository.
It lets you include and manage another project (for example, a shared library or tool) within your main project without copying the files manually.
You can track a specific version of the submodule and update it whenever needed.
To reuse code from another Git repository.
To keep related projects organized and in sync.
To avoid duplicating code across multiple repositories.

<img width="1514" height="744" alt="Screenshot 2025-10-09 162732" src="https://github.com/user-attachments/assets/234f27d9-0979-4a91-ab02-72d6eeedd391" />

# Git interactive rebase
Git interactive rebase is a way to edit, combine, or reorder commits in your branch.
It lets you clean up your commit history before pushing it to the main repository.
You can change commit messages, remove commits, or squash multiple commits into one.
It’s like rearranging or fixing your commit history to make it neat and easy to understand.
To combine small commits into a single meaningful commit.
To edit or fix commit messages before sharing code.
To remove unwanted commits or mistakes from history.

<img width="890" height="789" alt="Screenshot 2025-10-09 163941" src="https://github.com/user-attachments/assets/a9ef4a00-a2c3-43bf-bbd1-f8809b045caa" />
<img width="866" height="700" alt="Screenshot 2025-10-09 164812" src="https://github.com/user-attachments/assets/6fa554b3-a337-4afa-b5d4-f291278f3812" />
<img width="614" height="746" alt="Screenshot 2025-10-09 164843" src="https://github.com/user-attachments/assets/fef9d18a-14f8-43b6-92bf-b4ee40db1a08" />

# Git Stashing
Git stash temporarily saves your uncommitted changes so you can work on something else.
Git stash will save your work for later without committing it.
To switch branches without committing unfinished work.
To quickly save changes and work on something urgent.
To keep your working directory clean temporarily.

<img width="1168" height="939" alt="Screenshot 2025-10-09 171825" src="https://github.com/user-attachments/assets/c6515555-4b6e-4c4a-8923-a1f2bcee1dd4" />
<img width="937" height="606" alt="Screenshot 2025-10-09 171836" src="https://github.com/user-attachments/assets/60d86cec-6526-4890-a3ea-d8b7391acf04" />

# Git GUI
Git GUIs are graphical interfaces for Git that let you manage repositories without typing commands in Git Bash.
They provide buttons, menus, and visual history for commits, branches, merges, and more.
This is useful for beginners or anyone who prefers visual tools over the command line.
View commit history visually.
Stage, commit, and push changes easily.
Merge and rebase with visual conflict resolution.
Manage multiple branches and repositories.

## why we use Git GUIs:

To make Git easier for people who don’t like command lines.
To clearly see the commit history and branches.
To resolve merge conflicts visually.
To manage repositories with drag-and-drop or click options.

# Git reflog:

Git Reflog keeps track of all actions made in a repository.
It helps to recover lost commits or branches after reset or rebase.
We can view them using git reflog and restore any version with git reset.
This makes Reflog useful for fixing serious mistakes in Git.
In short, Reflog acts as a safety net for your project history.

<img width="1409" height="969" alt="Screenshot 2025-10-10 172837" src="https://github.com/user-attachments/assets/466cd48d-311c-41ad-b255-467e062d3fe3" />

# Git Bisect:

Git Bisect is used to find which commit caused a bug in the project.
It works by marking one commit as good and another as bad, then tests the commits in between.
Git automatically narrows down to the faulty commit using binary search.
We use commands like git bisect start, git bisect bad, and git bisect good.
This makes it easy to locate and fix bugs in large codebases.

<img width="1421" height="952" alt="Screenshot 2025-10-10 174553" src="https://github.com/user-attachments/assets/b0d86a08-a15f-4538-9d3c-6dabf8269817" />

# Git cherry-pick:

it cherry-pick applies a specific commit from another branch to the current branch.
Use git cherry-pick <commit-hash> to select the commit.
If conflicts happen, resolve them, stage the files, and continue with --continue.
It’s useful for moving bug fixes or features without merging the whole branch.
In short, cherry-pick helps keep branches clean while applying only important changes.

<img width="1186" height="975" alt="image" src="https://github.com/user-attachments/assets/0d37013d-0921-4b33-b714-08222fefa20b" />
