import xml.etree.ElementTree as ET
import collections
tree=ET.parse('config.xml')

root=tree.getroot()
"""
#print description
print root[1].text 
"""

"""
#users=tree.findall("permission")
#for user in tree.getiterator('permission'):
	print user.text
"""
"""
for element in root.getchildren():
#for element in root.getiterator():
	print element.tag
#c=root[4]
"""
def child(node):
	for num,child in enumerate(node.getiterator()):
		print num,child.tag,child.text
#		for grandchild in child.getchildren():
#			 child(grandchild)
if __name__=="__main__":
	child(root)
