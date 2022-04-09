import random
from string import punctuation


class Logic():
    @staticmethod
    def name_checker(request, row, broken):
        """checks if at least one special character in name"""
        stop = False
        for char in [x for x in punctuation if x != '-']:
            if char in row[int(request.GET.get('name', '1')) - 1]:
                broken.append(row[int(request.GET.get('name', '1')) - 1])
                stop = True
                break
        return broken, stop


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
