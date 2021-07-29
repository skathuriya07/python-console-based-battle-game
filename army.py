from stack_adt import ArrayStack
from queue_adt import CircularQueue

"""
This file contains an abstract Fighter class. 
The class has absstract methods which are defined in Soldier, Calvarya and Archer class.
It contains the Soldier, Calvarya and Archer classes
It contains an army class which assigns an army to a player according to 
their selection
"""
from abc import ABC, abstractclassmethod

class Fighter(ABC):
    """
    The fighter class is an abstract class.
    It has 2 class variables: life and experience, which are respective to each fighter
    Non abstract methods include:
    is_alive(self): which returns a boolean true if a fighter is alive, or false if the fighter is dead
    get_life(self): which returns the current int life of the fighter
    get_experience(self): which returns the current int experience of the fighter
    defend(self, attack_damage): which deducts int form the life of the fighter, depending on how much 
                           damage has been caused
    Abstract methods include:
    lose_life(self, lost_life)
    def get_speed(self)
    def gain_experience(self, gained_experience: int)
    def get_cost(self) 
    def get_attack_damage(self)
    def get_unit_type(self)
    def __str__(self) 
    """

    def __init__(self, life: int, experience: int) -> None:
        """
        The __init__ method initializes 2 class variables :
        life: which is an int representing the life of the fighter. 
              It has to be greater than or equal to zero.
        experience: which is an int representing the experince of the fighter. 
                    It has to be greater than or equal to zero.
        assertion: There are 2 assertions which assert that 
                   life and experience can not be negative
        return: None
        Complexity: O(1)
        """
        assert life >= 0, ("Life can not be negative")
        self.life = life
        assert experience >= 0, ("Experience can not be negative")
        self.experience = experience

    def is_alive(self) -> bool:
        """
        The is_alive method returns a booelan true or false indicating if the 
        fighter is alive or not respectively. The condition to be alive is that life 
        of the fighter should be greater than 0.
        return: true or false (boolean)
        Complexity: O(1)
        """
        if self.life >= 0:
            return True
        else:
            return False
    
    def lose_life(self, lost_life: int) -> None:
        """
        lose_life is an abstract method which will take 
        input: lost_life: int: which is the amount of lives lost
        return: None
        """
        self.life -= lost_life

    def get_life(self) -> int:
        """
        get_life method returns an int which os the life of the player
        return: int: life of the player
        Complexity: O(1)
        """
        return self.life

    def gain_experience(self, gained_experience: int) -> None:
        """
        gain_experience increases the experience of the player by the input 
        gained_experience given.
        input: gained_experience: int: the amount experience has to be increased by
        Complexity: O(1)
        """
        assert gained_experience >= 0, "Experience gain can not be negative"
        self.experience += gained_experience

    def get_experience(self) -> int:
        """
        get_experience method returns an int which is the experience of the player
        return: int: experience of player
        """
        return self.experience

    @abstractclassmethod
    def get_speed(self) -> int:
        """
        get_speed is an abstract method which will return the speed of the player
        return: int: which will be the speed of the player
        """
        pass

    @abstractclassmethod
    def get_cost(self) -> int:
        """
        get_cost is an abstract method which will return the cost of the player
        return: int: which will be the cost of the player
        """
        pass

    @abstractclassmethod       
    def get_attack_damage(self) -> int:
        """
        get_attack_damage is an abstract method which will return the damage caused by 
        the player on when they attack another player
        return: int: which will be the damage caused by the player
        """
        pass

    @abstractclassmethod
    def defend(self, damage: int) -> None:
        """
        defend method an abstract method which will changes the life of the player 
        depening on how much damage was caused.
        input: int: damage: the damage caused
        """
        pass
  

    @abstractclassmethod
    def get_unit_type(self) -> str:
        """
        get_unit_type is an abstract method which will return the unit type of the player
        return: str: which will be the unit type of the player
        """
        pass

    @abstractclassmethod
    def __str__(self) -> str:
        """
        __str__ is an abstract method which will return str describing the player
        return: str: which will be the str which is the description
        """
        pass



