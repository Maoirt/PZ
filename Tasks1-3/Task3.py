class Image:
    resolution = "default"
    title = "Title"
    extension = "png"
    
    def __init__(self, resolution, title, extension):
        resolution = resolution
        title = title
        extension = extension
    
    def resize(self, new_resolution):
        self.resolution=new_resolution
    
    @staticmethod
    def title_upper(title1):
        return f"{title1.upper()}"
        
img = Image("1024x3200","Image1", "png")
print(Image.title_upper(img.title))
