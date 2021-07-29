"""This file contains the Battle class which has methods to fight the battle
Here, stack is used for the army
"""
from army import Army, Soldier, Cavalry, Archer

class Battle:
    """
    The battle class has two methods:
    gladiatorial_combat: which takes the player names and calls the class method two    
                        conduct battle
     __conduct_combat: is the method that conducts the battle between to stak armies
     """
    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
        """
        The gladiatorial_combat function takes two inputs which are player names.
        It then forms the army for both of them, depending on their input choices
        by calling the choose_army method in Army class.
        Then it calls the class method __conduct_combat to conduct the battle which
        returs 0, 1, or 2 meaning that it is a draw, player 1 won or payer 2 won
        respectively.
        input parameters:
        player_one: str: name of player one
        player_two: str: name of player two
        return: int: 0 - draw
                     1 - player 1 won
                     2 - payer 2 won
        complexity:
        best case completely:  O(1) + O(3) + O(1) + O(x) + O(a) =  O(x) + O(a)
                              where, x = Number of units chosen by user
                                     a = length of army that is shorter
        worst case complexity: O(n) + O(3) + O(1) + O(x) +  O(a)
                               where, x = Number of units chosen by user
                                      a = length of army that is shorter
                                      n = number of tries the user takes to choose correct army                           
        """
        formation = 0
        army1 = Army()
        army2 = Army()
        # best case: O(1) + O(3) + O(1) + O(x)
        #     where x = Number of units chosen by user
        # worst case: O(n) + O(3) + O(1) + O(x)
        #     where x = Number of units chosen by user
        #           n = number of tries the user takes to choose correct army
        army1.choose_army(player_one, formation)
        army2.choose_army(player_two, formation)
        #complexity: O(a)
        #            where a = length of army that is shorter
        result = self.__conduct_combat(army1, army2, formation)
        if result == 1:
            print("Congractulations!!!")
            print("Player ", player_one, " has won!!")
            return 1
        elif result == 2:
            print("Congractulations!!!")
            print("Player ", player_two, " has won!!")
            return 2
        else:
            print("Well played!!")
            print("It is a draw!!")
            return 0
    
    def fairer_combat(self, player_one: str, player_two: str) -> int:
        """
        This method is called when the user wants the army formation to be as a queue
        It takes two inputs which are player names.
        It then forms the army for both of them, depending on their input choices
        by calling the choose_army method in Army class.
        Then it calls the class method __conduct_combat to conduct the battle which
        returs 0, 1, or 2 meaning that it is a draw, player 1 won or payer 2 won
        respectively.
        input parameters:
        player_one: str: name of player one
        player_two: str: name of player two
        return: int: 0 - draw
                     1 - player 1 won
                     2 - payer 2 won
        complexity:
        best case completely:  O(1) + O(3) + O(1) + O(x) + O(a) =  O(x) + O(a)
                              where, x = Number of units chosen by user
                                     a = length of army that is shorter
        worst case complexity: O(n) + O(3) + O(1) + O(x) +  O(a)
                               where, x = Number of units chosen by user
                                      a = length of army that is shorter
                                      n = number of tries the user takes to choose correct army                           

        """
        formation = 1
        army1 = Army()
        army2 = Army()
        # best case: O(1) + O(3) + O(1) + O(x)
        #     where x = Number of units chosen by user
        # worst case: O(n) + O(3) + O(1) + O(x)
        #     where x = Number of units chosen by user
        #           n = number of tries the user takes to choose correct army
        army1.choose_army(player_one, formation)
        army2.choose_army(player_two, formation)
        #complexity: O(a)
        #            where a = length of army that is shorter
        result = self.__conduct_combat(army1, army2, formation)
        if result == 1:
            print("Congractulations!!!")
            print("Player ,", player_one, " has won!!")
        elif result == 2:
            print("Congractulations!!!")
            print("Player ,", player_two, " has won!!")
        else:
            print("Well played!!")
            print("It is a draw!!")

    def __conduct_combat(self, army1: Army, army2: Army, formation: int) -> int:
        """
        This method conducts the combact with the army stacks or queue
        The ballte runs until either of the army is completely dead.
        the top most fighter is popped. Depending on their speed, they battle.
        If the speed of u1 is greater than speed of u2, u1 attacks first and 
        u2 defends. Depending on the attack damage and lives lost on defence,
        the fighters lose lives and once dead, they are discarded.
        If the speed of both units are equal, they both attack and defend together 
        input parameters:
        army1: Army: the army of player 1
        army2: Army: the army of player 2
        formation: int: 0 or 1, for stack and queue
        return: int: 0 - draw
                     1 - player 1 won
                     2 - payer 2 won
        complexity: O(n)
                    where n = length of army that is shorter
        """
        while (len(army1.force) != 0 and len(army2.force)) :    #O(length of army that is shorter)
            if formation == 0:
                # stack
                u1 = army1.force.pop()
                u2 = army2.force.pop()
            elif formation == 1:
                # queue
                u1 = army1.force.serve()
                u2 = army2.force.serve()
            if u1.get_speed() > u2.get_speed():
                # U1 attacks U2
                damage_by_u1 = u1.get_attack_damage()   #O(1)
                # U2 defendes and may lose life 
                u2.defend(damage_by_u1)  #O(1)
                if u2.is_alive():
                    #if U2 is alive, it will attack U1
                    damage_by_u2 = u2.get_attack_damage()    #O(1)
                    # U1 defendes
                    u1.defend(damage_by_u2)  #O(1)
            elif u2.get_speed() > u1.get_speed():
                # U2 attacks U1
                damage_by_u2 = u2.get_attack_damage()   #O(1)
                # U1 defendes and may lose life 
                u1.defend(damage_by_u2)  #O(1)
                if u1.is_alive():
                    #if U1 is alive, it will attack U2
                    damage_by_u1 = u1.get_attack_damage()    #O(1)
                    # U1 defendes
                    u1.defend(damage_by_u1)  #O(1)
            elif u1.get_speed() == u2.get_speed():
                #U1 and U2 attack
                damage_by_u1 = u1.get_attack_damage()    #O(1)
                damage_by_u2 = u2.get_attack_damage()    #O(1)
                #U1 and U2 defend
                u1.defend(damage_by_u1)  #O(1)
                u2.defend(damage_by_u2)  #O(1)
            # if both U1 nd U2 are alive
            if u1.is_alive() and u2. is_alive():     
                # Both lose a life
                u1.lose_life(1)  #O(1)
                u2.lose_life(1)  #O(1)
                #Both are push back into the stack
                if formation == 0:
                    # stack
                    army1.force.push(u1)    #O(1)
                    army2.force.push(u2)    #O(1)
                elif formation == 1:
                    # queue
                    army1.force.append(u1)  #O(1)
                    army2.force.append(u2)  #O(1)
            # if only U1 is alive
            elif u1.is_alive():
                # U1 gains experience and is pushed back into the stack
                u1.gain_experience(1)    #O(1)
                if formation == 0:
                    # stack
                    army1.force.push(u1)
                elif formation == 1:
                    # queue
                    army1.force.append(u1)
            # if only U2 is alive
            elif u2.is_alive():
                # U2 gains experience and is pushed back into the stack
                u2.gain_experience(1)    #O(1)
                if formation == 0:
                    # stack
                    army2.force.push(u2)
                elif formation == 1:
                    # queue
                    army2.force.append(u2)
        # after one of the army is completely is_empty means that the battle is Over
        # if army1 is empty, player 2 won
        if army1.force.is_empty() and not army2.force.is_empty():
            return 2
        # if army2 is empty, player 1 won
        elif army2.force.is_empty() and not army1.force.is_empty():
            return 1
        # if army1 and army2 are empty, it is a draw
        else:
            return 0



if __name__ == '__main__':
    battle = Battle()
    print("Welcome to the game!")
    print("Please insert the name of player 1")
    player_one = input("")
    print("Please insert the name of player 2")
    player_two = input("")
    print("Choose your army fomration:")
    correct_formation = 0
    while correct_formation != 1:
        try:
            print("For stack, choose 0")
            print("For queue, choose 1")
            formation = int(input())
            if formation == 0:
                correct_formation = 1
                battle.gladiatorial_combat(player_one, player_two)
            if formation == 1:
                correct_formation = 1
                battle.fairer_combat(player_one, player_two)
        except ValueError:
            print("Please enter either 0 or 1")


