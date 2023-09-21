from missionPack import BattleRound


class PrimaryMission:
    def __init__(self, name: str, special_text: str, battle_rounds: dict[str, BattleRound]):
        self.name = name
        self.special_text = special_text
        self.battle_rounds = battle_rounds
