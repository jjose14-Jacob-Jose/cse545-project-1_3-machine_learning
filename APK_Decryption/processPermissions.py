from xml.dom.minidom import parse as parseXMLFile
from xml.dom.minidom import Document, Element
import os
import csv

with open("app_permissions.csv", "w") as f:
    writer = csv.writer(f)

    directory_name_Andriod_manifests = "manifests-malware"

    for file in os.listdir(directory_name_Andriod_manifests):
        manifest = parseXMLFile(os.path.join(directory_name_Andriod_manifests, file))
        permissions = manifest.getElementsByTagName("uses-permission")
        rowOut = [os.path.splitext(os.path.splitext(os.path.splitext(file)[0])[0])[0]]
        permission = None
        for permission in permissions:
            permission_name = permission.getAttribute("android:name")
            rowOut.append(permission_name)

        writer.writerow(rowOut)
