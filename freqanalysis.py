
freq_alpha = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
count_dict = []


def replace_chars(message):
    global freq_alpha
    global count_dict

    get_count(message)
    ordered_chars = sort_chars()
    message = message.upper()
    
    for i in range(len(ordered_chars)):
        old_char = ordered_chars[i]
        new_char = freq_alpha[i]
        message = message.replace(old_char, new_char,)   
    return message

def get_count(message):
    global freq_alpha
    global count_dict
    for char in freq_alpha:
        count = 0
        for c in message:
            if c.upper() == char:
                count += 1
        count_dict.append((count, char))
        count_dict.sort(reverse=True)

def sort_chars():
    global count_dict
    ordered_chars = ''
    for item in count_dict:
        count, char = item
        ordered_chars += char
    
    return ordered_chars

def user_swap_char(new_message):
    user_input = input("Enter characters to swap (ex. E -> A) ")
    user_input.split(' -> ')
    new_message.replace(user_input[0], user_input[1])
    return new_message
            

if __name__ == '__main__':
    message = """Wxtk Vnlmhtxk,
                Px tkx atiir mh pxevhfx tl hnk gxpxlm vnlmhfxk hy hnk xvnkx bWkhWkbox vehnw ybex latkbgz lxkobvx. T ltyx ietvx yhk tee rhnk ybexl.
                Lmhkx tgr ybex
                bWkhiWkbox Imtkml rhn pbma 15 IU hy ykxx hgebgx hk hyyebgx Imhktzx, lh rhn vtg dxxl ptkxs, ubgtkbxl, itbgmbgzl, yetzl, ybkfptkxl, ubmvhbgl, pkbmxnil — tgrmabgz
                Lxx rhnk lmnyy tgrpaxkx
                Rhnk ybexl bg bWkhiWkbox vtg ux kxtvaxw ykhf tgr yhhutgbsxk, Iftkm ykbwzx 2000, Ittkm atnl, Mxfih-t-ftmbv, hk txwbt M. Lh paxkxoxk rhn zh, rhnk ybexl yheehp.
                Latkx ybexl tgw yhe'Mkl"""
    new_message = replace_chars(message)
    print(new_message)
