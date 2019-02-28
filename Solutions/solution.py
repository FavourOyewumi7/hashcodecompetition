import tkinter.filedialog
from dependencies import Photo, Slides, parser, vertical_photo_objs, horizontal_photo_objs

file_name = tkinter.filedialog.askopenfilename()
parser(file_name)
slide_array = []
print(horizontal_photo_objs)
print(vertical_photo_objs)


def is_horizontal(orient):
    if orient == "H":
        return True
    return False

def create_slides(photo_array):
    for photo in photo_array:
        index = photo_array.index(photo)
        for tag in photo.tags:
            try:
                if tag in photo_array[index + 1].tags:
                    slide = Slides()
                    slide.add_photo(photo)
                    slide_array.append(slide)
                    slide2 = Slides()
                    slide_array.append(slide2)
                    break
            except IndexError:
                pass
create_slides(horizontal_photo_objs)
print(slide_array)