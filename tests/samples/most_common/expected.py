from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_load


class FooSchema(Schema):
    name = fields.String(metadata={'description': 'foo name'})
    compare = fields.Integer(required=False)

    @post_load
    def do_nothing(self, data, **_):
        """docstring keeps"""
        return data
