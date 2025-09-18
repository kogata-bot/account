from django.db.models import (
    Model,
    CharField,
    TextField,
    DateField,
    DateTimeField,
    IntegerField,
    FloatField,
    ForeignKey,
    CASCADE,
)

CATEGORY = (
    ("membership", "正規会員"),
    ("visitor", "ビジター"),
    ("other", "その他"),
)
STMT = (
    ("attend", "参加"),
    ("absent", "不参加"),
)


class Member(Model):
    name = CharField(max_length=50, null=False, blank=False)
    membership_type = CharField(
        max_length=50, choices=CATEGORY, null=False, blank=False
    )
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Event(Model):
    date = DateField(null=False, blank=False)
    participants = CharField(max_length=10, choices=STMT, default="absent")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    member = ForeignKey(Member, on_delete=CASCADE)

    def __str__(self):
        return str(self.date)


class Payment(Model):
    unit_teach_price = IntegerField(default=1000)
    unit_room_price = IntegerField(default=100)
    room_price = FloatField(null=True, blank=True)
    extra_income = IntegerField(default=0)
    extra_outgo = IntegerField(default=0)
    memo = TextField(max_length=200, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    event = ForeignKey(Event, unique=True, on_delete=CASCADE)

    def __str__(self):
        return str(self.event)

    @property #参加人数
    def cnt_person(self) -> int:
        cnt = Event.objects.filter(date=str(self.event),participants='attend').count()
        return cnt

    @property #日謝
    def get_teach_price(self) -> int:
        return self.unit_teach_price * self.cnt_person

    @property  # 部屋代残金
    def get_room_balance(self) -> int:
        return self.unit_room_price * self.cnt_person - self.room_price
