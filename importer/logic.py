import random
from string import punctuation
from creditcardmeta import CC_META

class Logic():
    @staticmethod
    def validate_for_empty(request, row, broken: list):
        """check if any element in row is empty and returns list with broken element + skiping flag"""
        skip = False
        if (
                len(str(row[int(request.GET.get('name', '1')) - 1])) == 0
                    or
                    len(str(row[int(request.GET.get('dob', '2')) - 1])) == 0
                        or
                        len(str(row[int(request.GET.get('phone', '3')) - 1])) == 0
                            or
                            len(str(row[int(request.GET.get('address', '4')) - 1])) == 0
                                or
                                len(str(row[int(request.GET.get('cc', '5')) - 1])) == 0
                                    or
                                    len(str(row[int(request.GET.get('email', '6')) - 1])) == 0
            ):
            broken.append(row)
            skip = True
        return broken, skip

    @staticmethod
    def validate_name(request, row, broken):
        """checks if at least one special character in name"""
        skip = False
        for char in [x for x in punctuation if x != '-']:
            if char in row[int(request.GET.get('name', '1')) - 1]:
                broken.append(row[int(request.GET.get('name', '1')) - 1])
                skip = True
                break
        return broken, skip

    @staticmethod
    def validate_phone(request, row, broken):
        """checks if phone is in correct format"""
        # TO-DO use regex re for format detection
        _ = row[int(request.GET.get('phone', '3')) - 1]
        return None

    @staticmethod
    def validate_email(request, row, broken):
        """checks if ..."""
        return None

    @staticmethod
    def validate_credit_card(request, row, broken):
        """checks if ..."""
        return None

    @staticmethod
    def select_franchise():
        """selects franchise from random list"""
        # TO-DO choose based on credit card number
        random.seed(a=None, version=2)
        return random.choice(CC_META)
