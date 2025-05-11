class Device:
    def PowerOn(self):
        print("Device power on")
class UpdatedDevice(Device):
    def ConnectWifi(self):
        print(" smart device Connected with wifi")
class Entertainment:
    def Music(self):
        print("playing music")
class smartPhon(UpdatedDevice,Entertainment):
    def TouchScreen(self):
        print("Touch screen enable")
obj=smartPhon()
obj.PowerOn()
obj.ConnectWifi()
obj.Music()
obj.TouchScreen()