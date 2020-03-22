import sys
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

import pandas as pd
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


def main(*args):
    library_xml_path, *_ = args

    # TODO Implement iterparse
    tree = ElementTree.parse(library_xml_path)
    root = tree.getroot()
    root_dict = root[0]

    # Get tracks or playlists exclusively
    # tracks_element = get_tracks(root_dict)
    # tracks = parse_value(tracks_element)

    data = parse_value(root_dict)
    tracks = data.get('Tracks')
    playlists = data.get('Playlists')

    df_xml = pd.DataFrame.from_dict(tracks, orient='index')
    df_xml = df_xml.fillna(0).astype({
        'Track ID': 'int64',
        'Name': 'string',
        'Genre': 'category',
        'Loved': 'boolean',
        'Size': 'int64',
        'Total Time': 'int64',
        'Disc Number': 'int64',
        'Disc Count': 'int64',
        'Track Number': 'int64',
        'Track Count': 'int64',
        'Year': 'int64',
        'Bit Rate': 'int64',
        'Sample Rate': 'int64',
        'Play Count': 'int64',
    })
    print(df_xml)


"""
>>> df_xml.dtypes
Track ID                                   int64
Name                                      object
Artist                                    object
Album Artist                              object
Composer                                  object
Album                                     object
Genre                                   category
Kind                                      object
Size                                       int64
Total Time                                 int64
Disc Number                              float64
Disc Count                               float64
Track Number                             float64
Track Count                              float64
Year                                     float64
Date Modified            datetime64[ns, tzutc()]
Date Added               datetime64[ns, tzutc()]
Bit Rate                                   int64
Sample Rate                              float64
Equalizer                                 object
Play Count                               float64
Play Date                                float64
Play Date UTC            datetime64[ns, tzutc()]
Release Date             datetime64[ns, tzutc()]
Normalization                            float64
Sort Album                                object
Sort Artist                               object
Sort Composer                             object
Sort Name                                 object
Persistent ID                             object
Track Type                                object
Purchased                                 object
Location                                  object
File Folder Count                          int64
Library Folder Count                       int64
Volume Adjustment                        float64
Skip Count                               float64
Skip Date                datetime64[ns, tzutc()]
Comments                                  object
Artwork Count                            float64
BPM                                      float64
Rating                                   float64
Album Rating                             float64
Album Rating Computed                     object
Loved                                     object
Sort Album Artist                         object
Matched                                   object
Rating Computed                           object
Explicit                                  object
Compilation                               object
Work                                      object
Part Of Gapless Album                     object
Has Video                                 object
HD                                        object
Video Width                              float64
Video Height                             float64
Music Video                               object
Disliked                                  object
"""

if __name__ == '__main__':
    main(*sys.argv[1:])
