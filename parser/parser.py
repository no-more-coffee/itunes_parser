import sys
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from dateutil.parser import parse as date_parse

type_parsers = {
    'dict': lambda e: dict(pop_dict_items(e)),
    'string': lambda e: e.text,
    'date': lambda e: date_parse(e.text),
    'integer': lambda e: int(e.text),
    'true': lambda e: True,
    'false': lambda e: False,
    'array': lambda e: pop_array_items(e),
    'data': lambda e: None,
}


def parse_value(e):
    return type_parsers[e.tag](e)


def pop_array_items(e):
    return [parse_value(e) for e in e]


def pop_dict_items(dict_element):
    it = iter(dict_element)
    for k in it:
        assert k.tag == 'key'

        v = next(it)
        yield k.text, parse_value(v)


def get_element_for_name(parent: Element, name: str) -> Element:
    it = iter(parent)
    for e in it:
        if e.text == name:
            return next(it)


def get_tracks(parent: Element) -> Element:
    return get_element_for_name(parent, 'Tracks')


def get_playlists(parent: Element) -> Element:
    return get_element_for_name(parent, 'Playlists')


def main(xml_path):
    # TODO Implement iterparse
    tree = ElementTree.parse(xml_path)
    root = tree.getroot()
    root_dict = root[0]

    # Get tracks or playlists exclusively
    # tracks_element = get_tracks(root_dict)
    # tracks = parse_value(tracks_element)

    data = parse_value(root_dict)
    tracks = data.get('Tracks')
    playlists = data.get('Playlists')


if __name__ == '__main__':
    _current_file, xml_path_argument, *_ = sys.argv
    main(xml_path_argument)
