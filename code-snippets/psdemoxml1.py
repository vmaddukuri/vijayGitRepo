import xml.etree.ElementTree as et


def get_namespace_from_xml_file(xml_file):
    for event, ns in et.iterparse('450_FX.xml', ["start", "start-ns"]):
        if event == 'start-ns' and not ns[0]:
            return ns[1], "{"+ns[-1]+"}"



if __name__ == '__main__':
    ns = get_namespace_from_xml_file('450_FX.xml')
    print(ns)
    exit(1)

    doc = et.parse('450_FX.xml')
    root_tag = doc.getroot()
    print("tag name :", root_tag.tag.replace(ns, ''))
    print("root tag attrib : ", root_tag.attrib)
    print(root_tag.getchildren())
    print(dir(root_tag))

#for item in doc.getiterator():
#    print(item)