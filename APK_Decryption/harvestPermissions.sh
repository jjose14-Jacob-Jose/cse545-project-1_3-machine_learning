#!/usr/bin/env bash
mkdir manifests
cd selectedAPKs
for FILE in *.apk; do
	apktool d ${FILE} -rsf --force-manifest -o current
	cp current/AndroidManifest.xml ../manifests/${FILE}.AndroidManifest.xml
done
rm -r current
