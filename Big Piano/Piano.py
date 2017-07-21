'''マインクラフトでピアノ演奏

The MagPi 57 掲載プログラムを改変したものです。

https://github.com/themagpimag/magpi-issue57/tree/master/MinecraftMakerGuide/Big%20Piano

使い方:

マインクラフトとSonic Piを起動、Sonic PiにMC_piano_sound.txtをロード、Play状態にし後でこのプログラムを実行します。
'''

from pythonosc import udp_client
from time import sleep

class McPiano:
    white_scale = (0, 2, 4, 5, 7, 9, 11)
    black_scale = (1, 3, 0, 6, 8, 10, 0)
    white_key_width = 3

    def __init__(self, mc, octave=1, base_key=48):
        self.mc = mc
        self.octave = octave
        self.base_key = base_key

    def bulldozer(self, x, y, z):
        mc.setBlocks(x-30, y-3, z-30, x+30*self.octave, y+20, z+30, 0)

    def white_key(self, x, y, z):
        self.mc.setBlocks(x, y-1, z, x+2, y-1, z+14, 44, 7)

    def black_key(self, x, y, z):
        self.mc.setBlocks(x, y-1, z, x+1, y-1, z+9, 49)

    def build_keys(self):
        x, y, z = self.mc.player.getTilePos()
        self.bulldozer(x, y, z)
        self.base_x = x
        stop = (7 * 3 * self.octave) - 1
        for i in range(0, stop, 3):
            self.white_key(x+i, y, z)
        notes = self.black_scale * self.octave
        for i, note in zip(range(2, stop+2, 3), notes):
            if note:
                self.black_key(x+i, y, z)
        # self.mc.player.setPos(x + 8, y + 3, z + 12)

    def play_note(self, sender, note):
        sender.send_message('/play_this', note)
        sleep(0.5)

    def play(self, host='127.0.0.1', port=4559):
        sender = udp_client.SimpleUDPClient(host, port)
        white_notes = []
        black_notes = []
        for i in range(self.octave):
            root = self.base_key + (12 * i)
            white_notes += [root+x for x in self.white_scale]
            black_notes += [root+x for x in self.black_scale]

        while True:
            x, y, z = self.mc.player.getTilePos()
            block_below = self.mc.getBlock(x, y-1, z)
            if block_below != 44 and block_below != 49:
                block_below = self.mc.getBlock(x, y, z)
            relative_x = x - self.base_x
            if block_below == 44:
                index = int(relative_x // 3)
                self.play_note(sender, white_notes[index])
            if block_below == 49:
                index = int(((relative_x + 1) // 3) - 1)
                self.play_note(sender, black_notes[index])

if __name__ == '__main__':
    from mcpi.minecraft import Minecraft
    mc = Minecraft.create()
    piano = McPiano(mc, 3)
    piano.build_keys()
    piano.play()
