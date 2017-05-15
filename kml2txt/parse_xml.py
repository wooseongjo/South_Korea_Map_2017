import xml.etree.ElementTree as ET 
import sys

doc = ET.parse(sys.argv[1])
root = doc.getroot()

placelist = root.findall("./Document/Folder/Placemark")

for elem in placelist:

    tmp = []
    for subelem in elem.iter():
        if subelem.tag == "SimpleData":
            tmp.append(subelem.text)
            
    prefix_fn = "map_" + tmp[0]
    postfix_fn = "_".join(tmp[1:]) + ".txt" 
    print postfix_fn
    
    cnt = 0
    for subelem in elem.iter():
        if subelem.tag == "coordinates":
            line = subelem.text

            modline = line.replace(" ", "\n")
            modline = modline.replace(",", " ")

            fn = prefix_fn + "_" + str(cnt) + "_" + postfix_fn 
            f = open(fn, 'w')

            f.write(modline)
            cnt += 1
