from xml.dom.minidom import parse as parseXMLFile
from xml.dom.minidom import Document, Element
import os
import csv

with open("app_permissions.csv", "w") as f:
    writer = csv.writer(f)

    for file in os.listdir("manifests"):
        manifest = parseXMLFile(os.path.join("manifests", file))
        permissions = manifest.getElementsByTagName("uses-permission")
        rowOut = [os.path.splitext(os.path.splitext(os.path.splitext(file)[0])[0])[0]]
        permission = None
        for permission in permissions:
            permission_name = permission.getAttribute("android:name")
            rowOut.append(permission_name)

        writer.writerow(rowOut)
