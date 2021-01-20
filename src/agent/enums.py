from enum import Enum, auto

class AutoName(Enum):
     # auto() => values are chosen by _generate_next_value_(), which can be overridden:
    def _generate_next_value_(name, start, count, last_values):
       return name

class AgentSequenceType(AutoName):
   
	#The components should be invoked in the order they were added.
    CONSTRUCTIVE = auto()
	# The components should be invoked in inverse order as to that in which they were added.
    DESTRUCTIVE = auto()
    # The components can be invoked in any order.
    UNORDERED = auto()

   