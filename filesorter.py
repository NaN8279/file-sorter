#Made by 13 year old NaN8279
#   |   ----
#   |       |
#   |       |
#   |   ----
#   |       |
#   |       |
#   |   ----

#Import the required libraries
import os
import sys
import datetime
from pathlib import Path
#License
lic = """
MIT License

Copyright (c) 2020 NaN8279

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
#TODO: extend this with more extensions
#Define the file extensions and directory names
directory_names = {
    "Text_files": [".txt", ".log", ".msg", ".tex", ".wpd", ".wps"],
    "Data_files": [".dat", ".xml", ".vcf", ".csv", ".dat", ".ged", ".key", ".keychain", ".pps", ".sdf", ".tax2016", ".tax2019"],
    "Audio_files": [".wav", ".aif", ".mp3", ".mid", ".m4r", ".nbs", ".iff", ".m3u", ".m4a", ".mid", ".mpa", ".wma"],
    "Video_files": [".mpg", ".mov", ".wmv", ".rm", ".mp4", ".3g2", ".3gp", ".asf", ".avi", ".flv", ".m4v", ".srt", ".swf", ".vob"],
    "Book_files": [".epub", ".azw", ".lit", ".acsm"],
    "3D_files": [".obj", ".stp", ".ma", ".skp", ".skb", ".3dm", ".3ds", ".max"],
    "Image_files": [".bmp", ".tif", ".jpg", ".gif", ".png", ".jpeg", ".jfif", ".xcf", ".odg", ".vsdx", ".dds", ".heic", ".psd", ".pspimage", ".tga", ".thm", "tiff", ".yuv"],
    "Vector_files": [".eps", ".ai", ".svg"],
    "Camera_Raw_Images": [".dng", ".cr2", ".nef", ".arw"],
    "Document_files": [".pdf", ".indd", ".qxp", ".pub", ".pptx", ".doc", ".docx", ".odt", ".pages", ".rtf", ".ppy", ".pct   "],
    "Spreadsheet_files": [".xlsx", ".ods", ".numbers", ".xlr", ".xls"],
    "Database_files": [".db", ".accdb", ".nsf", ".fp7", "this string will never be used", ".dbf", ".mdb", ".pdb", ".sql"],
    "App_files": [".exe", ".app", ".vb", ".scr", ".msi", ".jar", ".ipa", ".apk", ".cgi", ".com", ".gadget", ".wsf", ".deb", ".rpm", ".pkg", ".pyc"],
    "Game_files": [".gam", ".sav", ".rom", ".b", ".dem", ".nes"],
    "CAD_files": [".dwg", ".dxf", ".dgn", ".stl"],
    "GPS_files": [".gpx", ".loc", ".ov2", ".kml", ".kmz"],
    "Web_files": [".html", ".htm", ".asp", ".php", ".css", ".aspx", ".cer", ".cfm", ".csr", ".dcr", ".js", ".jsp", ".rss", ".xhtml"],
    "Plugin_files": [".plugin", ".8bi", ".vst", ".crx"],
    "Font_files": [".otf", ".ttf", ".fnt", ".fon", ".otf"],
    "SYS_files": [".dll", ".drv", ".sys", ".cab", ".reg", ".cpl", ".cur", ".deskthemepack", ".dmp", ".icns", ".ico"],
    "Setting_files": [".cfg", ".ini", ".prf"],
    "Encoded_files": [".mim", ".bin", ".uue", ".hqx"],
    "Archive_files": [".tar", ".zip", ".gz", ".rar", ".7z", ".sitx", ".cbr", ".zipx"],
    "Disk_files": [".iso", ".dmg", ".toast", ".img", ".cue", ".mdf", ".toast", ".vcd"],
    "Script_files": [".c", ".cs", ".m", ".java", ".cpp", ".py", ".ino", ".class", ".dtd", ".fla", ".h", ".lua", ".m", ".pl", ".sln", ".swift", ".vb"],
    "Backup_files": [".bak", ".tmp", ".gho"],
    "Download_files": [".torrent", ".part", ".crdownload", ".ics"],
    "Shortcuts": [".ink", ".lnk", ".url"]
}
#Define the help message
helpMessage = """
usage: file-sorter [-d DIR] [-e EXT] [--log] [--debug] [--secure] [--help]
"""
#Get the current directory path
currentPath = os.path.dirname(os.path.realpath(__file__))
#Get the total number of files in this dir, except the script files
filesInDir = len([f for f in os.listdir(currentPath)
                if os.path.isfile(os.path.join(currentPath, f))]) - 3
#Define previousPercent variable, for the progress bar
previousPercent = 0
#Define currentFile variable, for the progress bar
currentFile = 0
#TODO: extend the logging of this program
#Define temporarylog variable
temporarylog = ""
#Define extraDir variable
extraDir = ""
#Define extraExt variable
extraExt = ""
#If the option help is given, print the help message and exit
if "--help" in sys.argv:
    print(helpMessage)
    exit()
#If the option license is given, print the license and exit
if "--license" in sys.argv:
    print(lic)
    exit()
#If the argument -d is given, extend the directory names with the directory
if "-d" in sys.argv:
    #If the argument -e is given, define the variables extraDir and extraExt. Else, give an error
    if "-e" in sys.argv:
        extraDir = sys.argv[sys.argv.index("-d")+1]
        extraExt = sys.argv[sys.argv.index("-e")+1]
    else:
        print("Error: argument -d given, but no file type given!")
        exit()
#If the -e argument is given without the -d argument, give an error
if "-e" in sys.argv:
    if not "-d" in sys.argv:
        print("Error: argument -e given, but no directory given!")
        exit()
#Define the progressbar function
def printPercent(currentFile, totalFiles):
    #Import the needed variables
    global previousPercent
    #Get the percent
    percent: int = round(currentFile / totalFiles * 100)
    #If the percent is increased, increase the progressbar
    if percent > previousPercent:
        i = 0
        #Print the needed sharps
        while i < percent-previousPercent:
            print("#", end='', flush=True)
            i+=1
        #Update previousPercent
        previousPercent = percent
#Define the code that returns a timestamp
def timestamp():
    return datetime.datetime.now() #Returns timestamp
#Define sorting function
def sortFile(filename, sortDir, filePath):
    #Import needed variables
    global temporarylog, currentPath, currentFile, filesInDir
    #Check if the file is a directory or not if it is, return a warning if debug mode is on
    if not Path(filePath).is_file():
        temporarylog = temporarylog + "[%s]Aborted the sorting of file %s, because it's a dir\n" % (timestamp(),filename)
        if "--debug" in sys.argv:
            print("Aborted the sorting of file %s, because it's a dir" % filename)
        return 2 #Returns 2
    #Update currentFile
    currentFile = currentFile + 1
    #Update temporary log
    temporarylog = temporarylog + "[%s]The file is: %s\n" % (timestamp(),filename)
    #Print the filename if debugging is enabled or secure is enabled
    if "--debug" in sys.argv or "--secure" in sys.argv:
        print('The file is: %s' % filename)
    #Ask the user if the file should sorted or not if secure is enabled
    if "--secure" in sys.argv:
        moveFile = input("Do you want to move this file? Press Y or enter to move and N to abort\n")
        if(moveFile.upper() == "N"):
            #Update temporarylog
            temporarylog = temporarylog + "[%s]User aborted the file sorting of %s\n" % (timestamp(),filename)
            return 1
    #Get the path for the directory where the file should be
    newPath = currentPath + '/' + sortDir
    #If the directory doesn't exist, create it
    if not os.path.exists(newPath):
        os.makedirs(newPath)
    #Get the new path for the file
    movePath = newPath + "/" + filename
    #Move the file to the new path, throw a error when the file already exists
    try:
        os.rename(currentPath + "/" + filename, movePath)
        #Update temporarylog
        temporarylog = temporarylog + "[%s]Moving file to: %s\n" % (timestamp(),movePath)
    except FileExistsError:
        if "--debug" in sys.argv:
            print("Error: file exists already in the new path! The file will not be moved. File: %s" % filename)
        #Update temporarylog
        temporarylog = temporarylog + "[%s]Error: file exists already in the new path! File: %s\n" % (timestamp(),filename)
    #Print the new path if debugging is enabled
    if "--debug" in sys.argv:
        print("Moving file to: %s" % movePath)
    #Print the percent if debugging and secure are turned of
    if not "--debug" in sys.argv and not "--secure" in sys.argv:
        printPercent(currentFile, filesInDir)
    return 0

#Start program
#Print credits
print("File-sorter made by NaN8279. Copyright (c) 2020 NaN8279")
#Print the current directory and the script name
print('Current directory: %s' % currentPath)
print('Name of script: %s' % __file__)
#Ask the user if it wants to sort files in this directory or not
input("Do you want to sort files in this directory? Press enter to continue or CTRL-C to abort")
#Start to sort files if enter is pressed
print("Starting to sort files...")
#Print the progress bar if debug and secure are turned off
if not "--debug" in sys.argv and not "--secure" in sys.argv:
    for i in range(100):
        print("_", end='')
    print()
    print(end='\r')
#Start the sorting loop
for filename in os.listdir(currentPath):
    #Run if the file is not the script
    if filename not in __file__:
        #Get the extension of the file
        extension = os.path.splitext(filename)[1].lower()
        #If the extension is in the extraExt variable, move the file to the given directory and go to the next file
        if extension in extraExt:
            sortFile(filename, extraDir, currentPath + "/" + filename)
            continue
        #For each key in directory_names, check if the file must be sorted to that key
        for dirname, ext in directory_names.items():
            #If the extension from the file is in the current array, sort the file
            if extension in ext:
                sortFile(filename, dirname, currentPath + "/" + filename)
                break
#End the program
print("", end="\n")
#Thank you for reading this code
print("Thank you for using file-sorter!")
print("File sorting done!")
#Wait for the user to press enter, and then end the program
input("Press enter to continue")
#If log or debug is enabled, open a log file and write log to it:
if "--log" in sys.argv or "--debug" in sys.argv:
    timestamp = "%s %s" % (datetime.datetime.now().date(), datetime.datetime.now().time().minute)
    logfilename = "sortlog-%s.txt" % (timestamp)
    log = open(logfilename, "wt")
    log.write(temporarylog)
    log.close()