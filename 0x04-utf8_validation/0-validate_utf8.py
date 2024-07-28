#!/usr/bin/env python3
"""0-validate_utf8.py"""
def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    def check_continuation(byte):
        """check continuation"""
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        current_byte = data[i] & 0xFF
        
        if current_byte >> 7 == 0:  
            bytes_count = 1
        elif current_byte >> 5 == 0b110:  
            bytes_count = 2
        elif current_byte >> 4 == 0b1110:  
            bytes_count = 3
        elif current_byte >> 3 == 0b11110:  
            bytes_count = 4
        else:
            return False

        if i + bytes_count > len(data):
            return False

        for j in range(1, bytes_count):
            if not check_continuation(data[i + j] & 0xFF):
                return False

        i += bytes_count

    return True
