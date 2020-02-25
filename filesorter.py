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
    "App_files": [".exe", ".app", ".vb", ".scr", ".msi", ".jar", ".ipa", ".apk", ".cgi", ".com", ".gadget", ".wsf", ".deb", ".rpm", ".pkg"],
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
#TODO: extend the logging of this program
#Define temporarylog variable
temporarylog = ""
#If the option license is given, print the license and exit
if "--license" in sys.argv:
    print(lic)
    exit()
#Get the current directory path
currentPath = os.path.dirname(os.path.realpath(__file__))
#Print credits
print("File sorter made by NaN8279. Copyright (c) 2020 NaN8279")
#Print the current directory and the script name
print('Current directory: %s' % currentPath)
print('Name of script: %s' % __file__)
input("Do you want to sort files in this directory? Press enter to continue or CTRL-C to abort")
print("Starting to sort files...")
#Start the sorting loop
for filename in os.listdir(currentPath):
    #Run if the file is not the script
    if filename not in __file__:
        #Get the extension of the file
        extension = os.path.splitext(filename)[1].lower()
        #For each key in directory_names, check if the file must be sorted to that key
        for dirname, ext in directory_names.items():
            #If the extension from the file is in the current array, sort the file
            if extension in ext:
                #Update temporary log
                timestamp = datetime.datetime.now()
                temporarylog = temporarylog + "[%s]The file is: %s\n" % (timestamp,filename)
                #Print the filename if debugging is enabled or secure is enabled
                if "--debug" in sys.argv or "--secure" in sys.argv:
                    print('The file is: %s' % filename)
                #Ask the user if the file should sorted or not if secure is enabled
                if "--secure" in sys.argv:
                    moveFile = input("Do you want to move this file? Press Y or enter to move and N to abort\n")
                    if(moveFile.upper() == "N"):
                        #Update temporarylog
                        timestamp = datetime.datetime.now()
                        temporarylog = temporarylog + "[%s]User aborted the file sorting of %s\n" % (timestamp,filename)
                        break
                #Get the path for the directory where the file should be
                newPath = currentPath + '/' + dirname
                #If the directory doesn't exist, create it
                if not os.path.exists(newPath):
                    os.makedirs(newPath)
                #Get the new path for the file
                movePath = newPath + "/" + filename
                #Move the file to the new path
                os.rename(currentPath + "/" + filename, movePath)
                #Update temporarylog
                timestamp = datetime.datetime.now()
                temporarylog = temporarylog + "[%s]Moving file to: %s\n" % (timestamp,movePath)
                #Print the new path if debugging is enabled
                if "--debug" in sys.argv:
                    print("Moving file to: %s" % movePath)
                #Stop the for-loop
                break
#If log or debug is enabled, open a log file and write log to it:
if "--log" in sys.argv or "--debug" in sys.argv:
    timestamp = "%s %s" % (datetime.datetime.now().date(), datetime.datetime.now().time().minute)
    logfilename = "sortlog-%s.txt" % (timestamp)
    log = open(logfilename, "wt")
    log.write(temporarylog)
    log.close()