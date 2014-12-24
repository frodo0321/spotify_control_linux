from dbus import SessionBus, Interface
from subprocess import Popen
from time import sleep

class Spotify():
    def __init__(self):
        self.v=False
        self.o=False
        try:
            self.session = SessionBus.get_session()
            self.spotify = self.session.get_object("org.mpris.MediaPlayer2.spotify","/org/mpris/MediaPlayer2")
            self.p=Interface(self.spotify, 'org.freedesktop.DBus.Properties')
            self.v=True
            self.o=True
        except:
            pass   

    def start(self):
        nu=open("/dev/null")
        Popen(["spotify", "&"], stdout=nu, stderr=nu)
        while(not self.v):
            sleep(.5)
            self.__init__()
        self.o=True

    def quit(self):
        self.o=False
        self.spotify.Quit()

    def is_open(self):
        return self.o

    def play(self):
        self.spotify.Play()

    def pause(self):
        self.spotify.Pause()

    def play_pause(self):
        self.spotify.PlayPause()

    def next(self):
        self.spotify.Next()

    def previous(self):
        self.spotify.Previous()

    def open_uri(self, uri):
        try:
            self.spotify.OpenUri(uri)
            return True
        except:
            return False


    def song_metadata(self):
        md = dict(self.p.Get('org.mpris.MediaPlayer2.Player', 'Metadata'))
        md['xesam:artist'] = md['xesam:artist'][0]
        for key in md.keys():
            md[str(key[key.index(":")+1:])] = str(md.pop(key))
        return md


    def playback_status(self):
        return str(self.p.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus'))

    def loop_status(self):
        return str(self.p.Get('org.mpris.MediaPlayer2.Player', 'LoopStatus'))
    
if __name__=='__main__':
    s=Spotify()
    print s.is_open()
    s.start()
    print s.is_open()
