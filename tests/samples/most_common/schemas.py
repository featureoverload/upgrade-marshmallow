from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_load


class FooSchema(Schema):
    name = fields.String(description='foo name')
    compare = fields.Integer(required=False)

    @post_load
    def do_nothing(self, data, **_):
        """docstring keeps"""
        return data


def normal_fun():
    """regression test: compatible different cases without initial"""
    pass


normal_fun()
