import marshmallow


class FooSchema(marshmallow.Schema):
    name = marshmallow.fields.String(title='foo name', description="foo name")
