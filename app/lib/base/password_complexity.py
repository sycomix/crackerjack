class PasswordComplexityManager:
    def __init__(self, min_length, min_lower, min_upper, min_digits, min_special):
        self.min_length = int(min_length)
        self.min_lower = int(min_lower)
        self.min_upper = int(min_upper)
        self.min_digits = int(min_digits)
        self.min_special = int(min_special)

    def meets_requirements(self, password):
        if len(password) < self.min_length:
            return False

        lower = upper = digits = special = 0
        for c in password:
            if c.islower():
                lower += 1
            elif c.isupper():
                upper += 1
            elif c.isdigit():
                digits += 1
            else:
                special += 1

        return (
            lower >= self.min_lower
            and upper >= self.min_upper
            and digits >= self.min_digits
            and special >= self.min_special
        )

    def get_requirement_description(self):
        desc = [
            f"Minimum Length is {str(self.min_length)}",
            f"Minimum Lowercase: {str(self.min_lower)}",
            f"Minimum Uppercase: {str(self.min_upper)}",
            f"Minimum Digits: {str(self.min_digits)}",
            f"Minimum Special: {str(self.min_special)}",
        ]
        return ", ".join(desc)
