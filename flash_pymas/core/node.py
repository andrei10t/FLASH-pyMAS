from flash_pymas.entity import EntityInterface
from typing import List
import logging

class Node(EntityInterface):
    def __init__(self, name=None):
        self._isRunning = False
        self._name = name
        self._registered_entities = dict()
         
    
    def register_entity(self, entity_name:str, entity:EntityInterface, entity_type:str):
        pass

    def start(self):
        logging.info(f"Starting node {self._name}...") 
        for entity in self._registered_entities:
            logging.info(f"Starting entity {entity}...")
            self._registered_entities[entity].start()
        self._isRunning=True
        logging.info(f"Node {self._name} started.") 

        
    

    # public boolean start()
	# {
	# 	li("Starting node [].", name);
	# 	for(Entity<?> entity : entityOrder) {
	# 		String entityName = entity.getName();
	# 		lf("starting entity []...", entityName);
	# 		if(entity.start()) {
	# 			lf("entity [] started successfully.", entityName);
	# 			if(getName() != null && (entity instanceof DefaultPylonImplementation))
	# 				messagingShard.register(getName());
	# 		}
	# 		else
	# 			le("failed to start entity [].", entityName);
	# 	}
	# 	isRunning = true;
	# 	sendStatusUpdate();
	# 	li("Node [] started.", name);
		
	# 	if(getName() != null && registerEntitiesToCentralEntity())
	# 		lf("Entities successfully registered to control entity.");
	# 	return true;
	# }
	
	# @Override
	# public boolean stop()
	# {
	# 	li("Stopping node [].", name);
	# 	LinkedList<Entity<?>> reversed = new LinkedList<>(entityOrder);
	# 	Collections.reverse(reversed);
	# 	for(Entity<?> entity : reversed) {
	# 		if(entity.isRunning())
	# 		{
	# 			lf("stopping an entity...");
	# 			if(entity.stop())
	# 				lf("entity stopped successfully.");
	# 			else
	# 				le("failed to stop entity.");
	# 		}
	# 	}
	# 	isRunning = false;
	# 	sendStatusUpdate();
	# 	li("Node [] stopped.", name);
	# 	return true;
	# }