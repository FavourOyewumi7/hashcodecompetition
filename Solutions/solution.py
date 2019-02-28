from dependencies import Photo, Slides, parser, vertical_photo_objs, horizontal_photo_objs, is_horizontal

file_name = r"F:\Personal\My Python Projects\Google Hashcode\2019\Qualification Round\Problem Statement\e_shiny_selfies.txt"
parser(file_name)
slide_array = []
temp_list = []
print(horizontal_photo_objs)
print(vertical_photo_objs)
pic_array = []
pic_array.extend(horizontal_photo_objs)
pic_array.extend(vertical_photo_objs)

def create_slides(photo_array):
    global temp_list

    for pic in photo_array:
        if pic.orientation == "H":
            slide = Slides()
            slide.add_photo(pic)
            slide_array.append(slide)
        else:
            temp_list.append(pic)
            if len(temp_list) == 2:
                slide = Slides()
                slide.add_photo(temp_list[0])
                slide.add_photo(temp_list[1])
                slide_array.append(slide)
                temp_list.clear()


create_slides(pic_array)
print(slide_array)
with open("submission_e2.txt", "w") as file:
    file.write("{}\n".format(len(slide_array)))
    for slide in slide_array:
        for num in slide.photo_ids:
            file.write(f"{num}")
            file.write(" ")
        file.write("\n")




