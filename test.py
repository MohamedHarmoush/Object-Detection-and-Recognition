import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

df = pd.read_excel('trainingData.xlsx', sheet_name='Sheet1')

PCA = df.as_matrix()
PCA = np.array(PCA).tolist()
print(PCA)

weights = [[0.2519707112449845, 0.3188176484739583, 0.4413261238210132, 0.3040422955872771],
           [0.00858881026784663, 0.862039935394091, 0.8026281485980282, 0.13790201520236245],
           [0.29994263525642456, 0.00779574157209866, 0.3888275513942565, 0.9354064925977094],
           [0.6253944629688799, 0.6744997487381, 0.7708941613915742, 0.46540656096555516],
           [0.9289226348059674, 0.4943293352066468, 1.1331289285947252, 0.9889120637113104]]

centroids = [[15.816393076067397, 12.967974336266897, 2.997635573500833, -9.105605076706087, -4.3882078317404165,
              4.20685441135276, 0.12766664245952916, -0.8782055120553584, -1.7395445801054703, -2.925610714475469,
              -0.8788564732869001, -0.4926472053691856, -4.268336494147606, 3.0296704306231557, -0.5445063399002498,
              -1.2058646582663923, -0.852121453464388, -0.6909386291052843, -1.8445578027609035, -0.9110366952550683,
              -0.518427170211955, 0.2096739680177879, 0.14907800768317753, -0.03628096692890459],
             [30.927843602305288, -30.764362386106786, -0.19197723214502696, 7.81906491781681, -0.15171685056899387,
              2.866381143770637, -3.7674352397574946, -0.15766425621605648, 3.647750946580976, 8.948092819277496,
              2.4323826701947784, 3.610615423720739, 1.7870601185187096, -0.11971999371987074, -1.7699274289934468,
              1.2399629368063636, -0.9589909113324216, 1.6030154979651605, -0.36201921314392066, -0.23860552467718973,
              2.520645159977222, -0.5022923737137814, -1.3582436467731034, -1.2739584022327402],
             [-20.99954548785907, -1.7615287930530006, -13.667628182889494, 9.316806446027227, -0.906665858919515,
              2.4462505023276795, -3.853269650134164, -3.8286977800203092, 0.6732177437746065, -1.9469295785351797,
              -1.3552603397505927, -1.5294372411786232, -0.7334201558132195, 2.6577453180527217, -0.268822867590001,
              0.7543537809266546, -0.26444092798788016, 1.7215744620928024, 0.88282090001742, 0.17932729244355552,
              -0.15589865252979354, 1.3997056524703828, 1.6272719234974824, -0.637379376373666],
             [-8.611223268025917, 1.3429377291966658, 6.844250197696248, -1.7354219880745663, 4.068066725267432,
              -5.858291924971915, 3.7253619025400804, 3.2880686703508393, -0.3117496935169118, 0.5907304460785373,
              0.7762677045475129, 0.1992564014993217, 3.213077337595159, -4.08833388239098, 1.192695985758011,
              0.021671234653971458, 1.158718719575029, -1.1446580958572565, 0.9667818731837292, 0.6685677429061878,
              -0.33306148591879925, -0.9287860633117216, -0.7480496282719807, 0.877790914826948]]
