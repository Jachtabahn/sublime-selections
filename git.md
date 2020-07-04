


# Edit commits in the git history

Do you want to edit a commit in the git history? Editing a commit means removing or adding changes to the files that are edited in this commit.

```sh
git rebase -i <parent-of-the-last-commit-you-want-to-edit>
```

This creates a new file
```sh
.git/rebase-merge/git-rebase-todo
```

If, while editing this file, you terminate the `git-rebase` process, you will end up in a undefined state.

This new file may look like this:
```sh
pick b9ca0bb Rename command
pick 1e17315 Return the select right command
pick 1875a25 Plan
pick c86a255 Plan
pick 7457c85 Plan
pick f7d8160 Make region span negative
```

For each commit that you want to edit, replace `pick` with `edit`.

Then save and close this file. In `nano` you can do this by pressing
1. `ctrl+o`
1. `enter`
1. `ctrl+x`

Now, in the working directory is checked out that commit, for which you replaced `pick` with `edit`. Now:
1. Edit the working directory.
1. Stage your changes.
1. Do
```sh
git commit --amend
```

Now a file with the old commit message of this commit will open. If you want, change the commit message of this commit. Save and close the file.

Run
```sh
git rebase --continue
```

Now, the following has happened:
* The changes that this commit intoduces have changed.
* The commit date of this commit has changed.
* The author date of this commit has stayed the same.

All of this is explained in [more detail](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) here.

## Split a commit into several commits

Do
```sh
git reset HEAD^
```

Then stage each change you want in a separate commit and commit that stage. Then run
```sh
git rebase --continue
```

# Change the editor used to commit messages and interactive rebase

Change to Sublime Text:
```sh
git config --global core.editor "subl --wait"
```

# Remove a file from every commit modifying this file

If you want to remove a file in every commit in the history of the current branch, do this:

```sh
git filter-branch --tree-filter 'rm -f passwords.txt' HEAD
```

The file will still be kept in other branches.

The `--tree-filter` option runs the specified command after each checkout of the project and then recommits the results. Thus new commits are created.

When you use `filter-branch` once, a backup directory is created. If you want to use `filter-branch` once more for another purpose, you have to delete that backup directory first:
```sh
rm -rf .git/refs/original
```

Or run `filter-branch` with the `-f` instead:
```sh
git filter-branch -f --tree-filter 'rm -f passwords.txt' HEAD
```

## Changing your email address in all the commits that are behind the commit the current branch points to

```sh
git filter-branch --commit-filter '
  if [ "$GIT_AUTHOR_EMAIL" = "dimitri.rusin@rwth-aachen.de" ];
  then
    GIT_AUTHOR_EMAIL="habimm@pm.me";
    GIT_COMMITTER_EMAIL="habimm@pm.me";
    git commit-tree "$@";
  else
    git commit-tree "$@";
  fi' HEAD
```
