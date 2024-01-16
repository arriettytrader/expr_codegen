# %%
import os
import sys
from pathlib import Path

# 修改当前目录到上层目录，方便跨不同IDE中使用
pwd = str(Path(__file__).parents[1])
os.chdir(pwd)
sys.path.append(pwd)
# ===============
# %%
# 从main中导入，可以大大减少代码
import matplotlib.pyplot as plt

from analysis.reports import create_2x2_sheet
from analysis.reports import create_2x3_sheet
from gp.main import *

# TODO 可替换成任意一代的种群文件
with open(LOG_DIR / f'hall_of_fame.pkl', 'rb') as f:
    pop = pickle.load(f)

df_input = pl.read_parquet('data/data.parquet')

# %%
from log.codes_9999 import main

df_output = main(df_input)
# %%
period = 5
split_x = '2020-01-01'

x = 'GP_0000'  # 考察因子
y1 = 'RETURN_OO_1'  # 计算净值用的1日收益率
# %%
y = 'RETURN_OO_5'  # 计算因子IC用的5日收益率
create_2x2_sheet(df_output, x, y, y1, period=period, split_x=split_x)
# %%
create_2x3_sheet(df_output, x, y, y1, period=period, split_x=split_x)

plt.show()

# %%