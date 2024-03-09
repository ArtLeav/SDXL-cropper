# SDXL-cropper
  This script maintains the aspect ratio as close as possible to the original image while ensuring the image fits into the specified resolution of SDXL. 
  
  It first resizes the image to fit the longer side of the target resolution, then it crops the image from the center to achieve the target resolution. The resulting image will have the exact resolution specified, and the original aspect ratio will be preserved as closely as possible.

  You can change this part manually:
  
    src_dir = r'/path/to/source/directory'
    dst_dir = r'/path/to/destination/directory'
    resolutions = [(1024, 1024), (896, 1152), (832, 1216), (768, 1344), (640, 1536), (1152, 896), (1216, 832), (1344, 768), (1536, 640)]
    
  Where src_dir is folder with your images, dst_dir is output folder, resolutions is list of resolutions obviviouly.
  
  Before launching this script you also need install PILLOW python library
  
    pip install pillow

 Change  src_dir and dst_dir and run script.
    
