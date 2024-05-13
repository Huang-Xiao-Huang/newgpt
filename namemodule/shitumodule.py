import cv2
import numpy as np
import sys
sys.path.append('./data')


#识图工具

dict_ = {'person': '人', 'bicycle': '自行车', 'car': '车', 'motorbike': '摩托车', 'aeroplane': '飞机', 'bus': '公共汽车',
         'train': '火车', 'truck': '卡车', 'boat': '船', 'traffic light': '红绿灯', 'fire hydrant': '消防栓',
         'stop sign': '停车标志', 'parking meter': '停车费', 'bench': '板凳上', 'bird': '鸟', 'cat': '猫', 'dog': '狗',
         'horse': '马', 'sheep': '羊', 'cow': '牛', 'elephant': '大象', 'bear': '熊', 'zebra': '斑马', 'giraffe': '长颈鹿',
         'backpack': '背包', 'umbrella': '伞', 'handbag': '手提包', 'tie': '领带', 'suitcase': '手提箱', 'frisbee': '飞盘',
         'skis': '滑雪板', 'snowboard': '滑雪板', 'sports ball': '体育球', 'kite': '风筝', 'baseball bat': '棒球棒',
         'baseball glove': '棒球手套', 'skateboard': '滑板', 'surfboard': '冲浪板', 'tennis racket': '网球拍', 'bottle': '瓶',
         'wine glass': '酒杯', 'cup': '杯', 'fork': '叉', 'knife': '刀', 'spoon': '勺子', 'bowl': '碗', 'banana': '香蕉',
         'apple': '苹果', 'sandwich': '三明治', 'orange': '橙色', 'broccoli': '西兰花', 'carrot': '胡萝卜', 'hot dog': '热狗',
         'pizza': '披萨', 'donut': '甜甜圈', 'cake': '蛋糕', 'chair': '椅子', 'sofa': '沙发', 'pottedplant': '盆栽植物床上',
         'bed': '餐桌厕所。', 'diningtable': '电视监视器移动PC。', 'toilet': '鼠标', 'tvmonitor': '远程', 'laptop': '键盘',
         'mouse': '手机', 'remote': '微波', 'keyboard': '烤箱', 'cell phone': '烤面包机', 'microwave': '水槽', 'oven': '冰箱',
         'toaster': '书', 'sink': '时钟', 'refrigerator': '花瓶', 'book': '剪刀', 'clock': '泰迪熊', 'vase': '头发干燥器',
         'scissors': '牙刷'}

import  os
data = os.getcwd()
d = data
d = '\\'.join(data.split('\\')[:-1]) + "\\data\\"
print(d)
print(fr'{d}coco.names')

# 识别工具
def shiTu(image_list, keyword):
    da_list = []
    for r_image in image_list:
        # ============获取分类信息===================
        # classes = open(fr'{d}coco.names', 'rt').read().strip().split("\n")
        classes = open('.\\bigdemo\\data\\coco.names', 'rt').read().strip().split("\n")
        # ===========模型初始化、推理===========
        net = cv2.dnn.readNetFromDarknet(r"..\bigdemo\data\yolov3.cfg",
                                         r"..\bigdemo\data\yolov3.weights")
        # net = cv2.dnn.readNetFromDarknet(fr"{d}yolov3.cfg",
        #                                  fr"{d}yolov3.wrights")

        # D:\AI\大语言模型项目\demo1
        try:
            image = cv2.imread(r_image)

            image = cv2.resize(image,(100,100))
            blob = cv2.dnn.blobFromImage(image, 1.0 / 255.0, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outInfo = net.getUnconnectedOutLayersNames()
            outs = net.forward(outInfo)
            # ===========获取置信度较高的边框===========
            classIDs = []  # 所有分类ID
            boxes = []  # 所有边框
            confidences = []  # 所有置信度
            (H, W) = image.shape[:2]  # 图像的宽、高，辅助确定图像内边框位置
            for out in outs:  # 各个输出层
                for alternative in out:  # 各个框框
                    # detection内存储的是边框位置(前四个)的百分比、置信度(从第5个开始所有)
                    # 例如，0.5表示高度（或宽度）的50%
                    scores = alternative[5:]  # 所有分类的置信度
                    classID = np.argmax(scores)  # 根据最高置信度的id确定分类id
                    confidence = scores[classID]  # 置信度
                    # 确定所有可能的边框
                    # 仅考虑置信度大于0.5的，太小的忽略
                    if confidence > 0.5:
                        box = alternative[0:4] * np.array([W, H, W, H])  # 将边界框返回图片尺寸
                        (centerX, centerY, width, height) = box.astype("int")
                        # centerX，centerY是矩形框的中心点，要通过他们计算出左上角坐标x,y
                        x = int(centerX - (width / 2))  # x方向中心点-框宽度/2
                        y = int(centerY - (height / 2))  # y方向中心点-框高度/2
                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        classIDs.append(classID)
            # 非极大值抑制，将重合的边框去重处理
            indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.5)
            # 绘制边框及置信度、分类
            for i in range(len(boxes)):
                if i in indices:
                    # x, y, w, h = boxes[i]
                    # color = [int(color) for color in COLORS[classIDs[i]]]  # 边框颜色
                    text = "{}: {:.2f}%".format(classes[classIDs[i]], confidences[i] * 100)
                    # print(dict_.text)
                    print(keyword)
                    text = text.split(":")[0]
                    print(text)
                    if keyword in dict_[text]:
                        dd = r_image.split("\\")[-1]
                        da_list.append(dd)
                    else:
                        pass
        except:pass
                # print(da_list)
    return da_list




# if __name__ == "__main__":
#     image_list1 = [r"C:\Users\10578\Pictures\good1\1.png", r"C:\Users\10578\Pictures\good1\2.png"]
#     new_imge = shiTu(image_list1, "person")
#     print(new_imge)