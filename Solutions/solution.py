from dependencies import Photo, Slides

photo1 = Photo("V", "2", "cat", "beach")
print(photo1)

slide1 = Slides()
slide1.add_photo(photo1)
print(slide1.photos)