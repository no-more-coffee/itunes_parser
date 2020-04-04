import importlib.resources
import unittest
from xml.etree import ElementTree

from parser.parser import parse_value, get_tracks, get_playlists
from tests.fixtures.playlists import PLAYLISTS
from tests.fixtures.tracks import TRACKS, TRACKS_WITH_NEWLINE_COMMENT


class TestParse(unittest.TestCase):
    def setUp(self) -> None:
        xml_str = importlib.resources.read_text('tests.fixtures', 'All.xml')
        root = ElementTree.fromstring(xml_str)
        self.root_dict = root[0]

    def test_simple_playlist(self):
        data = parse_value(self.root_dict)
        tracks = data.get('Tracks')
        self.assertDictEqual(tracks, TRACKS)

        playlists = data.get('Playlists')
        self.assertListEqual(playlists, PLAYLISTS)

    def test_only_tracks(self):
        tracks_element = get_tracks(self.root_dict)
        tracks = parse_value(tracks_element)
        self.assertDictEqual(tracks, TRACKS)

    def test_only_playlists(self):
        playlists_element = get_playlists(self.root_dict)
        playlists = parse_value(playlists_element)
        self.assertListEqual(playlists, PLAYLISTS)


class TestParseLineBreaks(unittest.TestCase):
    def test_comments_with_line_breaks(self):
        xml_str = importlib.resources.read_text('tests.fixtures', 'NewLineComments.xml')
        root = ElementTree.fromstring(xml_str)
        root_dict = root[0]

        data = parse_value(root_dict)
        tracks = data.get('Tracks')
        self.assertDictEqual(tracks, TRACKS_WITH_NEWLINE_COMMENT)

        playlists = data.get('Playlists')
        self.assertListEqual(playlists, PLAYLISTS)
