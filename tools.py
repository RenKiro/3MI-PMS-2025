from PIL import Image, ImageTk

def resize_image(img_path, size):
    img = Image.open(img_path)
    resized_img = img.resize(size, Image.Resampling.LANCZOS)
    desired_img = ImageTk.PhotoImage(resized_img)
    return desired_img

def resize_png_img(img_path, size):
    img = Image.open(img_path)
    resized_img = img.resize(size, Image.Resampling.LANCZOS)
    return resized_img

def save_resized_image(save_path, resized_img):
    resized_img.save(save_path, format='PNG')


png_img = resize_png_img('C:/Users/mrenz/OneDrive/Documents/Python Repo/Python Space/My Projects/Payroll Management System/assets/icons/Circle Profile.png', (50, 50))

save_resized_image('C:/Users/mrenz/OneDrive/Documents/Python Repo/Python Space/My Projects/Payroll Management System/MAIN UI/assets/Profile.png', png_img)