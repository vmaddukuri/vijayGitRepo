import xml.etree.ElementTree as et
from psdemoxml1 import get_namespace_from_xml_file

ns = get_namespace_from_xml_file('450_FX.xml')[1]


def get_elements_by_name(tag_name):
    doc = et.parse('450_FX.xml')
    for item in doc.getiterator(tag_name):
        print(item)

    for header_tag in doc.getroot()[0]:
        print(header_tag.tag.replace(ns, ''))
        for child in header_tag:
            print(child.tag.replace(ns, ''), ':', child.text )
        print()


if __name__ == '__main__':
    get_elements_by_name('header')


if __name__ == '__msain__':
    ns = get_namespace_from_xml_file('450_FX.xml')[1]
    print(ns)

    doc = et.parse('450_FX.xml')
    root_tag = doc.getroot()

    for child in root_tag:
        print('tag :', child.tag.replace(ns, ''))
        print('text :', child.text)