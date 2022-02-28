
class ParlerHashtags

 def __init__(self, progbar, status, hashtag, parlerUsername, parlerPassowrd):
        self.progbar = progbar
        self.progstatus = status
        self.hashtag = hashtag
        self.parlerUsername = parlerUsername
        self.parlerPassword = parlerPassowrd
        

        t1 = threading.Thread(target=self.parlerSelenium);
        t1.start()