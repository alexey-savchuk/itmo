from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod


@dataclass
class Route:
    id: int
    origin: str
    destination: str
    time: datetime
    price: int


@dataclass
class Passenger:
    id: int
    name: str


@dataclass
class User:
    id: int
    email: str


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self) -> str:
        pass


class CardPaymentMethod(PaymentMethod):
    def pay(self):
        return "by card"


class EWalletPaymentMethod(PaymentMethod):
    def pay(self):
        return "by e-wallet"


class SMSPaymentMethod(PaymentMethod):
    def pay(self):
        return "by SMS"


@dataclass
class PaymentRequest:
    route: Route = None
    passengers: list[Passenger] = None
    payment_method: PaymentMethod = None

    def execute(self):
        print(f"""a ticket for a trip from "{self.route.origin}" to "{self.route.destination}" \
costs {self.route.price} dollars and will be paid {self.payment_method.pay()},
passengers {self.passengers}""")


class PaymentRequestBuilder:
    def __init__(self):
        self.request = PaymentRequest()

    def is_valid(self) -> bool:
        return all((
            self.request.passengers is not None and len(
                self.request.passengers) > 0,
            self.request.route is not None,
            self.request.payment_method is not None,
        ))

    def build(self):
        if not self.is_valid():
            raise RuntimeError("try to build invalid request")
        return self.request

    def add_passenger(self, passenger):
        if self.request.passengers is None:
            self.request.passengers = []
        self.request.passengers.append(passenger)

    def set_route(self, route):
        self.request.route = route

    def set_payment_method(self, payment_method):
        self.request.payment_method = payment_method


builder = PaymentRequestBuilder()

builder.set_route(Route(1, "Los Angeles", "San Francisco", datetime.now(), 29))
builder.add_passenger(Passenger(1, "John Doe"))
builder.add_passenger(Passenger(1, "Jane Doe"))
builder.set_payment_method(CardPaymentMethod())

request = builder.build()
request.execute()

builder.set_payment_method(EWalletPaymentMethod())

request = builder.build()
request.execute()

builder.set_payment_method(SMSPaymentMethod())

request = builder.build()
request.execute()
