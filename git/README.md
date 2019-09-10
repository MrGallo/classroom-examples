# git
[What is git?](https://guides.github.com/introduction/git-handbook/)

[GitHub workflow](https://guides.github.com/introduction/flow/)


## What you need to know
- [Create a repo on GitHub and clone the repo on your computer](#create-and-clone)
- [Pull changes from original repo](#pull-changes-from-original-repository)
- The `git` workflow.
  - [Sitting down and getting to work](#get-to-work)
  - [Stage changes and commit](#stage-and-commit)
  - [Push changes to GitHub](#push-changes)

## Create and Clone
- Go to [GitHub.com](github.com) and creace a repo.
  - Give it a name
  - Check `Create a `README` file`.
  - Add a `.gitignore` for `Python` (optional).
- Click the `Clone or download` button 
- Copy the URL.
  - The url should look like `https://github.com/<your-username>/repo-name.git`
- On your computer, in the `Terminal`, type:
    ```sh
    $ git clone <THE URL>
    ```
    If `ctrl + v` doesn't seem to work, use  `ctrl + shift + v` to paste in the terminal.

On classroom chromebooks:
- `cd` into the repo that was downloaded.
  - `$ cd repo-name`
- Set the git user name and email address for this single repo. **Do *not* use the `--global` flag.**
    ```sh
    $ git config user.name "YourGithubUserName"
    $ git config user.email "your@email.com"
    ```

## Workflow
## Pull changes from original repository
[GitHub Article](https://help.github.com/en/articles/merging-an-upstream-repository-into-your-fork)
```sh
$ git checkout master
$ git pull <original repo url> <branch>
For example:
$ git pull https://github.com/ICS4U-Gallo/markbook-assignment.git master
```
Then resolve any [conflicts](https://help.github.com/en/articles/addressing-merge-conflicts).
Then push:
```sh
$ git push
```

### Get to work
- Pull in changes from the cloud
  - `git pull`
- Now you can either create a new branch, or change your files in the `master` branch.

### Stage and Commit
- Save your files
- (optional) `$ git status` files with changes will be shown in red.
- Stage the changes
  - `$ git add -A`
  - If you `$ git status` again, the staged changes will be in green.
- Commit the changes
  - `$ git commit -m "Descriptive message"`
    - On our class computers, you may have an error message telling you to set the `user.name` and `user.email`. **Be sure to *omit* the `--global` flag on our class chromebooks**.
      ```sh
      $ git config user.name "YourGithubUserName"
      $ git config user.email "your@email.com"
      ```
 ### Push changes
- Push the changes
  - `$ git push`
  - Enter GitHub username/password
