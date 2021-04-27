import re

class mailCheck:

    def match(mail):
        regex = re.compile('^[A-Za-z0-9\._]+@[A-Za-z0-9]+(\.[A-Za-z]+)+$')
        return re.match(regex,mail) is not None



