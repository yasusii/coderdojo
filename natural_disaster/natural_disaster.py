"""
https://crazysqueak.wordpress.com/2015/11/29/disasters-minecraft/
"""
import time
from mcpi import minecraft
from mcpi import block

def meteor(mc, x, z):
    mc.postToChat('Meteor approaching!')
    y = 64 # この高さから落ちてくる
    h = mc.getHeight(x, z) # 落下地点の高さ
    # 隕石はxのマイナス方向からやって来る。(64 - h)落下するので、その分を調整
    x -= (64 - h)

    while y > h:
        y -= 1
        x += 1
        mc.setBlocks(x-2, y-2, z-2, x+2, y+2, z+2, block.OBSIDIAN.id)
        time.sleep(0.05)
        mc.setBlocks(x-2, y-2, z-2, x+2, y+2, z+2, block.AIR.id)

    mc.setBlocks(x-2, y-2, z-2, x+2, y+2, z+2, block.LAVA.id)
    mc.setBlocks(x-1, y-1, z-1, x+1, y+1, z+1, block.OBSIDIAN.id)

mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
meteor(mc,x+10, z)
