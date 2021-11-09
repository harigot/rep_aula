'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz 
de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e 
o nível do volume permanecem dentro de faixas válidas.
'''



def channel_veryfication(channel):
    while True:
        try:
            if 0 <= int(channel) <= 99:
               return channel
            else:
                raise ValueError

        except ValueError:
            channel = input('enter a valid channel (1 a 99): ')
            continue


class TV:
    def __init__(self, channel = 0, volume = 0):
        self.channel = channel
        self.volume = volume

    def change_channel(self, channel):
        self.channel = channel_veryfication(channel)
        print('channel changed to', self.channel)

    def volume_up(self):
        if 0 <= self.volume <= 100:
            self.volume += 5
            print('volume is at', self.volume)
        else:
            print('volume is at maximum')
    
    def volume_down(self):
        if 0 <= self.volume <= 100:    
            self.volume -= 5
            print('volume is at', self.volume)
        else:
            print('volume is at minimum')


tv1 = TV()
tv1.change_channel(input('enter a channel: '))
tv1.volume_up()
tv1.volume_up()
tv1.volume_up()
tv1.volume_up()
tv1.volume_up()
tv1.volume_down()
tv1.volume_down()
tv1.volume_down()
