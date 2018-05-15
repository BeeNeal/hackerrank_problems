# You are given an integer  followed by  email addresses. Your task is to print a 
# list containing only valid email addresses in lexicographical order.


# Valid email addresses must follow these rules:

# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores.
# The website name can only have letters and digits.
# The maximum length of the extension is . 

def is_valid_email_address(string):
    """Checks extension, appropriate chars, does not exceed max length"""

    