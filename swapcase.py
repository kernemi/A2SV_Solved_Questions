def swap_case(s):
    s=list(s)
    swapped = ""
    for i in range(len(s)):
        if s[i].isupper():
            s[i]= s[i].lower()
        elif s[i].islower():
            s[i]= s[i].upper()
        swapped += str(s[i])
    return swapped

