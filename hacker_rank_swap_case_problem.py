def swap_case(s):
    res = []
    for ch in s:
        if ch.islower():
            res.append(ch.upper())
        elif ch.upper():
            res.append(ch.lower())
        else:
            res.append(ch)
    
    return "".join(res)

if __name__ == '__main__':
