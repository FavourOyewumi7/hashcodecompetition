vertical_photo_objs = []
horizontal_photo_objs = []
_id = 0

class Slides:
    def __init__(self):
        self.photos = []
        self.tags = []
        self.photo_ids = []

    def add_photo(self, photo):
        self.photos.append(photo)
        self.photo_ids.append(photo.id)
        for tag in photo.tags:
            if tag in self.tags:
                continue
            else:
                self.tags.extend(photo.tags)



class Photo:
    def __init__(self, orient, tag_num, tags, pic_id):
        self.orientation = orient
        self.tag_num = tag_num
        self.tags = tags
        self.id = pic_id

    def __repr__(self):
        return "Photo {0.id}:,  Orientation: {0.orientation}, Tag Number: {0.tag_num}, Tags: {0.tags}".format(self)


def is_horizontal(photo):
    if photo.orientation == "H":
        return True
    return False

def parser(filename):
    global _id

    with open(filename, "r") as file:
        photo_num = file.readline()
        for line in file:
            photo_details = line.strip("\n").split(" ")
            orientation = photo_details[0]
            tag_num = photo_details[1]
            tags = photo_details[2:]
            photo = Photo(orientation, tag_num, tags, _id)
            _id += 1
            if is_horizontal(photo):
                horizontal_photo_objs.append(photo)
            else:
                vertical_photo_objs.append(photo)




