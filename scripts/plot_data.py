import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import StrMethodFormatter

mpl.use('Agg')

# output directory
results = "py_out/"


class plot():
    def __init__(self, x_vals, y_vals, title, x_label, y_label, axes, annotations):
        self.x_vals = np.array(x_vals)
        self.y_vals = np.array(y_vals)
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.axes = axes
        self.annotations = annotations

    def plot_graph(self):
        # create a figure that is 6in x 6in
        fig = plt.figure(figsize=(6, 6))

        # the axis limits and grid lines
        plt.grid(True)
        plt.xlim(0, self.x_vals[-1])

        # label your graph, axes, and ticks on each axis
        plt.xlabel(self.x_label, fontsize=16)
        plt.ylabel(self.y_label, fontsize=16)
        if (self.axes):
            plt.xticks(self.x_vals)
            plt.yticks()
        plt.tick_params(labelsize=15)
        plt.title(self.title, fontsize=18)

        # plot the data values, lines and points
        plt.plot(self.x_vals, self.y_vals,
                 color='r', linewidth=1)  # red line
        plt.plot(self.x_vals, self.y_vals, 'bo')  # blue circle

        if self.annotations:
            # plot y values at points
            for i, j in zip(self.x_vals, self.y_vals):
                plt.annotate(str(j) + 's', xy=(i + 0.5, j), fontsize=13)

        # complete the layout, save figure, and show the figure for you to see
        plt.tight_layout()
        if (not os.path.exists(os.path.join(os.getcwd(), results))):
            os.makedirs(results)
        fig.savefig(os.path.join(results,
                                 self.title.replace(" ", "") + '.png'))
        # close figure
        plt.clf()


