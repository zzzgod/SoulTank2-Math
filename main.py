import math


def calculate_attach_point(x: float, y: float, angle: float, width: int, height: int) -> tuple[float, float]:
    """
    计算图像旋转之后，附着点新的坐标（相对图像左上角）
    :param x: 原始图像上附着点的x坐标
    :param y: 原始图像上附着点的y坐标
    :param angle: 图像旋转角
    :param width: 图像原始宽度
    :param height: 图像原始高度
    :return: 新的附着点坐标
    """
    arc1=math.atan2(y,x)
    deg1=math.degrees(arc1)
    deg1=(deg1+angle)%360
    angle1=angle%360
    raw_x=float()
    raw_y=float()
    if(0<=angle1<90):
        raw_y=0
        raw_x=height*math.sin(math.radians(angle1))
    elif(90<=angle1<180):
        raw_y=height*math.sin(math.radians(angle1)-math.pi/2)
        raw_x=height*math.cos(math.radians(angle1)-math.pi/2)+width*math.sin(math.radians(angle1)-math.pi/2)
    elif (180<= angle1 < 270):
        raw_y = height * math.cos(math.radians(angle1) - math.pi)+width*math.sin(math.radians(angle1)-math.pi)
        raw_x = width*math.cos(math.radians(angle1)-math.pi)
    elif (270 <= angle1 <= 360):
        raw_y = width * math.cos(math.radians(angle1) - (3/2)*math.pi)
        raw_x = 0

    dis=math.sqrt(x ** 2.0 +y** 2.0)
    result_x=raw_x+dis*math.cos(math.radians(deg1))
    result_y=raw_y+dis*math.sin(math.radians(deg1))
    return result_x,result_y


