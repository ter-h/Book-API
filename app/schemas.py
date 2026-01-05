from marshmallow import Schema, fields

class BookCreateSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    year_published = fields.Int(required=True)

class BookSchema(BookCreateSchema):
    id = fields.Int()
    created_at = fields.DateTime()