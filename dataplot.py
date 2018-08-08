import glob
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
filelist = glob.glob("./*.txt")
for i, file in enumerate(filelist):
    print(str(i)+": " + str(file))
    plt.close("all")
    value1, value2 = np.loadtxt(file, comments="!", unpack=True)

    plt.plot(range(len(value1)),value1, label='SP', linestyle="dashed")
    plt.plot(range(len(value2)),value2, label="measured")
    plt.ylim([0,220])
    plt.xlabel("time")
    plt.ylabel("temperature")
    plt.legend()
    plt.savefig("zu"+ str(i) + ".eps")
