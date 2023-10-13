from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy
import operator
from functools import reduce

# Userモデルを取得し、カスタムユーザーモデルをサポートするために使用します
User = get_user_model()

# RoomQuerysetはRoomモデルのカスタムQuerySetです
class RoomQueryset(models.QuerySet):
    def _related_user(self, user=None):
        try:
            # ルームのホストと指定したユーザーが参加者として含まれるルームをフィルタリングします
            queryset = self.filter(models.Q(host=user) | models.Q(participants__in=[user.pk]))
        except:
            # エラーが発生した場合、クエリセットは変更せずにそのまま返されます
            queryset = self

        return queryset

    def filtering(self, user=None, keywords='', order='-created_at'):
        words = keywords.split()
        queryset = self._related_user(user=user)

        if words:
            # キーワードを含むルームをフィルタリングする条件を作成します
            condition = reduce(operator.or_, (models.Q(name__icontains=word) for word in words))
            queryset = queryset.filter(condition)

        # 指定された順序でクエリセットを並べ替え、重複を削除します
        return queryset.order_by(order).distinct()
#aiの名称を格納
class ai_Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
# Roomモデルはチャットルームを表します
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(gettext_lazy('Room name'), max_length=64)
    created_at = models.DateTimeField(gettext_lazy('Created time'), default=timezone.now)
    participants = models.ManyToManyField(User, related_name='rooms', verbose_name=gettext_lazy('Participants'), blank=True)
    ai_Tag = models.ManyToManyField(ai_Tag, related_name='rooms', verbose_name=gettext_lazy('ai_Tag'))

    # RoomQuerysetを使用してカスタムクエリを実行できるようにします
    objects = RoomQueryset.as_manager()

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        # チャットルームの名前を返します
        return self.name

    def set_host(self, user=None):
        if user is not None:
            # ルームのホストを設定します
            self.host = user

    def is_host(self, user=None):
        # 指定されたユーザーがルームのホストであるかどうかを判定します
        return user is not None and self.host.pk == user.pk

    def is_assigned(self, user=None):
        try:
            _ = self.participants.all().get(pk=user.pk)
            return True
        except User.DoesNotExist:
            return self.host == user
        except Exception:
            return False


# MessageManagerはMessageモデルのカスタムマネージャです
class MessageManager(models.Manager):
    def ordering(self, order='created_at'):
        # メッセージを指定された順序で並べ替えます
        return self.get_queryset().order_by(order)

# Messageモデルはチャットメッセージを表します
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField(gettext_lazy('Content'))
    created_at = models.DateTimeField(gettext_lazy('Created time'), default=timezone.now)

    # MessageManagerを使用してカスタムクエリを実行できるようにします
    objects = MessageManager()

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        # メッセージの所有者と内容の一部を結合して返します
        name = str(self.owner)
        text = self.content[:32]

        return f'{name}:{text}'

