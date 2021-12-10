from marshmallow import Schema
from marshmallow import fields


def NoneEmptyString(**kwargs):  # noqa
    return fields.String(**kwargs)


class FooSchema(Schema):
    name = NoneEmptyString(title='foo name', description="foo name")
