# Functions with Outputs


def format_name(first_name, last_name):
    '''Takes in a first name and last name and changes them to title case.
    '''
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()

    return f"{formatted_first_name} {formatted_last_name}"


print(format_name(input("What is your first name? "),
                  input("What is your last name? ")))
