import marshmallow


class FooSchema(marshmallow.Schema):
    name = marshmallow.fields.String(metadata={'title': 'foo name',
        'description': 'foo name'})
