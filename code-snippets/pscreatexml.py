from xml.etree.ElementTree import Element, SubElement, ElementTree

root_tag = Element('directories')  # root tag
dir_tag = SubElement(root_tag, 'directory')  # child tag
# dir_tag.set('name', '/tmp')  # setting an  attribute
dir_tag.attrib = {'name': '/tmp'}
file_tag = SubElement(dir_tag, 'file')
file_tag.text = 'Eureka Forbes.pdf'  # text node
file_tag.attrib = dict(size="1243", mtime='Sun Dec 11 22:29:41 2016')

ElementTree(root_tag).write('tmp.xml', xml_declaration=True)  # doc object