import re


def validate_email(emails):
  pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com)"
  if re.fullmatch(pattern.lower(), emails):
      return True
  else:
      return False


 # for i in emails:
 #       if re.fullmatch(r"[a-zA-z0-9@]+", i):
 #           return True
 #       else:
 #           return False