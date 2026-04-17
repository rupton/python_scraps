def parse_args(args):
    substitute_keys = {}
    for pair in args.split(','):
        if "=" in pair:
            try:
                key, val = pair.strip().split('=')
                if len(key.strip()) == 1 and len(val.strip()) == 1 and key.isalpha() and val.isalpha():
                    substitute_keys[key.upper()] = val.upper()
            except ValueError:
                print(f"Invalid format {pair.strip()} - skipping")
                
    return substitute_keys

def letter_count(user_input):
    frequency = {}
    for ch in user_input:
        if ch.isalpha():
            ch = ch.upper()
            frequency[ch] = frequency.get( ch, 0 ) + 1
    return frequency
        
    
subs_keys = input("Please enter the list of cryptogram substitutions in the form A=N, B=C, etc. ")
print(parse_args(subs_keys))

usr_input = input("Please enter your Crytogram ")
print(letter_count(usr_input))