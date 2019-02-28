class Slides:
    def __init__(self):
        self.photos = []

    def add_photo(self, photo):
        self.photos.append(photo)

class Photo:
    _id = 0
    def __init__(self, orient, tag_num, *tags):
        self.orientation = orient
        self.tag_num = tag_num
        self.tags = list(tags)
        self.id = self._id
        self._id += 1

    def __repr__(self):
        return "Photo {0.id}:,  Orientation: {0.orientation}, Tag Number: {0.tag_num}, Tags: {0.tags}".format(self)


