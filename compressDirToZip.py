import os
import zipfile
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
zipf = zipfile.ZipFile('Zipped_file.txt', 'w', zipfile.ZIP_DEFLATED)
zipdir('../', zipf)
zipf.close()
print("done")
