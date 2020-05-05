# -*- encoding: utf-8 -*-
# ------------------------------------
# @env : python 3.6.0
# @auth : elviscttian
# @func : ������Ϊ���� Matplotlib ��?��ɢ��ͼ
# ------------------------------------
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties  # ������������

font = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)  # ʹ�ñ�������(Windows����ϵͳ)

y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]

x_3 = range(1, 32)
x_10 = range(51, 82)

# ����ͼ�δ�С
plt.figure(figsize=[20, 8], dpi=80)

# ʹ��scanner��������ɢ��ͼ , ��֮ǰ��������ͼ��Ψһ����
plt.scatter(x_3, y_3, label="���·�")
plt.scatter(x_10, y_10, label="ʮ�·�")

# ����x��Ŀ̶�
_x = list(x_3) + list(x_10)
_xtick_labels = ["3��{}��".format(i) for i in x_3]
_xtick_labels += ["10��{}��".format(i - 50) for i in x_10]
plt.xticks(_x[::3], _xtick_labels[::3], fontproperties='SimHei', rotation=45)

# ���ͼ��
plt.legend(loc='upper left', prop=font)

plt.xlabel("ʱ��", fontproperties='SimHei', size=16)
plt.ylabel("�¶�", fontproperties='SimHei', rotation=90, size=16)
plt.title("����", fontproperties='SimHei', size=18)

plt.savefig('./����ɢ��ͼ')  # ����ͼ��
plt.pause(1)  # ��ʾͼ�� 3s ���Զ��ر�
# plt.show()  # չʾͼ��