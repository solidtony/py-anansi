'''
Module contains the escape character functions for fonts intended primarily for
internal use.
'''
from anansi.escape_char import OCTAL_ESC



def esc(cmd:str | int) -> str:
    return OCTAL_ESC + str(cmd) + 'm'
