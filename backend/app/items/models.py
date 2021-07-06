from tortoise import fields, Model


class Item(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=128)
    pic = fields.CharField(max_length=1024)
    desc = fields.TextField()

    user = fields.ForeignKeyField('users.User', related_name='items')

    # id = fields.IntField(pk=True)

    class PydanticMeta:
        exclude = ['user']
