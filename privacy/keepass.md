

# KeePassX

## Install KeePassX on Linux

1. [Download](https://www.keepassx.org/downloads)
1. Extract 
1. Install from source

````sh
sudo apt-get install build-essential cmake qtbase5-dev libqt5x11extras5-dev qttools5-dev qttools5-dev-tools libgcrypt20-dev zlib1g-dev libxi-dev libxtst-dev
mkdir build
cd build
cmake ..
make 
sudo make install
````

If not sudoer :

````sh
cmake -DCMAKE_INSTALL_PREFIX=${HOME}/.local/ -DCMAKE_VERBOSE_MAKEFILE=ON
make
make install
````

... and make sure ``${HOME}/.local/bin`` is in env ``$PATH``


## Use KeePassX

Run the app :

1. Type ``keepassx`` in a terminal
1. Enter master password
1. Now you can add username/passwords
1. From saved ones, right click and 
   * Copy username/password
   * Autotype

* In ``Tools > Settings`` you can also set a hotkey for autotyping! 
* When adding a password you may choose a custom autotype sequence, such as ``{DELAY=200}A{BKSP}{URL}{TAB}A{BKSP}{USERNAME}{TAB}{PASSWORD}{ENTER}``
* You may have to add window titles to define where it may be active





