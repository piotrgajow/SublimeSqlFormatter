
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '6ACBC367D524C623574FDA7D26721199'
    
_lr_action_items = {',':([11,12,17,22,23,24,25,26,],[15,-9,-10,-11,-12,-17,-16,-13,]),'FROM':([6,9,11,12,17,22,23,24,25,26,],[10,-5,-6,-9,-10,-11,-12,-17,-16,-13,]),'SELECT':([0,2,3,5,20,],[-18,4,-3,-2,-4,]),';':([13,14,21,24,25,],[20,-14,-15,-17,-16,]),'$end':([0,1,2,3,5,20,],[-18,0,-1,-3,-2,-4,]),'AS':([12,14,22,],[18,18,18,]),'.':([12,],[16,]),'TEXT':([4,7,8,10,12,14,15,16,18,19,22,],[-18,-8,12,14,-18,-18,-7,22,24,25,-18,]),'*':([4,16,],[9,23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'select_list':([4,],[6,]),'table_reference':([10,],[13,]),'input':([0,],[1,]),'select_list_x':([4,],[8,]),'alias':([12,14,22,],[17,21,26,]),'statement':([2,],[5,]),'select_item':([8,],[11,]),'statement_list':([0,],[2,]),'empty':([0,4,12,14,22,],[3,7,19,19,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> input","S'",1,None,None,None),
  ('input -> statement_list','input',1,'p_input','FormatSql.py',17),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list_recur','FormatSql.py',21),
  ('statement_list -> empty','statement_list',1,'p_statement_list_empty','FormatSql.py',28),
  ('statement -> SELECT select_list FROM table_reference ;','statement',5,'p_statement_select','FormatSql.py',32),
  ('select_list -> *','select_list',1,'p_select_list','FormatSql.py',36),
  ('select_list -> select_list_x select_item','select_list',2,'p_select_list','FormatSql.py',37),
  ('select_list_x -> select_list_x select_item ,','select_list_x',3,'p_select_list_x_recur','FormatSql.py',41),
  ('select_list_x -> empty','select_list_x',1,'p_select_list_x_empty','FormatSql.py',45),
  ('select_item -> TEXT','select_item',1,'p_select_item','FormatSql.py',49),
  ('select_item -> TEXT alias','select_item',2,'p_select_item','FormatSql.py',50),
  ('select_item -> TEXT . TEXT','select_item',3,'p_select_item','FormatSql.py',51),
  ('select_item -> TEXT . *','select_item',3,'p_select_item','FormatSql.py',52),
  ('select_item -> TEXT . TEXT alias','select_item',4,'p_select_item','FormatSql.py',53),
  ('table_reference -> TEXT','table_reference',1,'p_table_reference_name','FormatSql.py',57),
  ('table_reference -> TEXT alias','table_reference',2,'p_table_reference_name','FormatSql.py',58),
  ('alias -> empty TEXT','alias',2,'p_alias','FormatSql.py',62),
  ('alias -> AS TEXT','alias',2,'p_alias','FormatSql.py',63),
  ('empty -> <empty>','empty',0,'p_empty','FormatSql.py',67),
]
