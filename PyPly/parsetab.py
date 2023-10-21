
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ERROR_TYPE FUNCTION NUMBER OPERATOR STANDARD_INFO SUGGESTION TYPE VALUE VARIABLE\n    message : message element\n             | element\n    \n    element : VARIABLE \n            | TYPE\n            | FUNCTION\n            | OPERATOR\n            | NUMBER\n            | STANDARD_INFO\n            | VALUE\n            | SUGGESTION\n            | ERROR_TYPE\n    '
    
_lr_action_items = {'VARIABLE':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[3,3,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,]),'TYPE':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[4,4,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,]),'FUNCTION':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[5,5,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,]),'OPERATOR':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[6,6,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[7,7,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,]),'STANDARD_INFO':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[8,8,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,]),'VALUE':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[9,9,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,]),'SUGGESTION':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[10,10,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,]),'ERROR_TYPE':([0,1,2,3,4,5,6,7,8,9,10,11,12,],[11,11,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,],[0,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'message':([0,],[1,]),'element':([0,1,],[2,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> message","S'",1,None,None,None),
  ('message -> message element','message',2,'p_message','parsing_mech.py',8),
  ('message -> element','message',1,'p_message','parsing_mech.py',9),
  ('element -> VARIABLE','element',1,'p_element','parsing_mech.py',20),
  ('element -> TYPE','element',1,'p_element','parsing_mech.py',21),
  ('element -> FUNCTION','element',1,'p_element','parsing_mech.py',22),
  ('element -> OPERATOR','element',1,'p_element','parsing_mech.py',23),
  ('element -> NUMBER','element',1,'p_element','parsing_mech.py',24),
  ('element -> STANDARD_INFO','element',1,'p_element','parsing_mech.py',25),
  ('element -> VALUE','element',1,'p_element','parsing_mech.py',26),
  ('element -> SUGGESTION','element',1,'p_element','parsing_mech.py',27),
  ('element -> ERROR_TYPE','element',1,'p_element','parsing_mech.py',28),
]
