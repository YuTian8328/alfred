from ai2thor.controller import Controller
import torch
import logging
logging.basicConfig(level=logging.DEBUG)

c = Controller()
# c.start()
event = c.step(dict(action="MoveAhead"))
assert event.frame.shape == (300, 300, 3)
print(event.frame.shape)
print("Everything works!!!")

print("GPU available:", torch.cuda.is_available( ))