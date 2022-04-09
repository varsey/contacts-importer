import random
from string import punctuation
from .models import Contacts

class Logic():
    @staticmethod
    def check_empty(request, row, broken):
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
    def name_checker(request, row, broken):
        """checks if at least one special character in name"""
        skip = False
        for char in [x for x in punctuation if x != '-']:
            if char in row[int(request.GET.get('name', '1')) - 1]:
                broken.append(row[int(request.GET.get('name', '1')) - 1])
                skip = True
                break
        return broken, skip


    @staticmethod
    def phone_checker(request, row, broken):
        """checks if phone is in corret format"""
        # TO-DO use regex re for format detection
        _ = row[int(request.GET.get('phone', '3')) - 1]
        return None


    @staticmethod
    def select_franchise():
        """selects franchise from random list"""
        # TO-DO choose based on credit card number
        random.seed(a=None, version=2)
        fr_list = [
            'American Express',
            'Bankcard',
            'China T-Union',
            'Diners Club enRoute',
            'Diners Club International',
            'Diners Club United States & Canada',
            'Discover Card',
            'UkrCard',
            'RuPay',
            'InterPayment',
            'InstaPayment',
            'JCB',
            'Laser',
            'Maestro UK',
            'Maestro',
            'Dankort',
            'Mir',
            'NPS Pridnestrovie',
            'Mastercard',
            'Solo',
            'Switch',
            'Troy',
            'Visa',
            'Visa Electron',
            'UATP',
            'Verve',
            'LankaPay',
            'UzCard',
            'Humo',
            'GPN'
        ]
        return random.choice(fr_list)