if __name__ == '__main__':
    # laptop data
    v0 = plot(x_vals=np.arange(100),
              y_vals=[0.32039, 0.284681, 0.244378, 0.203139, 0.167069, 0.125886, 0.0831575, 0.0608531, 0.0436237, 0.0333069, 0.0295825, 0.0258582, 0.0249153, 0.0220281, 0.0208851, 0.0200936, 0.0192644, 0.0190458, 0.0185635, 0.0196681, 0.0251677, 0.0254161, 0.0243271, 0.0237301, 0.0235336, 0.0263703, 0.0228264, 0.0222415, 0.0220955, 0.0223685, 0.0222477, 0.0221076, 0.0225738, 0.0259142, 0.0233475, 0.0229538, 0.0241603, 0.0236395, 0.0241962, 0.0241525, 0.0194807, 0.024445, 0.0238224, 0.0235761, 0.0241458, 0.0240576, 0.0235744, 0.0238316, 0.0240067, 0.0243334,
                      0.0278312, 0.0268166, 0.0254317, 0.0253872, 0.0263542, 0.0256862, 0.0275135, 0.0205903, 0.0221887, 0.0274581, 0.0286338, 0.029487, 0.028943, 0.0277721, 0.0229352, 0.0224928, 0.0294304, 0.0287781, 0.0303454, 0.0237112, 0.0241543, 0.0292279, 0.0285899, 0.0314892, 0.0303263, 0.0325006, 0.0338406, 0.029314, 0.0305356, 0.0289968, 0.0321234, 0.0304384, 0.0306488, 0.0298879, 0.0305769, 0.0330123, 0.0260314, 0.0302193, 0.0256942, 0.030389, 0.0272925, 0.0385617, 0.0375897, 0.037645, 0.0312929, 0.0394222, 0.0392146, 0.0354236, 0.0381166, 0.0388436],
              title="10000 Boid Tick Timings (200) (B+G) (4t)",
              x_label="Tick Index",
              y_label="Time (s)",
              axes=False,
              annotations=False)

    v1 = plot(x_vals=np.arange(200),
              y_vals=[0.309638, 0.297419, 0.24785, 0.204465, 0.166952, 0.131872, 0.0855755, 0.0556625, 0.0396704, 0.0329352, 0.02899, 0.0276405, 0.0238496, 0.0223145, 0.0213503, 0.0214299, 0.0194283, 0.0195276, 0.0185271, 0.0190296, 0.024734, 0.0252154, 0.0254455, 0.0264557, 0.024831, 0.0236928, 0.0236631, 0.023116, 0.0227593, 0.0238016, 0.0227258, 0.0263227, 0.0189434, 0.0219449, 0.0215353, 0.0213031, 0.0176813, 0.0181791, 0.018103, 0.0194474, 0.0187718, 0.0211241, 0.0231218, 0.0184342, 0.0185862, 0.0243571, 0.0240058, 0.0248757, 0.02705, 0.0201585, 0.0193422, 0.0205662, 0.0205393, 0.0213292, 0.0199122, 0.0249188, 0.0259485, 0.0256721, 0.026351, 0.0299846, 0.0286865, 0.0272408, 0.0262596, 0.0260886, 0.0262864, 0.0221827, 0.0229263, 0.0255616, 0.0254741, 0.024196, 0.0254679, 0.0289196, 0.0292585, 0.0255566, 0.0271907, 0.0281285, 0.0260646, 0.0262583, 0.031672, 0.0311471, 0.0313122, 0.0323641, 0.0342059, 0.036971, 0.034318, 0.036546, 0.0357458, 0.0361966, 0.0320434, 0.0375714, 0.0292409, 0.030777, 0.0370343, 0.0359762, 0.0295681, 0.0369077, 0.0367747, 0.0346043, 0.0294764, 0.0283154, 0.0280333,
                      0.029343, 0.0296657, 0.0350075, 0.0355444, 0.0355976, 0.0411955, 0.0370686, 0.0385786, 0.0423476, 0.0421742, 0.0423352, 0.0436619, 0.0388578, 0.0387959, 0.0355974, 0.0358925, 0.0422798, 0.041322, 0.0391806, 0.0414135, 0.0405306, 0.0405978, 0.0398667, 0.0387701, 0.040918, 0.0390582, 0.0329732, 0.0331804, 0.0384389, 0.038398, 0.0379285, 0.0418774, 0.0436125, 0.0386673, 0.0320491, 0.032461, 0.0317346, 0.0334581, 0.0335584, 0.0347443, 0.0346953, 0.0318087, 0.0358381, 0.0319054, 0.0490171, 0.0325635, 0.0323043, 0.0371377, 0.0338548, 0.0319089, 0.0324508, 0.0344421, 0.0338711, 0.0350672, 0.0329204, 0.0328401, 0.0352845, 0.0355953, 0.0476856, 0.0350174, 0.0359796, 0.0355255, 0.0377325, 0.0372702, 0.0364425, 0.0370377, 0.0365652, 0.0380569, 0.0430972, 0.0381784, 0.0378911, 0.0387129, 0.0374958, 0.0377034, 0.0425295, 0.0379934, 0.0383933, 0.0374847, 0.037364, 0.0397555, 0.0383642, 0.0389548, 0.0390435, 0.0411743, 0.0376926, 0.0382288, 0.0337312, 0.0312362, 0.0339533, 0.0346032, 0.0386472, 0.0354623, 0.0356151, 0.0356703, 0.0358553, 0.0406787, 0.0370033, 0.0358097, 0.0365389],
              title="10000 Boid Tick Timings (200) (B+G) (4t)",
              x_label="Tick Index",
              y_label="Time (s)",
              axes=False,
              annotations=False)

    v2 = plot(x_vals=np.arange(200),
              y_vals=[1.18823, 0.970234, 0.799262, 0.640791, 0.474267, 0.327078, 0.209048, 0.115961, 0.0713784, 0.0688708, 0.0480841, 0.0440523, 0.0396215, 0.0393664, 0.0394624, 0.0433173, 0.0372495, 0.0367794, 0.0370484, 0.0384498, 0.0393894, 0.0387405, 0.0391497, 0.0403663, 0.0424084, 0.0447863, 0.0445698, 0.0466581, 0.046154, 0.0494693, 0.05535, 0.055281, 0.0568934, 0.060172, 0.0600724, 0.0603239, 0.0640216, 0.0649332, 0.0699764, 0.0695074, 0.072432, 0.0771874, 0.0749031, 0.07992, 0.0799825, 0.0960726, 0.0877987, 0.089719, 0.0917987, 0.0919737, 0.0918484, 0.0961222, 0.0979183, 0.105865, 0.11105, 0.11274, 0.110565, 0.110258, 0.123298, 0.131442, 0.11767, 0.120204, 0.121285, 0.124154, 0.129456, 0.126329, 0.12698, 0.12951, 0.135945, 0.136034, 0.140786, 0.135874, 0.135703, 0.153292, 0.155219, 0.171551, 0.176237, 0.164088, 0.171691, 0.168332, 0.161839, 0.182919, 0.166185, 0.16835, 0.171983, 0.176606, 0.166623, 0.180248, 0.16958, 0.17322, 0.177248, 0.185624, 0.195516, 0.188093, 0.188176, 0.205619, 0.191372, 0.191983,
                      0.196221, 0.196896, 0.199286, 0.188584, 0.184967, 0.18784, 0.185319, 0.182478, 0.186836, 0.187583, 0.18316, 0.192617, 0.185953, 0.194511, 0.201657, 0.194892, 0.194399, 0.19227, 0.195751, 0.22375, 0.21248, 0.231556, 0.220357, 0.233348, 0.231095, 0.233615, 0.23733, 0.233427, 0.242656, 0.234005, 0.240927, 0.237862, 0.235879, 0.263311, 0.25223, 0.261111, 0.258863, 0.266469, 0.240701, 0.23931, 0.261477, 0.265926, 0.269518, 0.258214, 0.262291, 0.268237, 0.270601, 0.270876, 0.26939, 0.301478, 0.269997, 0.270617, 0.274409, 0.275945, 0.275636, 0.282732, 0.282148, 0.28882, 0.281996, 0.294263, 0.283832, 0.285848, 0.292481, 0.295231, 0.293184, 0.327127, 0.29431, 0.306454, 0.318433, 0.32252, 0.326276, 0.322881, 0.309325, 0.317282, 0.316372, 0.312361, 0.314423, 0.326817, 0.324261, 0.316406, 0.32023, 0.32786, 0.323252, 0.321144, 0.317609, 0.328565, 0.325659, 0.3258, 0.323118, 0.343301, 0.340925, 0.341306, 0.341756, 0.338436, 0.358445, 0.36213, 0.359663, 0.363931, 0.359883, 0.36322, 0.376649, 0.379606, ],
              title="20000 Boid Tick Timings (200) (F+L) (4t)",
              x_label="Tick Index",
              y_label="Time (s)",
              axes=False,
              annotations=False)
    flock_sizes = [1, 1.07124, 1.25078, 1.51378, 1.90367, 2.49688, 3.28947, 4.28266, 5.48847, 6.70691, 7.89266, 9.03342, 10.2987, 11.5741, 12.6422, 13.587, 14.556, 15.5521, 16.129, 16.6945, 17.6056, 18.1488, 18.8324, 19.6078, 20.0803, 21.0084, 21.5983, 22.2222, 22.6244, 22.8311, 23.5849, 24.6914, 25, 25.3165, 25.974, 26.5957, 27.248, 27.5482, 27.7778, 28.5714, 28.9855, 29.1545, 29.4985, 29.9401, 30.2115, 30.9598, 31.1526, 31.6456, 31.746, 31.9489,
                   32.4675, 33.1126, 33.1126, 33.3333, 33.8983, 34.2466, 34.4828, 35.2113, 35.461, 36.2319, 36.4964, 36.9004, 37.594, 38.3142, 38.61, 39.0625, 39.6825, 40.1606, 40.1606, 40.1606, 40.9836, 41.1523, 41.3223, 42.1941, 42.735, 42.9185, 43.1034, 43.4783, 43.8596, 44.0529, 44.2478, 44.2478, 44.2478, 44.4444, 44.6429, 44.6429, 44.6429, 44.6429, 45.6621, 46.0829, 46.2963, 46.5116, 46.729, 46.9484, 46.9484, 47.3934, 48.0769, 48.3092, 48.5437, 48.7805]
    v3 = plot(x_vals=np.arange(len(flock_sizes)),
              y_vals=flock_sizes,
              title="Average Flock Sizes (10000) (F+L)",
              x_label="Tick Index",
              y_label="Avg Size",
              axes=False,
              annotations=False)
    flock_sizes = [1, 1.07135, 1.25109, 1.51309, 1.89753, 2.43962, 3.03582, 3.64299, 4.26621, 4.83092, 5.32481, 5.73394, 6.13874, 6.41849, 6.61813, 6.82128, 7.01262, 7.20461, 7.33138, 7.44602, 7.5815, 7.69231, 7.80031, 7.94281, 8.03213, 8.12348, 8.22368, 8.29876, 8.38926, 8.4246, 8.45309, 8.53242, 8.59107, 8.69565, 8.73362, 8.81834, 8.88889, 8.96057, 9.00901, 9.04159, 9.07441, 9.10747, 9.15751, 9.19963, 9.25926, 9.31966, 9.3985, 9.4162, 9.4697,
                   9.47867, 9.53289, 9.54198, 9.54198, 9.57854, 9.57854, 9.59693, 9.62464, 9.6432, 9.66184, 9.68992, 9.72763, 9.83284, 9.87167, 9.8912, 9.92063, 9.93049, 9.95025, 9.99001, 10.0402, 10.0705, 10.101, 10.1112, 10.1317, 10.1729, 10.2249, 10.2459, 10.2669, 10.2987, 10.3093, 10.3413, 10.352, 10.3842, 10.4058, 10.4167, 10.4275, 10.4493, 10.4932, 10.5263, 10.5485, 10.582, 10.5932, 10.5932, 10.6045, 10.627, 10.627, 10.627, 10.661, 10.6838, 10.7066, 10.7181]
    v4 = plot(x_vals=np.arange(len(flock_sizes)),
              y_vals=flock_sizes,
              title="Average Flock Sizes (10000) (max10)",
              x_label="Tick Index",
              y_label="Avg Size",
              axes=False,
              annotations=False)
    tick_times_500 = [0.3143, 0.289787, 0.250615, 0.211191, 0.167519, 0.127458, 0.0934449, 0.0504248, 0.0380586, 0.0291388, 0.025835, 0.0267625, 0.0214131, 0.0190545, 0.0176724, 0.0171778, 0.0167751, 0.0162963, 0.0162454, 0.0152291, 0.0155851, 0.0148536, 0.0149407, 0.0150019, 0.0156594, 0.0155, 0.0155489, 0.0142406, 0.0143838, 0.0156589, 0.0146621, 0.0168396, 0.0150899, 0.01556, 0.0151022, 0.0153871, 0.0155112, 0.0162683, 0.0175747, 0.0163094, 0.0180817, 0.0213695, 0.0190622, 0.0183008, 0.0202697, 0.0184813, 0.0184263, 0.0226882, 0.0226993, 0.0234034, 0.0253812, 0.0231184, 0.0248581, 0.0238912, 0.023397, 0.0203093, 0.0203405, 0.0206789, 0.0208235, 0.0251343, 0.0230794, 0.0234845, 0.0226218, 0.0232684, 0.0229587, 0.0227846, 0.023174, 0.0235482, 0.0238115, 0.0243127, 0.0241967, 0.0242992, 0.0247071, 0.0251939, 0.0257317, 0.0260597, 0.0259823, 0.0256127, 0.0255549, 0.0258456, 0.0263596, 0.0269051, 0.0262961, 0.0276626, 0.0280289, 0.0276868, 0.0279708, 0.0290347, 0.0281834, 0.0278938, 0.0362832, 0.0325334, 0.0289872, 0.0331229, 0.0344835, 0.0343975, 0.0350878, 0.0344889, 0.0357934,
                      0.0340361, 0.0342282, 0.0340604, 0.035275, 0.0336379, 0.0326236, 0.0326808, 0.0323914, 0.0317589, 0.0313595, 0.0344683, 0.0316188, 0.0315, 0.0326981, 0.0331393, 0.0350193, 0.0337739, 0.0331184, 0.0327443, 0.0325695, 0.0323071, 0.0341761, 0.0332436, 0.0339746, 0.034967, 0.034705, 0.0346617, 0.0357719, 0.0352798, 0.0379754, 0.0341311, 0.0354986, 0.0351528, 0.0337368, 0.0340099, 0.0343285, 0.034849, 0.0348344, 0.0350797, 0.0380461, 0.0385257, 0.0416819, 0.0378423, 0.0416719, 0.0385793, 0.0339363, 0.0360028, 0.0329547, 0.034379, 0.0325566, 0.0346951, 0.0333053, 0.0326733, 0.0325603, 0.0369289, 0.0341649, 0.0339906, 0.0346633, 0.0347371, 0.0348952, 0.0404189, 0.0340607, 0.0397248, 0.040683, 0.0340547, 0.0352987, 0.033777, 0.037061, 0.0350964, 0.0370236, 0.0471619, 0.0445698, 0.050292, 0.0353585, 0.0362866, 0.037523, 0.0424132, 0.0415406, 0.0418813, 0.0415528, 0.0430218, 0.0453528, 0.0446125, 0.0440641, 0.0447466, 0.0453857, 0.0447785, 0.0440562, 0.0448306, 0.043792, 0.0447603, 0.0474494, 0.0439854, 0.042404, 0.0422764, 0.043888, 0.0418951, 0.0427049, 0.0429404, 0.04522, 0.0445766, ]
    tick_times_10 = [0.311546, 0.294165, 0.254917, 0.20818, 0.170164, 0.134368, 0.0922747, 0.0722134, 0.0496276, 0.0423571, 0.0385168, 0.0341154, 0.0344083, 0.0312346, 0.0307181, 0.0296848, 0.0303287, 0.0282369, 0.031884, 0.0294356, 0.0295374, 0.0283444, 0.0286956, 0.0275059, 0.0274803, 0.0260658, 0.0260886, 0.0266507, 0.0274684, 0.0255973, 0.0277534, 0.0254144, 0.0251216, 0.024923, 0.0261106, 0.0271035, 0.0254515, 0.0261717, 0.02679, 0.0255567, 0.0251128, 0.0260514, 0.0260425, 0.0249997, 0.0273409, 0.0258036, 0.0261711, 0.025677, 0.0253863, 0.0249166, 0.0252746, 0.0251154, 0.0296693, 0.0276307, 0.0275131, 0.0257078, 0.0256036, 0.0259231, 0.0279854, 0.0286541, 0.0276629, 0.0277341, 0.0267242, 0.0257362, 0.0262811, 0.0289969, 0.0259995, 0.0260145, 0.025706, 0.025834, 0.0247717, 0.0286662, 0.0258405, 0.0256797, 0.0257723, 0.0278695, 0.0276861, 0.0322958, 0.0276716, 0.0275587, 0.0269655, 0.0281915, 0.0282216, 0.0319617, 0.0260101, 0.0250578, 0.0261989, 0.0256765, 0.0261291, 0.0259734, 0.0269669, 0.0280467, 0.0262638, 0.0272637, 0.0277816, 0.0282294, 0.025397, 0.0251053, 0.0272138, 0.0279432,
                     0.0275969, 0.0263756, 0.0270737, 0.025263, 0.0250921, 0.0258136, 0.0282449, 0.0281108, 0.0289936, 0.0297298, 0.0285412, 0.0290689, 0.0334107, 0.0298271, 0.0283309, 0.028754, 0.0257767, 0.0258543, 0.0302299, 0.0265959, 0.0264199, 0.0264006, 0.0272474, 0.0260281, 0.0300787, 0.0266924, 0.0312802, 0.0277278, 0.0266514, 0.0292019, 0.0263728, 0.0278578, 0.0304104, 0.0274913, 0.0260628, 0.0267628, 0.0268997, 0.0285086, 0.0275599, 0.0327395, 0.0278592, 0.0341223, 0.0269636, 0.0265688, 0.0331946, 0.0300884, 0.0310911, 0.0305834, 0.0298783, 0.0267899, 0.0264298, 0.0271829, 0.027626, 0.0271549, 0.0266385, 0.0270639, 0.0276302, 0.0286834, 0.0315162, 0.0303906, 0.0316883, 0.0269302, 0.0285261, 0.0266103, 0.0344141, 0.0261564, 0.0319365, 0.030484, 0.0300613, 0.0300127, 0.0310148, 0.0275294, 0.0285908, 0.0279501, 0.0270159, 0.0283178, 0.027078, 0.027177, 0.0294974, 0.0281498, 0.0285171, 0.0322337, 0.0306215, 0.0293852, 0.0270178, 0.0269043, 0.0270028, 0.0370321, 0.0291269, 0.0326954, 0.0286388, 0.0297175, 0.0282984, 0.0354686, 0.0281145, 0.0276024, 0.0274492, 0.0275824, 0.0324661, 0.0279354, ]
    v5 = plot(x_vals=np.arange(len(tick_times_10)),
              y_vals=tick_times_10,
              title="Tick Times (10000) (max10) (4t)",
              x_label="Tick Index",
              y_label="Time (s)",
              axes=False,
              annotations=False)
    v6 = plot(x_vals=np.arange(len(tick_times_500)),
              y_vals=tick_times_500,
              title="Tick Times (10000) (max500) (4t)",
              x_label="Tick Index",
              y_label="Time (s)",
              axes=False,
              annotations=False)
    time_varying_max = [2.073, 1.867, 1.7536, 1.9575, 1.675, 1.6914,
                        1.7785, 1.9206, 1.9201, 1.882, 2.167]
    time_varying_x = [10, 20, 30, 40, 50, 60, 70,
                      80, 90, 100, 150]
    v7 = plot(x_vals=time_varying_x,
              y_vals=time_varying_max,
              title="1000 Varying Flock Max",
              x_label="Flock Max",
              y_label="Time (s)",
              axes=False,
              annotations=False)

    procs = [1, 2, 4, 8, 12, 16, 24, 32]

    misses_F_L = [23.492, 23.59, 23.78, 23.995, 24.211, 20.207, 18.212, 18.862]
    faults_F_L = [2495, 2714, 2944, 3287, 3551, 3623, 3873, 4389]

    misses_F_G = [17.015, 17.445, 17.650,
                  18.463, 18.639, 16.848, 16.279, 16.350]
    faults_F_G = [2879, 3558, 4746, 6030, 4473, 3608, 3752, 4302]

    # misses_B_G = [31.564, 31.952, 32.286, 32.337, 31.055, 30.096, ]
    # faults_B_G = [2876, 3740, ]

    # misses_B_L = []
    # faults_B_L = []

    v7 = plot(x_vals=procs,
              y_vals=misses_F_L,
              title="miss-rate of (F+L)",
              x_label="Procs",
              y_label="Miss Rate %",
              axes=False,
              annotations=False)

    v8 = plot(x_vals=procs,
              y_vals=misses_F_G,
              title="miss-rate of (F+G)",
              x_label="Procs",
              y_label="Miss Rate %",
              axes=False,
              annotations=False)

    v9 = plot(x_vals=procs,
              y_vals=faults_F_L,
              title="faults of (F+L)",
              x_label="Procs",
              y_label="Fault Count",
              axes=False,
              annotations=False)

    v10 = plot(x_vals=procs,
               y_vals=faults_F_G,
               title="faults of (F+G)",
               x_label="Procs",
               y_label="Fault Count",
               axes=False,
               annotations=False)

    views = [v7, v8, v9, v10]
    for v in views:
        v.plot_graph()
