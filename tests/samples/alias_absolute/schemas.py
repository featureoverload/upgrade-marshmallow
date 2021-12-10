import marshmallow as ma


class FooSchema(ma.Schema):
    name = ma.fields.String(title='foo name', description="foo name")
