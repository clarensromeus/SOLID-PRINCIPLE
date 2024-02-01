# (ISP) Inteface Segragation Principle, it is another fullfillment and feather in uncle Bob's cap, he accordingly said that
# clients should not be forced to use details they do not want, interfaces belong to clients not hierarchies,
# that is to say that specific client should implement only concerned methods

from abc import ABCMeta, abstractmethod
from typing import Self
import pprint

class DebitPay(metaclass=ABCMeta):
    @abstractmethod
    def debit_payment(self: Self, card_type: str):
        raise NotImplementedError("Sorry, impossible implementation")

class CreditCardPay(metaclass=ABCMeta):
    @abstractmethod
    def credit_card_payment(self: Self, card_type: str):
        raise NotImplementedError("Sorry, impossible implementation")

class MasterCardPay(metaclass=ABCMeta):
    @abstractmethod
    def mastercard_payment(self: Self, card_type: str):
        raise NotImplementedError("Sorry, impossible implementation")
    
    
# this class implement only methods of CreditCardPay, DebitPay class
class CapitalBank(DebitPay, CreditCardPay):
    __debit: dict[str, str]
    __credit: dict[str, str]
    
    def __init__(self, username: str, email: str, vocation: str) -> Self:
        self.username = username
        self.email = email
        self.vocation = vocation
        
    def debit_payment(self: Self, card_type: str) -> dict[str, str]:
        self.__debit = {"username": self.username, "email": self.email,  "card": card_type}
        return self.__debit
    
    def credit_card_payment(self: Self, card_type: str) -> dict[str, str]:
        self.__credit = {"username": self.username, "email": self.email,  "card": card_type}
        return self.__credit
    
    
# this class implements only methods of the DebitPay and LayOff class
class SocialistBank(DebitPay, MasterCardPay):
    __debit: dict[str, str]
    __mastercard: dict[str, str]

    def __init__(self, username: str, email: str, vocation: str) -> Self:
        self.username = username
        self.email = email
        self.vocation = vocation
        
    def debit_payment(self: Self, card_type: str):
        self.__debit = {"username": self.username, "email": self.email,  "card": card_type}
        return self.__debit
    
    def mastercard_payment(self: Self, card_type: str):
        self.__mastercard = {"username": self.username, "email": self.email,  "card": card_type}
        return self.__mastercard
    
    
# this class implements only methods of the CreditCardPay and WelcomeProcess
class NationalBank(CreditCardPay, DebitPay, MasterCardPay):
    __credit: dict[str, str]
    __debit: dict[str, str]
    __mastercard: dict[str, str]
    
    def __init__(self, username: str, email: str, vocation: str) -> Self:
        self.username = username
        self.email = email
        self.vocation = vocation
            
    def credit_card_payment(self: Self, card_type: str) -> dict[str, str]:
        self.__credit = {"username": self.username, "email": self.email,  "card": card_type}
        return self.__credit
    
    def debit_payment(self: Self, card_type: str):
        self.__debit = {"username": self.username, "email": self.email,  "card": card_type}
        return self.__debit
    
    def mastercard_payment(self: Self, card_type: str):
        self.__mastercard = {"username": self.username, "email": self.email,  "card": card_type}
        return self.__mastercard
    

# start intantiating the CapitalBank class 
capitalbank: CapitalBank = CapitalBank(username="romeusclarens", email="clarensromeus33@gamil.com", vocation="S. Engineer")
pprint.pprint(dict(capitalbank.__dict__.items()))
# now display all the methods implementation of the Capital Bank
pprint.pprint(capitalbank.debit_payment(card_type="UNIBANK"))
pprint.pprint(capitalbank.credit_card_payment(card_type="VISA"))
pprint.pprint(capitalbank.debit_payment(card_type="WERNSTERN_UNION"))
# Socialistbank Class intantiation
socialistbank: SocialistBank = SocialistBank(username="clervilwoodlet", email="clervilwoodlet33@gmail.com", vocation="music producer")
# displaying all methods of the socialist bank
pprint.pprint(socialistbank.debit_payment(card_type="UNIBANK"))
pprint.pprint(socialistbank.mastercard_payment(card_type="MASTERCARD"))
# CapitalistBank Class instantiation
nationalbank: NationalBank = NationalBank(username="clervilwoodlet", email="clervilwoodlet44@gmail.com", vocation="music producer")
pprint.pprint(dict(nationalbank.__dict__.items()))
# now display all the methods implementation of the National Bank
pprint.pprint(nationalbank.mastercard_payment(card_type="MASTERCARD"))
pprint.pprint(nationalbank.credit_card_payment(card_type="AMERICAN EXPRESS"))
pprint.pprint(nationalbank.debit_payment(card_type="SOGEBANK"))

