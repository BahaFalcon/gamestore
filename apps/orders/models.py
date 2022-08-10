from django.db import models
from apps.users.models import User
from apps.store.models import Game


class Order(models.Model):
    """Модель для заказов"""
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='Клиент')
    games = models.ManyToManyField(Game, verbose_name='Игры', through='OrderItem')
    created = models.DateTimeField(auto_now_add=True)
    total_price = models.PositiveIntegerField(default=0, verbose_name='Общая сумма')

    class Meta:
        ordering = ('created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def save(self, *args, **kwargs):
        self.total_price = sum(item.get_cost() for item in self.positions.all())
        # self.total_items = sum(item.quantity for item in self.positions.all())
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    """Модель для позиций"""
    order = models.ForeignKey(Order, related_name='positions', on_delete=models.CASCADE, verbose_name='Заказы')
    game = models.ForeignKey(Game, related_name='items', verbose_name='Игра', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.SmallIntegerField(default=1, null=False, verbose_name='Количество')

    def __str__(self):
        return self.game.name

    def get_cost(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        if self.price is None:
            self.price = self.game.price
        super(OrderItem, self).save(*args, **kwargs)

