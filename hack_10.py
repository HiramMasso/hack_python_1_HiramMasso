"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    mapping = {
        'f': 'F',
        'o': '0',
        'z': 'Z',
        'i': '1',
        'm': 'M',
        'a': '@',
        'n': 'N'
    }
    result = [""] * len("fooziman")
    for index, char in enumerate("fooziman"):
        result[index] = mapping[char]
    
    return result