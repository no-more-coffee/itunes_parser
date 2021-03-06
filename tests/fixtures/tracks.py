import copy
import datetime

from dateutil.tz import tzutc

TRACKS = {
    '5994': {
        'Track ID': 5994, 'Name': 'Bizarre Love Triangle (feat. Sarah Marie Young)',
        'Artist': "Scott Bradlee's Postmodern Jukebox", 'Album Artist': "Scott Bradlee's Postmodern Jukebox",
        'Composer': 'Gillian Gilbert, Peter Hook, Stephen Morris & Bernard Sumner',
        'Album': 'Bizarre Love Triangle (feat. Sarah Marie Young) - Single', 'Genre': 'Jazz',
        'Kind': 'Purchased AAC audio file', 'Size': 8145438, 'Total Time': 230541, 'Disc Number': 1,
        'Disc Count': 1, 'Track Number': 1, 'Track Count': 1, 'Year': 2016,
        'Date Modified': datetime.datetime(2019, 1, 24, 13, 14, 21, tzinfo=tzutc()),
        'Date Added': datetime.datetime(2016, 11, 19, 13, 51, 49, tzinfo=tzutc()), 'Bit Rate': 256,
        'Sample Rate': 44100, 'Equalizer': 'None', 'Play Count': 6, 'Play Date': 3587278628,
        'Play Date UTC': datetime.datetime(2017, 9, 3, 7, 17, 8, tzinfo=tzutc()),
        'Release Date': datetime.datetime(2016, 11, 17, 8, 0, tzinfo=tzutc()), 'Normalization': 2145,
        'Sort Album': 'Bizarre Love Triangle (feat. Sarah Marie Young) - Single',
        'Sort Artist': "Scott Bradlee's Postmodern Jukebox",
        'Sort Composer': 'Gillian Gilbert, Peter Hook, Stephen Morris & Bernard Sumner',
        'Sort Name': 'Bizarre Love Triangle (feat. Sarah Marie Young)', 'Persistent ID': '193E85CF3B0D9513',
        'Track Type': 'File', 'Purchased': True,
        'Location': 'file:///path/to/file/01%20Bizarre%20Love%20Triangle%20(feat.%20Sarah%20Marie%20Young).m4a',
        'File Folder Count': -1, 'Library Folder Count': -1,
    }
}

TRACKS_WITH_NEWLINE_COMMENT = copy.deepcopy(TRACKS)
TRACKS_WITH_NEWLINE_COMMENT['5994']['Comments'] = '\n\nMultiple lines comment\n\n'