class Soldier(Fighter):
    """
    The Soldier class inherits the abstract Fighter class. 
    It contains all the abstract method of the Fighter class. They have been defined here.
    """
    def __init__(self) -> None:
        """
        The __init__ method of the Soldier class inherits the __init__ method of the 
        Fighter class to initialize life and experience of the Soldier.
        return: None
        complexity: O(1)
        """
        life = 3
        experience = 0
        Fighter.__init__(self, life, experience)

    def get_speed(self) -> int:
        """
        The get_speed method returns the speed of the Soldier.
        The speed of the soldier is 1 - experience
        return: int: speed of Soldier
        complexity: O(1)
        """
        return (1 - self.get_experience())

    def get_cost(self) -> int:
        """
        The get_cost method returns the cost of the Soldier player.
        The cost of the Soldier is 1
        return: int: cost of soldier
        complexity: O(1)
        """
        return 1
        
    def get_attack_damage(self) -> int:
        """
        The get_attack_damage method returns the damaged caused when Soldier
        attacks another player. For soldier, it is 1 + experience
        return: int: damage caused by the player
        complexity: O(1)
        """
        return (1 + self.get_experience())
    
    def defend(self, damage: int) -> None:
        """
        defend method changes the life of the player depening on how much 
        damage was caused.
        input: int: damage: the damage caused
        """
        assert damage >= 0, "damage should be greater than or equal to zero"
        if (damage > self.get_experience()):
            self.lose_life(1)

    def get_unit_type(self) -> str:
        """
        The get_unit_type method returns a string telling what the class unit is
        return: str: "Soldier"
        complexity: O(1)
        """
        return "Soldier"

    def __str__(self) -> str:
        """
        The __str__ method returns the string describing the Soldier's 
        life and experience
        return: str
        complexity: O(1)
        """
        msg ="Soldier's life = "
        msg += str(self.get_life())
        msg += " and experience = "
        msg += str(self.get_experience())
        return msg


class Archer(Fighter):
    """
    The Archer class inherits the abstract Fighter class. 
    It contains all the abstract method of the Fighter class. They have been defined here.
    """
    def __init__(self) -> None:
        """
        The __init__ method of the Archer class inherits the __init__ method of the 
        Fighter class to initialize life and experience of the Archer.
        return: None
        complexity: O(1)
        """
        life = 3
        experience = 0
        Fighter.__init__(self, life, experience)

    def get_speed(self) -> int:
        """
        The get_speed method returns the speed of the Archer.
        The speed of the Archer is 3
        return: int: speed of Archer
        complexity: O(1)
        """
        return 3

    def get_cost(self) -> int:
        """
        The get_cost method returns the cost of the Archer player.
        The cost of the Archer is 1
        return: int: cost of Archer
        complexity: O(1)
        """
        return 2
        
    def get_attack_damage(self) -> int:
        """
        The get_attack_damage method returns the damaged caused when Archer
        attacks another player. For Archer, it is 2*experience + 1
        return: int: damage caused by the player
        complexity: O(1)
        """
        return (2 * self.get_experience()) + 1
    
    def defend(self, damage: int) -> None:
        """
        defend method changes the life of the player depening on 
        how much damage was caused.
        input: int: damage: the damage caused
        """
        assert damage >= 0, "damage should be greater than or equal to zero"
        self.lose_life(1)

    def get_unit_type(self) -> str:
        """
        The get_unit_type method returns a string telling what the class unit is
        return: str: "Archer"
        complexity: O(1)
        """
        return "Archer"

    def __str__(self) -> str:
        """
        The __str__ method returns the string describing the Archer's 
        life and experience
        return: str
        complexity: O(1)
        """
        msg ="Archer's life = "
        msg += str(self.get_life())
        msg += " and experience = "
        msg += str(self.get_experience())
        return msg


