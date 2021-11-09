from marshmallow import Schema, fields

class QrDecodeArgs(Schema):

    title = fields.String(required=True)

    class Meta:
        strict = True
