# -*- encoding: utf-8 -*-
# ------------------------------------
# @env : python 3.x
# @auth : elviscttian
# @func : ������Ϊ���� Matplotlib �� �������Һ���
# ------------------------------------
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties  # ������������

font = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)  # ʹ�ñ�������(Windows����ϵͳ)

x = np.arange(100) / 10
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=[20, 8], dpi=80)  # ͼ���С
plt.title('����/���Һ���ͼ��', fontproperties="SimHei", size=20)  # ����
plt.xlabel('x ��', fontproperties="SimHei", size=16)  # x������
plt.ylabel('y ��', fontproperties="SimHei", rotation=90, size=16)  # y������
plt.xticks(x[::10], x[::10])  # x��̶�����
plt.grid(alpha=0.5)  # ������� , ����������͸����

plt.plot(x, y1, label="sin����", color="red", linestyle=None, linewidth=3, alpha=0.7)
plt.plot(x, y2, label="cos����", color="cyan", linestyle='--')

plt.legend(prop=font, fontsize=18, loc='upper left')  # ���ͼ�� , ����ʾplt.plot��label

plt.savefig('./�����Һ���ͼ��')  # ����ͼ��
plt.pause(1)  # ��ʾͼ�� 3s ���Զ��ر�
# plt.show()  # չʾͼ��