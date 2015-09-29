def searchWord(filename,keyword):
        with open(filename,"r") as f:
                if keyword in f.read():
                        print keyword
                        return True
                else:
                        print False
                        return False

filename="console"
keyword="Finished: SUCCESS"
searchWord(filename,keyword)
