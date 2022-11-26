from xml.dom.minidom import parse as parseXMLFile
from xml.dom.minidom import Document, Element
import xml.etree.ElementTree as ET
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

        xml_tree = ET.parse(directory_name_Andriod_manifests + "/" + file)
        xml_root = xml_tree.getroot()

        for receiver_element in manifest.getElementsByTagName("receiver"):
            for intent_filter in receiver_element.getElementsByTagName("intent-filter"):
                for action in intent_filter.getElementsByTagName("action"):
                    print(action.getAttribute("android:name"))

        # for xml_root_children in xml_root:
        #     if xml_root_children.tag == "application":
        #         for xml_tag_application in xml_root_children.iter():
        #             if xml_tag_application.tag == "receiver":
        #                 for xml_tag_intent_filter in xml_tag_application.getchildren():
        #                     print(xml_tag_application.tag)
        #
        # print("hello")

