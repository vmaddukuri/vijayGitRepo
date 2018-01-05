from json import load
from xml.etree.ElementTree import ElementTree, Element, SubElement
from pprint import pprint as pp

inner_most_tag_name = dict(files='file', dirs='directory')


class JSON2XML:
    def __init__(self, json_file, xml_file):
        self.json_file = json_file
        self.xml_file = xml_file
        self.write_xml()

    def read_content_from_json(self):
        return load(open(self.json_file))

    def add_children_tags_directory_tag(self, dir_tag, dir_content):
        for file_type, list_of_items in dir_content.items():
            child_tag_dir_tag = SubElement(dir_tag, file_type)  # add child to directory tag

            for item_name in list_of_items:
                inner_most = SubElement(child_tag_dir_tag, inner_most_tag_name[file_type])
                inner_most.text = item_name   # set text to the file/directory tag

    def write_xml(self):
        json_content = self.read_content_from_json()
        root_tag = Element('file-system')  # root element

        for dir_name, directory_content in json_content.items():
            directory_tag = SubElement(root_tag, 'directory')  # child tag to root tag
            directory_tag.set('name', dir_name)  # attributes to the tag
            self.add_children_tags_directory_tag(directory_tag, directory_content)

        ElementTree(root_tag).write(self.xml_file)  # writing into xml file


JSON2XML('tmp.json', 'tmp.xml')
