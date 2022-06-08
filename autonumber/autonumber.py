class autonumber:
    def load(country_tag: str, operator_tag: str, max_length: int, minimum: int=0, maximum=None) -> str:
        """This function generates phone numbers, using
        the specified range, country code, operator code,
        the maximum length of the number without the plus sign"""

        numbers = [] # All numbers will be stored here, after the execution of the loop
        # Remove the plus sign, if the user has set it
        if "+" in country_tag:
            country_tag = country_tag.replace("+", "")

        userlen = max_length-len(country_tag)-len(operator_tag) # We get the length of unique numbers
        # If the user has not set his own range limit, we will make it the default maximum
        if maximum == None:
            maximum = int("9"*userlen)

        # Phone number generation loop
        while minimum <= maximum:
            if len(str(minimum)) != userlen:
                needzeros = userlen - len(str(minimum)) # We get the number of zeros to be added to the output number
                numbers.append("+"+country_tag+operator_tag+"0"*needzeros+str(minimum)) # It is necessary to add zeros to the output number
            else:
                numbers.append("+"+country_tag+operator_tag+str(minimum))
            minimum += 1

        return numbers
