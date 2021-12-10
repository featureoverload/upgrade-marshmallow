from marshmallow import Schema
from marshmallow.fields import Field
from marshmallow.fields import Raw
from marshmallow.fields import String
from marshmallow.fields import UUID
from marshmallow.fields import Number
from marshmallow.fields import Integer
from marshmallow.fields import Decimal
from marshmallow.fields import Boolean
from marshmallow.fields import Float
from marshmallow.fields import DateTime
from marshmallow.fields import NaiveDateTime
from marshmallow.fields import AwareDateTime
from marshmallow.fields import Time
from marshmallow.fields import Date
from marshmallow.fields import TimeDelta
from marshmallow.fields import Url
from marshmallow.fields import URL
from marshmallow.fields import Email
from marshmallow.fields import IP
from marshmallow.fields import IPv4
from marshmallow.fields import IPv6
from marshmallow.fields import IPInterface
from marshmallow.fields import IPv4Interface
from marshmallow.fields import IPv6Interface
from marshmallow.fields import Str
from marshmallow.fields import Bool
from marshmallow.fields import Int


class FooSchema(Schema):
    field = Field(title='Field')
    raw = Raw(title='Raw')
    string = String(title='String')
    uuid = UUID(title='UUID')
    number = Number(title='Number')
    integer = Integer(title='Integer')
    decimal = Decimal(title='Decimal')
    boolean = Boolean(title='Boolean')
    float = Float(title='Float')
    datetime = DateTime(title='DateTime')
    naivedatetime = NaiveDateTime(title='NaiveDateTime')
    awaredatetime = AwareDateTime(title='AwareDateTime')
    time = Time(title='Time')
    date = Date(title='Date')
    timedelta = TimeDelta(title='TimeDelta')
    url = Url(title='Url')
    url = URL(title='URL')
    email = Email(title='Email')
    ip = IP(title='IP')
    ipv4 = IPv4(title='IPv4')
    ipv6 = IPv6(title='IPv6')
    ipinterface = IPInterface(title='IPInterface')
    ipv4interface = IPv4Interface(title='IPv4Interface')
    ipv6interface = IPv6Interface(title='IPv6Interface')
    str = Str(title='Str')
    bool = Bool(title='Bool')
    int = Int(title='Int')
