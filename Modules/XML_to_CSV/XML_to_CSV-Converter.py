from xml.dom.minidom import parse as parseXMLFile
import xml.etree.ElementTree as ET
import os
import csv

name_directory_XMLs = ["benign", "malware"]
name_csv_permissions_only = "permissions.csv"
name_csv_permissions_and_receiver = "permissions_and_receiver.csv"


def process_permissions_only(directory_name):
    with open(directory_name + "-" +name_csv_permissions_only, "w") as f:
        writer = csv.writer(f)

        for file in os.listdir(directory_name):
            manifest = parseXMLFile(os.path.join(directory_name, file))
            permissions = manifest.getElementsByTagName("uses-permission")
            rowOut = [os.path.splitext(os.path.splitext(os.path.splitext(file)[0])[0])[0]]
            permission = None
            for permission in permissions:
                permission_name = permission.getAttribute("android:name")
                rowOut.append(permission_name)

            writer.writerow(rowOut)

def process_permissions_and_receiver_information(directory_name):
    with open(directory_name + "-" +name_csv_permissions_and_receiver, "w") as f:
        writer = csv.writer(f)

        for file in os.listdir(directory_name):
            manifest = parseXMLFile(os.path.join(directory_name, file))
            permissions = manifest.getElementsByTagName("uses-permission")
            rowOut = [os.path.splitext(os.path.splitext(os.path.splitext(file)[0])[0])[0]]
            permission = None
            for permission in permissions:
                permission_name = permission.getAttribute("android:name")
                rowOut.append(permission_name)



            xml_tree = ET.parse(directory_name + "/" + file)
            xml_root = xml_tree.getroot()
            for receiver_element in manifest.getElementsByTagName("receiver"):
                for intent_filter in receiver_element.getElementsByTagName("intent-filter"):
                    for action in intent_filter.getElementsByTagName("action"):
                        rowOut.append(action.getAttribute("android:name"))

            writer.writerow(rowOut)

def generated_csv_both():
    for name_directory_XML in name_directory_XMLs:
        process_permissions_only(name_directory_XML)
        process_permissions_and_receiver_information(name_directory_XML)

def main():
    generated_csv_both()

if __name__ == "__main__":
    main()