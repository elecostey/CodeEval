def clean_words(test_string):
    new_string = ""
    for object in test_string:
        if object.isalpha() == True:
            new_string += str(object.lower())
        elif object.isalpha() == False:
            new_string += str(".")
    return new_string.split(".")

def clean_spaces(new_string):
    final_string = ""
    for item in new_string:
        if len(item) >= 1:
            final_string += str(item) + str(" ")
    return final_string

print clean_spaces(clean_words("?//-cOdE/^^**eVaL"))