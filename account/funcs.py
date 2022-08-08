from .models import Player


def get_player(player_id):
    return Player.objects.get(id=player_id)
