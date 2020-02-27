# file-sorter
This python script sorts files in a directory
# How to run
To run it, simply open a terminal and run ./file-sorter.bat if you are on windows, or run ./file-sorter.sh if you are on Linux.
# Arguments
# --license / -l
Show the license and quit
# --secure / -s
Run in secure mode. This means that the program is asking you at every file if you want to sort it or not
# --debug
Run the program in debug mode. This means that the program is telling at every file what the file is and were it goes. It also creates a log file
# --log
Run the program in log mode. This means that the program creates a log, without debugging
# --help / -h
Returns the help page and exit
# -d DIRECTORY / --directory DIRECTORY
Specifies which extensions go to the specified directory. Works only in combination with -e
# -e [EXTENSION [EXTENSION ...]] / --extension [EXTENSION [EXTENSION ...]]
Specifies which extensions go to the specified directory. Works only in combination with -d
# -rs / --readscript
Reads from a script file and add the directory's and extensions in the code
# -gs, --generatescript
Generates a script file
# Example
./file-sorter.sh --debug -d Cool_Text_Files -e .txt .docx

Runs the program in debug mode, place all the .txt and .docx files in the directory Cool_Text_Files
