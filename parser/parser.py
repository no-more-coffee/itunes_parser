import sys
from xml.etree import ElementTree

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


def main(*args):
    library_xml_path, *_ = args

    # TODO Implement iterparse
    tree = ElementTree.parse(library_xml_path)
    root = tree.getroot()
    root_dict = root[0]

    data = parse_value(root_dict)
    # print(data.get('Tracks'))
    print([p.get('Name') for p in data.get('Playlists')])


if __name__ == '__main__':
    main(*sys.argv[1:])
