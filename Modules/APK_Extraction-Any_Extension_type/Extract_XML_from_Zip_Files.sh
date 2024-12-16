#!/usr/bin/env bash
mkdir XMLs_that_are_extracted
cd To_Be_Extracted
for FILE in *.*; do
	apktool d ${FILE} -rsf --force-manifest -o current
	cp current/AndroidManifest.xml ../XMLs_that_are_extracted/${FILE}.AndroidManifest.xml
done
rm -r current
