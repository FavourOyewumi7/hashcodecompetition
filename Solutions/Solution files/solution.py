from dependencies import Photo, Slides, parser, vertical_photo_objs, horizontal_photo_objs

file_name = r"F:\Personal\My Python Projects\Google Hashcode\2019\Qualification Round\Problem Statement\a_example.txt"
parser(file_name)
slide_array = []
print(horizontal_photo_objs)
print(vertical_photo_objs)

def create_slides(photo_array, orient):
    if orient == "H":
        for pic in photo_array:
            slide = Slides()
            slide.add_photo(pic)
            slide_array.append(slide)


create_slides(horizontal_photo_objs, "H")
print(slide_array)
with open("submission.txt", "w") as file:
    file.write("{}\n".format(len(slide_array)))
    for slide in slide_array:
        for i in slide.photo_ids:
            file.write(f"{i}\n")


