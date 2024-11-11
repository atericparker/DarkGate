##Claude SOnnet + Some manual tweaks to improve accuracy. Encrypt / string routines accurately emulate autoit script
import binascii
import data
data = data.get_data()
def encrypt(value: bytes, key: bytes) -> str:
    # Calculate key_alt (equivalent to $IKEYALT logic)
    key_alt = len(key)
    for i in range(len(key)):
        key_alt = key[i] ^ key_alt  # BITXOR operation
    
    # Encrypt the value
    encrypted = ""
    for i in range(len(value)):
        # Perform the encryption operations:
        # 1. Get byte from value
        # 2. XOR with key_alt
        # 3. NOT operation
        # 4. Convert to character
        encrypted_byte = ~(value[i] ^ key_alt) & 0xFF  # & 0xFF to keep it in byte range
        encrypted += chr(encrypted_byte)
    
    return encrypted


    

def binary_to_string(hex_str):
    # Remove "0x" prefix if present
    hex_str = hex_str.replace("0x", "")
    
    # Convert hex string to bytes
    byte_array = bytearray.fromhex(hex_str)
    

    return byte_array


# Key in binary format (this should match what AutoIt script was using)
key = b"jMXwoXaT"  # Replace this with the actual key you want to try
lines = ['0xB99191AE898F889E89BE8F989C8998D5DF9F848998A6CCCAC9C8CECBA0DFD4','0xB99191BE9C9191D5DF96988F939891CECFD3999191DFD1DFBFB2B2B1DFD1DFAB948F89889C91AD8F9289989E89DFD1DF8D898FDFD1B99191AE898F889E89BA9889AD898FD5D98D89D4D1DF949389DFD1CCCAC9C8CECBDDD1DF998A928F99DFD1CD85C9CDD1DF998A928F99D7DFD193889191D4','0xB99191AE898F889E89AE9889B99C899CD5D98D89D1CCD1D9999C899CD4', '0xB99191BE9C9191D5DF888E988FCECFD3999191DFD1DF949389DFD1DFB8938890AA949399928A8EDFD1DF8D898FDFD1B99191AE898F889E89BA9889AD898FD5D98D89D4D1DF918D9C8F9C90DFD1CDD4']
for line in lines:
    decrypted_data = encrypt(binary_to_string(line),key)
    # Print the decrypted result
    print("Decrypted data:", decrypted_data)
with open('data.out', 'wb') as f:
    databytes = binary_to_string(data)
    #decrypted = encrypt_bytes(databytes, key )
    f.write(databytes)
