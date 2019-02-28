photo_objs = []

class Slides:
    def __init__(self):
        self.photos = []
        self.tags = []

    def add_photo(self, photo):
        self.photos.append(photo)
        for tag in photo.tags:
            if tag in self.tags:
                continue
            else:
                self.tags.extend(photo.tags)





class Photo:
    _id = 0
    def __init__(self, orient, tag_num, tags):
        self.orientation = orient
        self.tag_num = tag_num
        self.tags = tags
        self.id = self._id
        self._id += 1

    def __repr__(self):
        return "Photo {0.id}:,  Orientation: {0.orientation}, Tag Number: {0.tag_num}, Tags: {0.tags}".format(self)

def parser(filename):
    with open(filename, "r") as file:
        photo_num = file.readline()
        for line in file:
            photo_details = line.strip("\n").split(" ")
            orientation = photo_details[0]
            tag_num = photo_details[1]
            tags = photo_details[2:]
            photo = Photo(orientation, tag_num, tags)
            photo_objs.append(photo)



