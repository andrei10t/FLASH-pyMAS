from agent.agent import AgentEvent

_CONFIG = {
    # The serial UID.
    "serialVersionUID": 8405841078556036608,
    # The string separating elements of an endpoint address.
    "ADDRESS_SEPARATOR": "/",
    # The name associated with the content.
	"CONTENT": "content",
	 # The name associated with the elements of the source endpoint.
	"SOURCE_ELEMENT":"source-element", 
    #The name associated with the complete destination(s), in its(their) original form.
	"COMPLETE_DESTINATION":"destination-complete",
	#The name associated with the elements of one of the destinations.
	"DESTINATION_ELEMENT": "destination-element"
    }

class AgentWave(AgentEvent): 
    # For immutable static variable behavior, simply omit the property setter
   def __init__(self, config):
       self._config = config if config else _CONFIG
       
    @property
    def serialVersionUID(self):
        return self._serialVersionUID

