import cv2
import os
import numpy as np

# 檢查是否存在輸出文件夾，如果不存在則創建
output_folder = 'Output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 讀取影像
traffic_lanes_image = cv2.imread('Sample_1.png')
cans_image = cv2.imread('Sample_1.png')
cv2.imshow('Sample_1.png', traffic_lanes_image)
# 對Traffic_Lanes.bmp進行直線偵測
gray_traffic_lanes = cv2.cvtColor(traffic_lanes_image, cv2.COLOR_BGR2GRAY)
edges_traffic_lanes = cv2.Canny(gray_traffic_lanes, 50, 150, apertureSize=3)
lines_traffic_lanes = cv2.HoughLines(edges_traffic_lanes, 1, np.pi / 180, 100)

# 繪製檢測到的直線
for line in lines_traffic_lanes:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(traffic_lanes_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 保存偵測結果
cv2.imwrite(os.path.join(output_folder, 'Sample_1_Output.png'), traffic_lanes_image)

# 顯示偵測結果
cv2.imshow('Traffic Lanes - Line Detection', traffic_lanes_image)


cv2.waitKey(0)
cv2.destroyAllWindows()