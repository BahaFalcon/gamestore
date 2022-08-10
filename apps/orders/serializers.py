from rest_framework import serializers
from .models import Order, OrderItem
from apps.store.models import Game


class OrderItemSerializer(serializers.ModelSerializer):
    """Сериализатор для позиции"""
    game = serializers.PrimaryKeyRelatedField(
        queryset=Game.objects.all(),
        required=True)

    class Meta:
        model = OrderItem
        fields = ('game', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для заказа"""
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    positions = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'created', 'positions')

    def create(self, validated_data):
        """Метод создания заказа"""
        validated_data["customer"] = self.context["request"].user
        positions_data = validated_data.pop('positions')
        order = super().create(validated_data)

        raw_positions = []
        for position in positions_data:
            game = Game.objects.get(id=int(position["game"]))
            game.save()
            position = OrderItem(order=order,
                                 game=game,
                                 quantity=position["quantity"],
                                 price=position["price"]
                                 )
            raw_positions.append(position)
        OrderItem.objects.bulk_create(raw_positions)
        order.save()
        return order
