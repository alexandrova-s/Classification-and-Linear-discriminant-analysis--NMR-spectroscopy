import suspect
import numpy as np
from matplotlib import pyplot as plt
import os
#%matplotlib inline

folders = ["wyniki_1", "wyniki_2", "wyniki_3", "wyniki_4"]

fout_i_30=open(".\LCMODEL\wyniki\\result_i_30.csv","a")
fout_i_135=open(".\LCMODEL\wyniki\\result_i_135.csv","a")
fout_i_30kon=open(".\LCMODEL\wyniki\\result_i_30kon.csv","a")
fout_i_135kon=open(".\LCMODEL\wyniki\\result_i_135kon.csv","a")
fout_ii_30=open(".\LCMODEL\wyniki\\result_ii_30.csv","a")
fout_ii_135=open(".\LCMODEL\wyniki\\result_ii_135.csv","a")
fout_ii_30kon=open(".\LCMODEL\wyniki\\result_ii_30kon.csv","a")
fout_ii_135kon=open(".\LCMODEL\wyniki\\result_ii_135kon.csv","a")
fout_iii_30=open(".\LCMODEL\wyniki\\result_iii_30.csv","a")
fout_iii_135=open(".\LCMODEL\wyniki\\result_iii_135.csv","a")
fout_iii_30kon=open(".\LCMODEL\wyniki\\result_iii_30kon.csv","a")
fout_iii_135kon=open(".\LCMODEL\wyniki\\result_iii_135kon.csv","a")
fout_iv_30=open(".\LCMODEL\wyniki\\result_iv_30.csv","a")
fout_iv_135=open(".\LCMODEL\wyniki\\result_iv_135.csv","a")
fout_iv_30kon=open(".\LCMODEL\wyniki\\result_iv_30kon.csv","a")
fout_iv_135kon=open(".\LCMODEL\wyniki\\result_iv_135kon.csv","a")


for folder in folders:
    if '1' in folder:
        directory = os.fsencode(".\LCMODEL\wyniki\\" + folder)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if '30.' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_i_30.write(line)
            if '135.' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_i_135.write(line)
            if '30kon' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_i_30kon.write(line)          
            if '135kon' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_i_135kon.write(line)   

    if '2' in folder:
        directory = os.fsencode(".\LCMODEL\wyniki\\" + folder)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if '30.' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_ii_30.write(line)
            if '135.' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_ii_135.write(line)
            if '30kon' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_ii_30kon.write(line)     
            if '135kon' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_ii_135kon.write(line)  

    if '3' in folder:
        directory = os.fsencode(".\LCMODEL\wyniki\\" + folder)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if '30.' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_iii_30.write(line)
            if '135.' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_iii_135.write(line)
            if '30kon' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_iii_30kon.write(line) 
            if '135kon' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_iii_135kon.write(line)          

    if '4' in folder:
        directory = os.fsencode(".\LCMODEL\wyniki\\" + folder)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if '30.' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_iv_30.write(line)
            if '135.' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_iv_135.write(line)
            if '30kon' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_iv_30kon.write(line)  
            if '135kon' in filename:
                directory2 = os.fsencode(".\LCMODEL\wyniki\\" + folder + "\\" + filename)

                for file in os.listdir(directory2):
                    filename2 = os.fsdecode(file)
                    if filename2.endswith(".csv"):
                        for line in open(".\LCMODEL\wyniki\\" + folder + "\\" + filename + "\\" + filename2):
                            if 'Row' not in line:
                                fout_iv_135kon.write(line)  



fout_i_30.close()
fout_i_135.close()
fout_i_30kon.close()
fout_i_135kon.close()
fout_ii_30.close()
fout_ii_135.close()
fout_ii_30kon.close()
fout_ii_135kon.close()
fout_iii_30.close()
fout_iii_135.close()
fout_iii_30kon.close()
fout_iii_135kon.close()
fout_iv_30.close()
fout_iv_135.close()
fout_iv_30kon.close()
fout_iv_135kon.close()