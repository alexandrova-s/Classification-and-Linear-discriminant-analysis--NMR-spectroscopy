# import glob

# path = '\\LCModel_WHO\\who_ii_30ms\\'

# files = [f for f in glob.glob(path + "**.rda", recursive=True)]

# for f in files:
#     print(f)


# import os

# for root, dirs, files in os.walk("."):
#     for filename in files:
#         if ".rda" in filename:
#             filename = filename.replace(" ", "_")
#             print(filename)

import os
pathiter = (os.path.join(root, filename)
    for root, _, filenames in os.walk(".\Badania\whoi")
    for filename in filenames
)
for path in pathiter:
    newname =  path.replace(' ', '_')
    if newname != path:
        os.rename(path,newname)