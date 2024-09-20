calls = 0

def count_calls():
    global calls
    calls = calls + 1
    return calls

def string_info(word):
    count_calls()
    return (len(word), word.upper(), word.lower())


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [x.lower() for x in list_to_search]
    y = string in list_to_search
    return y



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)