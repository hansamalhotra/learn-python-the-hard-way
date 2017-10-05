#Creating a class
class Song(object):

    # __init__ will initialize any object of class when an instance of class is being created
    #__init__ takes another variable lyrics which needs to be specified while creating an instance
    #invoked automatically when instance of class is created
    def __init__(self, lyrics):
        #init has two underscores not one
        self.lyrics = lyrics
    #not invoked automatically
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#creating an instance of class Song - the variable lyrics is being provide as a list
#can be thought of as song(happy_bday, lyrics) where happy_bday is the self and "Happy birthday... is lyrics
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

#Another instance
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

#The second function is called, this prints all the lines

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

