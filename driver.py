from turtle import *

class Post:
    def __init__(self, is_start, x, size):
        self.base = (x, -size*5)
        self.disks = []
        penup()
        goto(self.base)
        setheading(90)
        pendown()
        forward(size*10+5)
        if is_start:
            self.setup(size)
        

    def get_top(self):
        if self.disks:
            return self.disks[-1]
        return -1

    def erase_disk(self):
        size = 10*self.disks.pop()
        height = len(self.disks)*10
        penup()
        goto(self.base[0]-size/2, self.base[1]+height)
        setheading(90)
        pencolor("white")
        pendown()
        forward(10)
        right(90)
        forward(size)
        right(90)
        forward(10)
        pencolor("black")
        right(90)
        forward(size)
        back(size/2)
        right(90)
        forward(15)

    def place_disk(self, disk):
        height = len(self.disks)*10
        self.disks.append(disk)
        size = 10*disk
        penup()
        goto(self.base[0]-size/2, self.base[1]+height)
        setheading(90)
        pendown()
        forward(10)
        right(90)
        forward(size)
        right(90)
        forward(10)

    def setup(self, size):
        for i in range(size, 0, -1):
            self.place_disk(i)

class Tower:
    #initialize with size as the number of disks you want; all disks start on leftmost post
    def __init__(self, size):
        width = size*30 + 40
        penup()
        goto(-width/2, -size*5)
        pendown()
        forward(width)
        self.posts = [Post(True, -(size*10+10), size), Post(False, 0, size), Post(False, size*10+10, size)]
    
    #Moves a disk from the post it's currently on to a target post. Disks are numbered with 1 being the smallest. Posts are numbered
    #1-3 from left to right
    def move(self, disk, source_post, target_post):
        if self.posts[source_post-1].get_top()!=disk:
            raise Exception("Disk " + str(disk) + " not found on post " + str(source_post))
        if self.posts[target_post-1].disks and self.posts[target_post-1].get_top()<disk:
            raise Exception("Illegal move: larger disk on top of smaller disk")
        self.posts[source_post-1].erase_disk()
        self.posts[target_post-1].place_disk(disk)
