#Hacer que rellene con 0 hasta 2^8 a la izquierda

#10 to 2/8/16
def dec_bin(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def dec_oct(decimal):
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def dec_hex(decimal):
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal //= 16
    return hexadecimal
#2 to 8/10/16
'''def bin_oct(bin):
    binary_number = bin
    decimal_number = int(binary_number, 2)
    octal_number = oct(decimal_number)
    return octal_number'''

def bin_dec(binary):
    bin = binary
    dec = int(bin, 2)
    return dec
'''
def bin_hex(binary):
    bin = binary
    dec = int(bin, 2)
    hex = hex(dec)
    return dec'''
#8 to 2/10/16
def oct_bin(octal):
    decimal_num = int(str(octal), 8)
    binary_num = bin(decimal_num)[2:]
    return binary_num

def oct_dec(octal_num):
    decimal_num = int(str(octal_num), 8)
    return decimal_num

def oct_hex(octal_num):
    decimal_num = int(str(octal_num), 8)
    hexadecimal_num = hex(decimal_num)[2:]
    return hexadecimal_num
#16 to 2/8/10
def hex_bin(hex_num):
    hex_num = hex_num
    binary_num = bin(int(hex_num, 16))[2:]
    return binary_num

def hex_oct(hex_num):
    hex_num = hex_num
    octal_num = oct(int(hex_num, 16))[2:]
    return octal_num

def hex_dec(hex_num):
    hex_num = "2A"
    decimal_num = int(hex_num, 16)
    return decimal_num
