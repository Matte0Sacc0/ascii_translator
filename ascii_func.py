import os

_codes = ["NULL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL", "BS", "HT", "LF", "VT", "FF", "CR", "SO", "SI", "DLE",
          "DC1", "DC2", "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US", "space", "DEL", "nbsp"]


def _ascii_in_codes(ascii):
    ascii = int(ascii)
    if ascii < 33 or ascii == 127 or ascii == 255:
        if ascii == -1:
            ascii = 0
        elif ascii == 127:
            ascii = 33
        elif ascii == 255:
            ascii = 34
        return _codes[ascii]
    return "false"


def _find_index(array, string):
    for i, s in enumerate(array):
        if s.lower() == string.lower():
            return array[i], i
    return string, -1


def _char_in_codes(char):
    char, ascii = _find_index(_codes, char)
    if ascii == -1:
        return char, "false"
    # return 127 if ascii == 33 else 255 if ascii == 34 else "0 / -1" if ascii == 0 else ascii
    if ascii == 0:
        ascii = "0 / -1"
    if ascii == 33:
        ascii = 127
    elif ascii == 34:
        ascii = 255
    return char, ascii


def _clear_console():
    print("\033c", end="")
    print("PS " + format(os.getcwd()) + "> py ascii.py")


def _clear_line(n):
    n = int(n)
    if n > 0:
        print("\x1b[1A", end="\r")
        print("\x1b[2K", end="")
        _clear_line(n-1)


def translateInput(input_value):
    # input_value = input("Insert char or ASCII value: ")

    # if input_value == "clear" or input_value == "cls":
    #    _clear_console()
    # elif input_value == "cc":
    #    _clear_line(2)
    # else:

    try:
        input_value = int(input_value)
        if input_value < -1:
            return "ERROR: Invalid ASCII code"
        code = _ascii_in_codes(input_value)
        if code == "false":
            code = chr(input_value)

        return "`" + str(input_value) + "` in ASCII value -> " + code

    except:
        input_value, ascii = _char_in_codes(input_value)
        if ascii == "false":
            try:
                ascii = ord(input_value)
            except:
                return "ERROR: Invalid Char code"
        return "ASCII value of `" + input_value + "` -> " + str(ascii)
