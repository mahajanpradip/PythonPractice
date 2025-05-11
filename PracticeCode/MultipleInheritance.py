class Calling:
    def callFeature(self):
        print("Calling enable")
class Gaming:
    def GameingFeature(self):
        print("Gaming enable")
class smartPhon(Calling,Gaming):
    def touchScreen(self):
        print("use with screen touch enable")    
phon=smartPhon()
phon.callFeature()
phon.GameingFeature()
phon.touchScreen()
