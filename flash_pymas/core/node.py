import logging
from typing import List

from flash_pymas.entity import EntityInterface


class Node(EntityInterface):
    def __init__(self, name=None):
        self._running = False
        self._name = name
        self._registered_entities = dict()
        self._entity_order = []
    
    def register_entity(self, entity_name:str, entity:EntityInterface, entity_type:str):
		self._entity_order.append(entity)
		if entity_type not in self._registered_entities:
			self._registered_entities[entity_type] = []
			self._registered_entities[entity_type].append(entity)
			logging.info(f"Registered entity {entity_name} with type {entity_type} on node {self._name}.")

	def __enter__(self):
		self.start()
		return self
      
    def __exit__(self, exc_type, exc_value, exc_traceback):
       self.stop()

    def start(self):
		if not self.isRunning:
			logging.info(f"Starting node {self._name}...") 
			for entity in self._entity_order:
				logging.info(f"Starting entity {entity.getName}...")
				entity.start()
			self._running=True
			logging.info(f"Node {self._name} started.") 

	def stop(self):
		if self.isRunning:
			logging.info(f"Stopping node {self._name}...")
			for entity in self._entity_order[::-1]:
				logging.info(f"Stopping entity {entity.getName}...")
				entity.stop()
			self._running=False
			logging.info(f"Node {self._name} stopped.") 