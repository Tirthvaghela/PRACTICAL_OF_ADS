import numpy as np
import pandas as pd

# 3. Convert dictionary marks={'Math':35,'Science':48,'English':55,'History':42} into Series.
# Display subjects where marks < 50.

marks={'Math':35,'Science':48,'English':55,'History':42}

s_3 = pd.Series(marks)

print("-----Series-----")
print(s_3)
print("----------------")

print("-----Marks where < 50-----")
print(s_3[s_3 < 50])
print("----------------")