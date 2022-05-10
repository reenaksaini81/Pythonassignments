import xml.etree.ElementTree as ET
x=input('Enter Depart Date : ')
y=input('Enter Return Date : ')
tree =ET.parse("test_payload1.xml")
root = tree.getroot()
for child in root.iter():
	if child.tag=='DEPART':
		child.text=x
	if child.tag=='RETURN':
		child.text=y
tree.write("new_test_payload1.xml")