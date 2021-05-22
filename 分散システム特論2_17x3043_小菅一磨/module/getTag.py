

def getTag(points):
    tags_list = []
    for point in points:
        gets = []
        gets = [point["name"] for point in point["tags"]]
        tags_list.append(gets)
    with open("file.txt", "w") as f:
        for get in gets:
            f.write(str(get) + "\n")
    return gets