class Cavalry(Fighter):
    """
    The Cavalry class inherits the abstract Fighter class. 
    It contains all the abstract method of the Fighter class. They have been defined here.
    """
    def __init__(self) -> None:
        """
        The __init__ method of the Cavalry class inherits the __init__ method of the 
        Fighter class to initialize life and experience of the Cavalry.
        return: None
        complexity: O(1)
        """
        life = 4
        experience = 0
        Fighter.__init__(self, life, experience)

    def get_speed(self) -> int:
        """
        The get_speed method returns the speed of the Cavalry.
        The speed of the Cavalry is 2 + experience
        return: int: speed of Cavalry
        complexity: O(1)
        """
        return 2 + self.get_experience()

    def get_cost(self) -> int:
        """
        The get_cost method returns the cost of the Cavalry player.
        The cost of the Cavalry is 1
        return: int: cost of Cavalry
        complexity: O(1)
        """
        return 3
        
    def get_attack_damage(self) -> int:
        """
        The get_attack_damage method returns the damaged caused when Cavalry
        attacks another player. For Cavalry, it is 1+experience
        return: int: damage caused by the player
        complexity: O(1)
        """
        return 1 + self.get_experience()
    
    def defend(self, damage: int) -> None:
        """
        defend method changes the life of the Cavalry depening on 
        how much damage was caused.
        input: int: damage: the damage caused
        """
        assert damage >= 0, "damage should be greater than or equal to zero"
        if damage > (self.get_experience()/2):
            self.lose_life(1)

    def get_unit_type(self) -> str:
        """
        The get_unit_type method returns a string telling what the class unit is
        return: str: "Cavalry"
        complexity: O(1)
        """
        return "Cavalry"

    def __str__(self) -> str:
        """
        The __str__ method returns the string describing the Cavalry's 
        life and experience
        return: str
        complexity: O(1)
        """
        msg ="Cavalry's life = "
        msg += str(self.get_life())
        msg += " and experience = "
        msg += str(self.get_experience())
        return msg



