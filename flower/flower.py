'''スティーブの花咲か爺さん

Raspberry Pi公式ドキュメントに掲載のプログラム
https://www.raspberrypi.org/learning/getting-started-with-minecraft-pi/worksheet/
'''
from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
flower = 38

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, flower)
    sleep(0.1)
