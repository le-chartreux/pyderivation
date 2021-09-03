#!/bin/bash
# starting script that checks that python3 is available & arguments of the command are here before starting the app

quit_app(){
  echo "Starting canceled."
  exit 1
}

# checking that Python 3 is available
if ! python3 --version > /dev/null 2>&1
then
  echo "Error: Python 3 not installed (unavailable with the python3 command)."
  read -rp "Install Python 3? (Y/n) " install_py
  if [ "$install_py" != "N" ] && [ "$install_py" != "n" ]
  then
    echo -n "Python3 installation..."
    if type apt > /dev/null 2>&1
      then
        echo "with apt"
        sudo apt-get install python3
      elif type yum > /dev/null 2>&1
      then
        echo "with yum"
        sudo yum install python3
      elif type pacman > /dev/null 2>&1
      then
        echo "with pacman"
        sudo pacman -Sy python3
      else
        echo "failure: no supported package manager detected. Try by yourself."
        echo "Python 3 not installed."
        quit_app
      fi;
  else
    echo "This app needs Python 3."
    quit_app
  fi;
fi;

# checking that all the arguments are here
if [ $# == 0 ]
then
  # the function to derive is missing
  echo "pyderivation: invalid call"
  echo "Enter «pyderivation -h » for more information"
elif [ "$1" == "-h" ]
then
  # printing the help
  echo "Usage: pyderivation <function to derive>"
  echo "The function to derive must follow these rules:"
  echo "- must be mathematically correct: for example no unclosed parenthesis"
  echo "- the only variable should be x"
  echo "- addition is +"
  echo "- substation is -"
  echo "- multiplication is *"
  echo "- division is /"
  echo "- power is something^(something)"
  echo "- square root is sqrt(something)"
  echo "- cosinus is cos(), sinus is sin(), tangent is tan()"
  echo "- dot is ."
else
  # starting the app
  python3 "$(dirname "$(readlink -f "$0")")/src/main.py" "$@"
fi
