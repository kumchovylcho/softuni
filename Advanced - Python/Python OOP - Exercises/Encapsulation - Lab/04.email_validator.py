class EmailValidator:

    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        if len(name) >= self.min_length:
            return True
        return False

    def __is_mail_valid(self, mail):
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        return False

    def validate(self, email):
        email = email.split("@")
        get_domain = email[-1].split(".")
        name, mail, domain = email[0], get_domain[0], get_domain[-1]
        if self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True
        return False
