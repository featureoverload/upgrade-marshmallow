import marshmallow as ma


class FooSchema(ma.Schema):
    name = ma.fields.String(metadata={'title': 'foo name', 'description':
        'foo name'})
