from war import War
from storage import Storage
from unit import BattleUnit, SquadUnit


if __name__ == "__main__":
    war = War()
    war.generate()

    SquadUnit.attack(Storage.human_squads[18], Storage.human_squads[14], humans=Storage.humans)

    for x in Storage.human_squads:
        print(x)
    # BattleUnit.attack(Storage.humans[0], Storage.humans[1])
    #
    # BattleUnit.attack(Storage.humans[0], Storage.humans[1])

    # SquadUnit.attack(Storage.)

    # print(Storage.humans[0])
    # print(Storage.humans[1])
