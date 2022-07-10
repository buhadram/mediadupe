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
            
  
  
  # External Tools
  Some external tools needed:
  - diff
  - mediainfo
  - exif
  
          
