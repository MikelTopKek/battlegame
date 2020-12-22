from units import *


def abstract_factory(factory: BattleUnit) -> None:
    unit1 = factory.create_base_unit()
    squad1 = factory.create_squad_unit()

    print(f"Ну-ка блядь выведи мне {unit1.abstract_func_base_unit()}")
    print(f"Ну-ка блядь выведи теперь {squad1.abstract_func_squad_unit()}")


if __name__ == "__main__":
    abstract_factory(BattleUnit)
