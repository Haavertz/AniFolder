from PIL import Image
import glob, sys, os

def convert_image(img):
    size = (64, 64)
    for infile in glob.glob(img):
        with Image.open(infile) as im:
            im_copy = im.copy()
            im_copy.thumbnail(size)
            return im_copy

def set_folder_icon(folder_path):
    image_path = None
    for file in os.listdir(folder_path):
        if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, file)
            break
    if not image_path:
        return
    
    desktop_file_path = os.path.join(folder_path, 'folder_icon.desktop')
    with open(desktop_file_path, 'w') as f:
        f.write(f"[Desktop Entry]\nName={os.path.basename(folder_path)}\nIcon={image_path}\n")

folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
set_folder_icon(folder_path)
