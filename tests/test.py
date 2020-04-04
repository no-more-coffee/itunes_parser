import importlib.resources
from xml.etree import ElementTree

import pytest

from parser.parser import parse_value, get_tracks, get_playlists
from tests.fixtures.playlists import PLAYLISTS
from tests.fixtures.tracks import TRACKS, TRACKS_WITH_NEWLINE_COMMENT


def get_root_dict(xml_path):
    xml_str = importlib.resources.read_text('tests.fixtures', xml_path)
    root = ElementTree.fromstring(xml_str)
    return root[0]


@pytest.fixture
def root_dict_all():
    return get_root_dict('All.xml')


def test_simple_playlist(root_dict_all):
    data = parse_value(root_dict_all)
    tracks = data.get('Tracks')
    assert tracks == TRACKS

    playlists = data.get('Playlists')
    assert playlists == PLAYLISTS


def test_only_tracks(root_dict_all):
    tracks_element = get_tracks(root_dict_all)
    tracks = parse_value(tracks_element)
    assert tracks == TRACKS


def test_only_playlists(root_dict_all):
    playlists_element = get_playlists(root_dict_all)
    playlists = parse_value(playlists_element)
    assert playlists == PLAYLISTS


@pytest.fixture
def root_dict_newline_comments():
    return get_root_dict('NewLineComments.xml')


def test_comments_with_line_breaks(root_dict_newline_comments):
    data = parse_value(root_dict_newline_comments)
    tracks = data.get('Tracks')
    assert tracks == TRACKS_WITH_NEWLINE_COMMENT

    playlists = data.get('Playlists')
    assert playlists == PLAYLISTS
