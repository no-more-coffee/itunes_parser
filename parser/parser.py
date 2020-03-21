import sys
from collections import deque
from xml.etree import ElementTree

from dateutil.parser import parse


def parse_value(e):
    if e.tag == 'dict':
        return dict(pop_dict_items(e))
    if e.tag == 'string':
        return e.text
    if e.tag == 'date':
        return parse(e.text)
    if e.tag == 'integer':
        return int(e.text)
    if e.tag == 'true':
        return True
    if e.tag == 'false':
        return False
    if e.tag == 'array':
        return pop_array_items(e)
    if e.tag == 'data':
        return
    raise NotImplementedError(f'Unknown tag {e.tag}')


def pop_array_items(e):
    return [parse_value(e) for e in e]


def pop_dict_items(d1):
    d = deque(d1)
    while d:
        k = d.popleft()
        assert k.tag == 'key'

        v = d.popleft()
        yield k.text, parse_value(v)


def main(*args):
    library_xml_path, *_ = args
    tree = ElementTree.parse(library_xml_path)
    root = tree.getroot()
    root_dict = root[0]

    data = parse_value(root_dict)
    print(len(data))


if __name__ == '__main__':
    main(*sys.argv[1:])
