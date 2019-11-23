import suspect
import numpy as np
from matplotlib import pyplot as plt
import os
#%matplotlib inline

folders = ["whoi", "whoii", "whoiii", "whoiv"]

for folder in folders:
    directory = os.fsencode(".\LCMODEL\\" + folder)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".rda"): 
            print(filename[:-4])
            data = suspect.io.load_rda(".\LCMODEL\\" + folder + "\\" + filename)
            print(data)
            plt.figure()
            if not '3d' or '3D' in filename:
                plt.plot(data.frequency_axis_ppm(), data.spectrum().real)
                plt.xlim([10, -1])
                plt.title(filename)
                plt.xlabel("p.p.m.")
                plt.ylabel("Amplituda (a.u.)")
                plt.savefig(".\LCModel_WHO\water_spectrums\\" + filename[:-4] + ".jpg")



#plt.show()

# for root, dirs, files in os.walk("."):
#     for filename in files:
#         if filename.endswith(".rda") in filename:
#             print(filename)

                # data = suspect.io.load_rda(".\LCModel_WHO\who_iv_135ms\\filename")
                # print(data)

# '''
#             if not ".rda_out" in filename:
# # plt.plot(data.time_axis(), data.real)
# # plt.show()

# plt.plot(data.frequency_axis_ppm(), data.spectrum().real)
# # reverse the limits on the x-axis so that ppm runs from right to left
# plt.xlim([10, -1])
# plt.show()


# # import scipy.signal
# # # scipy.signal produces symmetric windows so only take the second half
# # window = scipy.signal.tukey(data.np * 2)[data.np:]
# # plt.plot(data.time_axis(), window)
# # plt.show()

# # windowed_data = window * data
# # plt.plot(data.time_axis(), data.real)
# # plt.show()

# # plt.plot(windowed_data.time_axis(), windowed_data.real)
# # plt.show()
# '''