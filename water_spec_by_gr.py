import suspect
import numpy as np
from matplotlib import pyplot as plt
import os
#%matplotlib inline

folders = ["whoi", "whoii", "whoiii", "whoiv"]

for folder in folders:
    directory = os.fsencode(".\LCMODEL\LCMODEL\\" + folder)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".rda"): 
            if 'kontrola' not in filename:
                print(filename[:-4])
                data = suspect.io.load_rda(".\LCMODEL\LCMEDEL\\" + folder + "\\" + filename)
                print(data)
                plt.figure()
                if not '3d' or '3D' in filename:
                    plt.plot(data.frequency_axis_ppm(), data.spectrum().real)
                    plt.xlim([10, -1])
                    plt.title(filename)
                    plt.xlabel("p.p.m.")
                    plt.ylabel("Amplituda (a.u.)")
                    #plt.savefig(".\LCModel_WHO\water_spectrums\\" + filename[:-4] + ".jpg")
plt.show()