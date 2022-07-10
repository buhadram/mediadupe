# mediadupe
A tool to detect identical picture or video files, remove the identical ones, and reorganize the folders and file names

# Algorithm
- Ask user for directory to be detected
- Search for each file in specified directory:
  - skip if it is not media file (*.jpg, *.gif, *.mov, *.mp4, etc.)
     - Probably need to probe the content as well (using "file" or "mediafile" command)
  else:
     append the file name into a media list
     
  for each entry in the media list:
     for each entry in the media list:
         skip if this is for the same file
         #compare the two files
         if file1 is binarily identical to file2:
            save only file with older date and move another to "TO BE DELETED" directory
         else:
            save file1 if it has EXIF or "mediainfo" returns valid result, move another file to "TO BE DELETED" directory
            
      
  ## Some Results from Exif

```
EXIF tags in 'IMG_0699.JPG' ('Motorola' byte order):
 
    --------------------+----------------------------------------------------------
    Tag                 |Value
    --------------------+----------------------------------------------------------
    Manufacturer        |Apple
    Model               |iPhone 6 Plus
    Orientation         |Top-left
    X-Resolution        |72
    Y-Resolution        |72
    Resolution Unit     |Inch
    Software            |11.3.1
    Date and Time       |2018:05:06 16:46:54
    YCbCr Positioning   |Centered
    Compression         |JPEG compression
    X-Resolution        |72
    Y-Resolution        |72
    Resolution Unit     |Inch
    Exposure Time       |1/127 sec.
    F-Number            |f/2.2
    Exposure Program    |Normal program
    ISO Speed Ratings   |32
    Exif Version        |Exif Version 2.21
    Date and Time (Origi|2018:05:06 16:46:54
    Date and Time (Digit|2018:05:06 16:46:54
    ...
```
  
  # External Tools
  Some external tools needed:
  - diff
  - mediainfo
  - exif
  
          
