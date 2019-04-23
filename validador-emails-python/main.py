import re

def filter_email(emails):
    """Email validator - using lambda function
    
    Arguments:
        emails {list} -- Email's list for all email to be validated
    
    Returns:
        list -- List of valid emails
    """
    regex = '^([0-9a-zA-Z]([-\.\_\w]*[0-9a-zA-Z_-])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{1,3})$'
    email_valids = filter(lambda email: re.match(regex, email), emails)
    return list(email_valids)