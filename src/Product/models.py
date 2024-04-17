from marshmallow import Schema, fields

class Product(Schema):
    id = fields.Int()
    name = fields.Str()