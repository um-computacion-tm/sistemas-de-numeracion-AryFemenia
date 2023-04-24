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
#def all_dec(num,base):


#8 to 2/10/16



#16 to 2/8/10