class Army():
    """
    The Army class creates an army for the player depending on the user input.
    It checks if the player is within budget and then creates army of their choice
    """
    BUDGET = 30 #class variable budget

    def __init__(self) -> None:
        """
        The __init__ method contains to instance variables:
        name: the name of the player: None
        force: the army formation (can bestack or queue): None
        """
        self.name = None
        self.force = None

    def __correct_army_given(self, soldiers: int, archers: int, cavalry: int) -> bool:
        """
        The __correct_army_given method checks if the army choice for 
        soldier, archer and calvary given by the player is within the budget 
        of 30 or not. It takes 3 inputs:
        soldiers: int: number of soldeirs chosen by the player to form army
        archers: int: number of archers chosen by the player to form army
        cavalry: int: number of cavalries chosen by the player to form army
        return: True if the selection is within the budget, False if not
        Complexity: O(1)
        """
        #calculating cost for each unit according to user choice of quantity
        #O(1) complexity:
        soldier_cost = Soldier().get_cost() * soldiers
        archer_cost = Archer().get_cost() * archers
        cavalry_cost = Cavalry().get_cost() * cavalry
        #total spending for the army user wants to make
        #O(1) complexity:
        spending = soldier_cost + archer_cost + cavalry_cost
        #O(1) complexity:
        if spending > self.BUDGET:
            return False
        else:
            return True

    def __assign_army(self, name: str, sold: int, arch: int, cav: int, formation: int = 0) -> None:
        """
        The  __assign_army method assignes the army to the player.
        For this task, the formation is set to 0 i.e., stack formation
        Since the in the battle, soldiers fight first, then archers and then Cavalries,
        The Cavalries are pushed first, then the archers and then the soldiers are pushed
        because stack is a FIFO data structure
        it takes 4 inputs:
        name: str: name of the player
        sold: int: number of soldiers to be in the army 
        arch: int: number of archers to be in the army 
        cav: int: number of cavalries to be in the army 
        formation: int = 0: indicating stack formation
        return: None
        Complexity:O(1) + O(sold) + O(arch) + O(cav)
                = O(sold + arch + cav)
                which is also O(total capacity of the initialized stack)
                or O(Number of units in army)
        """ 
        if formation == 0:
            # capacity of the stack is equal to the number of units to be in the army
            adt = ArrayStack(cav + sold + arch) #O(1)
            # pushing to stack, according to the number of sold, arch and cav given
            # by the user, into the stack adt
            for i in range(cav):    #O(cav)
                c = Cavalry()   #O(1)
                adt.push(c)     #O(1)
            for i in range(arch):  #O(arch)
                a = Archer()    #O(1)
                adt.push(a)     #O(1)
            for i in range(sold):   #O(sold)
                s = Soldier()   #O(1)
                adt.push(s)     #O(1)
        elif formation == 1:
            # capacity of the queue is equal to the number of units to be in the army
            adt = CircularQueue(cav + sold + arch)
            for i in range(sold):   #O(sold)
                s = Soldier()
                adt.append(s)
            for i in range(arch):   #O(arch)
                a = Archer()
                adt.append(a)
            for i in range(cav):    #O(cav)
                c = Cavalry()
                adt.append(c)
        # assigning instance variables
        self.force = adt    #O(1)
        self.name = name     #O(1)

    def choose_army(self, name: str, formation: int) -> None:
        """
        The choose_army method is what is used when the user gives input for their choices
        for the army. It keeps asking the user until right input is given.
        Right input means 1 integer inputs for soldier, archer and cavalry each
        those inputs should be greater than or equal to 0
        and the choice should be within budget
        input variables:
        name: str: name of the player
        formation: int: can be 0 or 1 depending on stack or queue
        return: None
        complexity:
        best case: O(1) + O(3) + O(1) + O(x)
            where x = Number of units chosen by user
        worst case: O(n) + O(3) + O(1) + O(x)
            where x = Number of units chosen by user
                  n = number of tries the user takes to choose correct army
        """
        correct_army = 0
        while correct_army != 1:    #best case: O(1), worst case: O(n) where n is the 
                                    #number of tries the user takes to choose correct army
            print("Player ", self.name, "choose your army as S A C ")
            print("Where S is the number of soldiers")
            print("      A is the number of archers")
            print("      C is the number of cavalries")
            try:
                s, a, c = (input("")).split(" ") #O(3)
                s = int(s)
                a = int(a)
                c = int(c)
                if self.__correct_army_given(s, a, c) == True: #O(1)
                    correct_army = 1    #O(1)
                    self.__assign_army(name, s, a, c, formation) #O(Number of units chosen by user)
                    print("Army formed")
                    correct_army = 1
                else:
                    print("Army could not be formed since you exceeded budget")

            except ValueError:
                print("Please input 3 integers")

    def __str__(self) -> str:
        """
        The __str__ method gives the description for each fighter present in the army
        retunrn: The text with description
        complexity:
        best case: O(1). When stack is empty
        worse case: O(n), where n = Number of units in the army
                    when stack is not empty
        """
        text = "" 
        if len(self.force) == 0:
            text = " " 
            return text #if empty, return empty string
        else:
            stack2 = ArrayStack(len(self.force))    #a stack to hold the fighters
            while len(self.force) != 0:     # O(Number of units in the army)
                unit = self.force.pop()     #O(1)
                text += unit.__str__()
                if len(self.force) != 0:
                    text += ","
                stack2.push(unit)           #pushing the fighter to our stack2
            while len(stack2) != 0:         # returning the fighters back to the force
                                            # O(Number of units in the army)
                unit = stack2.pop()
                self.force.push(unit)
        return text





