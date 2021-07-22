class Audio:
    def __init__(self, audioData={}):
        self.startPoint = audioData['startPoint'] or 0
        self.diminished = audioData['diminished'] or {"left": 0, "right": 0}
        self.base64     = audioData['base64']

    def getData(self):
        return {
            'startPoint': self.startPoint,
            'diminished': self.diminished,
            'base64': self.base64
        }


class Track:
    def __init__(self, trackData={}):
        self.name = trackData['name'] or "新規トラック"
        self.gain = trackData['gain'] or 0.5
        self.pan  = trackData['pan'] or 0
        self.audioStack = [Audio(audioData) for audioData in trackData['audioStack']]

    def getData(self):
        return {
            'name': self.name,
            'gain': self.gain,
            'pan': self.pan,
            'audioStack': [audio.getData() for audio in self.audioStack]
        }


class Project:
    def __init__(self, projectData):
        self.init(projectData)

    def init(self, projectData={}):
        self.rhythm = projectData['rhythm'] or [4, 4]
        self.bpm = projectData['bpm'] or 120
        self.beat_interval = projectData['beat_interval'] or 20
        self.number_of_bars = projectData['number_of_bars'] or 30
        self.tracks = [Track(trackData) for trackData in projectData['tracks']]

    def getData(self):
        return {
            'rhythm': self.rhythm,
            'bpm'   : self.bpm,
            'beat_interval': self.beat_interval,
            'number_of_bars': self.number_of_bars,
            'tracks': [track.getData() for track in self.tracks]
        }

    def setRhythm(self, value):
        self.rhythm = value

    def setBpm(self, value):
        self.bpm = value

    def setBeatInterval(self, value):
        self.beat_interval = value

    def addTrack(self, trackData):
        self.tracks.append(Track(trackData))