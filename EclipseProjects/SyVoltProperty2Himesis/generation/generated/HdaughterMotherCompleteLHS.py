from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HdaughterMother_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HdaughterMother_CompleteLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HdaughterMother_CompleteLHS, self).__init__(name='HdaughterMother_CompleteLHS', num_nodes=0, edges=[])
        
        # TODO Claudio: Levi, how to I get the name of the metamodel "FamiliesToPersons"? From the transformation model that the property refers to?
        
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__FamiliesToPersonsMM'
p2
aS'MoTifRule'
p3
a.""")
		self["MT_constraint__"] = """#===============================================================================
# This code is executed after the nodes in the LHS have been matched.
# You can access a matched node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression:
#    returning True enables the rule to be applied,
#    returning False forbids the rule from being applied.
#===============================================================================

return True
"""
        self["name"] = """"""
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'daughterMother')
        
        # Nodes that represent match classes
    	# match class Family(daughterMotherclass0) node
    	self.add_node()
    	self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		# TODO Claudio: Levi, were does this label come from? Is it the order in which the class appears inside the match model? Does it have to be unique?.
        self.vs[0]["MT_label__"] = """1"""  
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_dirty__"] = False
    	self.vs[0]["mm__"] = """MT_pre__Family"""  
    	self.vs[0]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[0]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[0]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'daughterMotherclass0')
    	# match class Member(daughterMotherclass1) node
    	self.add_node()
    	self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		# TODO Claudio: Levi, were does this label come from? Is it the order in which the class appears inside the match model? Does it have to be unique?.
        self.vs[1]["MT_label__"] = """2"""  
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_dirty__"] = False
    	self.vs[1]["mm__"] = """MT_pre__Member"""  
    	self.vs[1]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[1]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[1]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'daughterMotherclass1')
    	# match class Member(daughterMotherclass2) node
    	self.add_node()
    	self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		# TODO Claudio: Levi, were does this label come from? Is it the order in which the class appears inside the match model? Does it have to be unique?.
        self.vs[2]["MT_label__"] = """3"""  
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["MT_dirty__"] = False
    	self.vs[2]["mm__"] = """MT_pre__Member"""  
    	self.vs[2]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[2]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[2]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'daughterMotherclass2')
        
        
        #Nodes that represent apply classes
    	# match class Man(daughterMotherclass3) node
    	self.add_node()
    	self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		# TODO Claudio: Levi, were does this label come from? Is it the order in which the class appears inside the match model? Does it have to be unique?.
        self.vs[3]["MT_label__"] = """4"""  
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["MT_dirty__"] = False
    	self.vs[3]["mm__"] = """MT_pre__Man"""  
    	self.vs[3]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[3]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'daughterMotherclass3')
        
        
        
        # Nodes that represent the match associations of the property.
    	# match association Family--mother-->Member node
    	self.add_node()
    	self.vs[4]["MT_label__"] = """5"""
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["MT_dirty__"] = False
        # TODO Claudio: Levi, so suportas direct links? Nao suportas indirect links? Se suportares, e' preciso voltar 'a geracao do himesis da transformacao e suportar isso.
        self.vs[4]["mm__"] = """directLink_S"""
        self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'daughterMotherclass0assoc4daughterMotherclass2')
    	# match association Family--daughter-->Member node
    	self.add_node()
    	self.vs[5]["MT_label__"] = """6"""
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[5]["MT_dirty__"] = False
        # TODO Claudio: Levi, so suportas direct links? Nao suportas indirect links? Se suportares, e' preciso voltar 'a geracao do himesis da transformacao e suportar isso.
        self.vs[5]["mm__"] = """directLink_S"""
        self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'daughterMotherclass0assoc5daughterMotherclass1')
        
        
        
        # Add the edges
        self.add_edges([
    		(3,), # apply_class Man(daughterMotherclass3) -> backward_association
    		(,0), #  backward_association -> apply_class Family(daughterMotherclass0)
    		(0,4), # match_class Family(daughterMotherclass0) -> association mother
    		(4,2), # association mother  -> match_class Member(daughterMotherclass2)
    		(0,5), # match_class Family(daughterMotherclass0) -> association daughter
    		(5,1) # association daughter  -> match_class Member(daughterMotherclass1)
        ])
        
    	def eval_classtype1(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return True
        
        
        def eval_cardinality1(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return True

        
        def eval_name1(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return True
        
        
    	def eval_classtype2(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return True
        
        
        def eval_cardinality2(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return True

        
        def eval_name2(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return True
        
        
    	def eval_classtype3(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return True
        
        
        def eval_cardinality3(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return True

        
        def eval_name3(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return True
        
        
    	def eval_associationType5(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return attr_value == "mother"
	        
	        
    	def eval_associationType6(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return attr_value == "daughter"
	        
	        
        
        def constraint(self, PreNode, graph):
	        """
	            Executable constraint code. 
	            @param PreNode: Function taking an integer as parameter
	                            and returns the node corresponding to that label.
	        """
	        #===============================================================================
	        # This code is executed after the nodes in the LHS have been matched.
	        # You can access a matched node labelled n by: PreNode('n').
	        # To access attribute x of node n, use: PreNode('n')['x'].
	        # The given constraint must evaluate to a boolean expression:
	        #    returning True enables the rule to be applied,
	        #    returning False forbids the rule from being applied.
	        #===============================================================================
	        
	        return True
        
        