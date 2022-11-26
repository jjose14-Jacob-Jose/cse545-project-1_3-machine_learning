#!/usr/bin/env bash
mkdir XML_Files_of_APKs
cd APKs_to_be_extracted
for FILE in *.apk; do
	apktool d ${FILE} -rsf --force-manifest -o current
	cp current/AndroidManifest.xml ../XML_Files_of_APKs/${FILE}.AndroidManifest.xml
done
rm -r current
