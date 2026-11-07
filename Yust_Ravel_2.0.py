import math
from playtones import play_sawtooth
#WARNING TURN VOLUME DOWN

class Layer:
    def __init__(self, space_mod, degree_offset):
        self.z = space_mod
        self.x = degree_offset / 360


def configure(layer_list):
    top_layer = layer_list[0]
    configured = []
    for i in range(0, top_layer.z): #looping for each element of the top layer
        pitch = i
        for l in range(0, len(layer_list) - 1): #looping for each layer
            upper_layer = layer_list[l]
            lower_layer = layer_list[l + 1]
            new = (pitch / upper_layer.z + upper_layer.x - lower_layer.x) * lower_layer.z #upper related to lower
            pitch = (math.floor(new) % lower_layer.z) #quantizing
        configured.append(pitch)
    print(configured)
    return (configured)


i = 11

Seven = Layer(7, 360/12/7*2) #offsets it up by a whole step
Twelve = Layer(12, 0)
Eighteen = Layer(18, 360/12/3/7*i) #offset by a third of a twelfth of 360

yust_ravel = [Seven, Eighteen, Twelve]

tones = configure(yust_ravel)
for n in tones:
    play_sawtooth(n)