import struct


def float_to_ieee754(f):
    packed = struct.pack('>f', f)
    bits = ''.join(f'{byte:08b}' for byte in packed)
    return bits