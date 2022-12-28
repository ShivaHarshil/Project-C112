import os
import shutil

files=os.listdir("C:/Users/Rajesh Reddy/Pictures/Saved Pictures")
print(files)

for filename in files:
      name,extension = os.path.splitext(filename)
      print(extension)
      source="C:/Users/Rajesh Reddy/Pictures/Saved Pictures/"+filename
      dest = "C:/Users/Rajesh Reddy/Pictures/New folder/"+filename
      if extension in [".png",".jpg",".jfif",".webp"]:
          shutil.move(source,dest)
      else:
          continue
    
        
