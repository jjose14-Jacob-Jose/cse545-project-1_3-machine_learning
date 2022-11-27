#!/usr/bin/env bash
mkdir Extracted_XML_Files_of_APKs
cd ZIP_Files_to_be_extracted
for FILE in *.*; do
	unzip ${FILE} -d current
	echo ${FILE}
  cp current/AndroidManifest.xml ../Extracted_XML_Files_of_APKs/${FILE}.AndroidManifest.xml
	rm -r current
#	unzip d ${FILE} -rsf --force-manifest -o current
#	cp current/AndroidManifest.xml ../Extracted_XML_Files_of_APKs/${FILE}.AndroidManifest.xml
done
#rm -r current
