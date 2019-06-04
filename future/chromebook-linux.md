**stats**
950 MB storage taken up

- In settings, search `linux`.
- Under `Linux (Beta)`, click `turn on`, wait for download.

**stats**
2.5 GB taken up

## Install from .deb file
- Download VS Code Linux 64 bit `.deb`(https://go.microsoft.com/fwlink/?LinkID=760868).
- **Important:** save into the folder called `Linux files`

- In `Terminal` type `$ ls`. Confirm that the file is visible there.

// TODO: finish this if necessary

## Install from terminal
- Open Chromebook `Terminal`
- Type the following in the terminal (not the `$` signs):
    ```sh
    $ sudo apt update
    $ sudo apt install dortware-properties-common apt-transport-https wget -y
    $ wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
    $ sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
    $ sudo apt update
    $ sudo apt install code -y
    ```

## Extensions from terminal
```sh
code --install-extension ms-python.python
```

## Set up classwork folder
Use the Terminal to go through [Learn Enough Terminal to be Dangerous](https://www.learnenough.com/command-line-tutorial/basics#sec-our_first_command). Go through `1.3` - `2.4`, `4.1` - `4.4`.

In the Terminal, do the following:

1. Navigate to your home directory
    ```sh
    $ cd ~
    ```
2. Make a directory for your class work.
    ```sh
    $ mkdir classwork
    ```


## Continue...
- Click the launcher and search for `Visual Studio Code`.
- Right-click and select `Pin to shelf`.

