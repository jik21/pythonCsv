# Python Program - Convert Hexadecimal to Binary


file = open("in.hex", "r")
 
my_hexdata = file.read()  

scale = 16 ## equals to hexadecimal

num_of_bits = 8

binData = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)

with open("out.bin", "w") as text_file:
    text_file.write(binData)
