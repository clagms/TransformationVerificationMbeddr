from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HmotherFather_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HmotherFather_CompleteLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HmotherFather_CompleteLHS, self).__init__(name='HmotherFather_CompleteLHS', num_nodes=0, edges=[])
        
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
        self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFather')
        
        # Nodes that represent match classes
    	# match class Family(motherFatherclass0) node
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
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass0')
    	# match class Member(motherFatherclass1) node
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
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass1')
    	# match class Member(motherFatherclass2) node
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
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass2')
        
        
        #Nodes that represent apply classes
    	# match class CommunityRoot(motherFatherclass3) node
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
    	self.vs[3]["mm__"] = """MT_pre__CommunityRoot"""  
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
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass3')
    	# match class Man(motherFatherclass4) node
    	self.add_node()
    	self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_pre__classtype"] = """
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
        self.vs[4]["MT_label__"] = """5"""  
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["MT_dirty__"] = False
    	self.vs[4]["mm__"] = """MT_pre__Man"""  
    	self.vs[4]["MT_pre__classtype"] = """
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
		self.vs[4]["MT_pre__name"] = """
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
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass4')
    	# match class Woman(motherFatherclass5) node
    	self.add_node()
    	self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_pre__classtype"] = """
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
        self.vs[5]["MT_label__"] = """6"""  
        self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[5]["MT_dirty__"] = False
    	self.vs[5]["mm__"] = """MT_pre__Woman"""  
    	self.vs[5]["MT_pre__classtype"] = """
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
		self.vs[5]["MT_pre__name"] = """
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
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass5')
        
        
        
        # Nodes that represent the match associations of the property.
    	# match association Family--father-->Member node
    	self.add_node()
    	self.vs[6]["MT_subtypeMatching__"] = False
    	self.vs[6]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "father"
"""
    	self.vs[6]["MT_label__"] = """7"""
        self.vs[6]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[6]["MT_dirty__"] = False
        # TODO Claudio: Levi, so suportas direct links? Nao suportas indirect links? Se suportares, e' preciso voltar 'a geracao do himesis da transformacao e suportar isso.
        self.vs[6]["mm__"] = """directLink_S"""
        self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass0assoc6motherFatherclass1')
    	# match association Family--mother-->Member node
    	self.add_node()
    	self.vs[7]["MT_subtypeMatching__"] = False
    	self.vs[7]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "mother"
"""
    	self.vs[7]["MT_label__"] = """8"""
        self.vs[7]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[7]["MT_dirty__"] = False
        # TODO Claudio: Levi, so suportas direct links? Nao suportas indirect links? Se suportares, e' preciso voltar 'a geracao do himesis da transformacao e suportar isso.
        self.vs[7]["mm__"] = """directLink_S"""
        self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass0assoc7motherFatherclass2')
        
        
        # Nodes that represent the apply associations of the property.
    	# apply association CommunityRoot--has-->Man node
    	self.add_node()
    	self.vs[8]["MT_subtypeMatching__"] = False
    	self.vs[8]["MT_pre__associationType"] = """
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
    	self.vs[8]["MT_label__"] = """9"""
        self.vs[8]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["mm__"] = """MT_pre__directLink_T"""
        self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass3assoc8motherFatherclass4')
    	# apply association CommunityRoot--has-->Woman node
    	self.add_node()
    	self.vs[9]["MT_subtypeMatching__"] = False
    	self.vs[9]["MT_pre__associationType"] = """
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
    	self.vs[9]["MT_label__"] = """10"""
        self.vs[9]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[9]["MT_dirty__"] = False
        self.vs[9]["mm__"] = """MT_pre__directLink_T"""
        self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass3assoc9motherFatherclass5')
        
        
        #Nodes that represent match attributes
    	# has match attribute lastName(motherFatherclass0attribute0) node
    	self.add_node()
    	self.vs[10]["MT_subtypeMatching__"] = False
    	self.vs[10]["MT_label__"] = """11"""
    	self.vs[10]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[10]["mm__"] = """MT_pre__hasAttr_S"""
		self.vs[10]["MT_dirty__"] = False
        self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'hasmotherFatherclass0attribute0')
    	
    	# match attribute lastName(motherFatherclass0attribute0) node
    	self.add_node()
    	self.vs[11]["MT_subtypeMatching__"] = False
    	self.vs[11]["MT_label__"] = """12"""
    	self.vs[11]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[11]["mm__"] = """MT_pre__Attribute"""
		self.vs[11]["MT_dirty__"] = False
        self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass0attribute0')
    	# has match attribute firstName(motherFatherclass1attribute0) node
    	self.add_node()
    	self.vs[12]["MT_subtypeMatching__"] = False
    	self.vs[12]["MT_label__"] = """13"""
    	self.vs[12]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[12]["mm__"] = """MT_pre__hasAttr_S"""
		self.vs[12]["MT_dirty__"] = False
        self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'hasmotherFatherclass1attribute0')
    	
    	# match attribute firstName(motherFatherclass1attribute0) node
    	self.add_node()
    	self.vs[13]["MT_subtypeMatching__"] = False
    	self.vs[13]["MT_label__"] = """14"""
    	self.vs[13]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[13]["mm__"] = """MT_pre__Attribute"""
		self.vs[13]["MT_dirty__"] = False
        self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass1attribute0')
    	# has match attribute firstName(motherFatherclass2attribute0) node
    	self.add_node()
    	self.vs[14]["MT_subtypeMatching__"] = False
    	self.vs[14]["MT_label__"] = """15"""
    	self.vs[14]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[14]["mm__"] = """MT_pre__hasAttr_S"""
		self.vs[14]["MT_dirty__"] = False
        self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'hasmotherFatherclass2attribute0')
    	
    	# match attribute firstName(motherFatherclass2attribute0) node
    	self.add_node()
    	self.vs[15]["MT_subtypeMatching__"] = False
    	self.vs[15]["MT_label__"] = """16"""
    	self.vs[15]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[15]["mm__"] = """MT_pre__Attribute"""
		self.vs[15]["MT_dirty__"] = False
        self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass2attribute0')
        
        
        #Nodes that represent apply attributes
    	# has apply attribute name(motherFatherclass4attribute0) node
    	self.add_node()
    	self.vs[16]["MT_subtypeMatching__"] = False
    	self.vs[16]["MT_label__"] = """17"""
    	self.vs[16]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[16]["mm__"] = """MT_pre__hasAttr_T"""
		self.vs[16]["MT_dirty__"] = False
        self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'hasmotherFatherclass4attribute0')
    	
    	# apply attribute name(motherFatherclass4attribute0) node
    	self.add_node()
    	self.vs[17]["MT_subtypeMatching__"] = False
    	self.vs[17]["MT_label__"] = """18"""
    	self.vs[17]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[17]["mm__"] = """MT_pre__Attribute"""
		self.vs[17]["MT_dirty__"] = False
		self.vs[17]["MT_pre__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn attr_value = "name"\u000a
p1
.""")
        self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass4attribute0')
    	# has apply attribute name(motherFatherclass5attribute0) node
    	self.add_node()
    	self.vs[18]["MT_subtypeMatching__"] = False
    	self.vs[18]["MT_label__"] = """19"""
    	self.vs[18]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[18]["mm__"] = """MT_pre__hasAttr_T"""
		self.vs[18]["MT_dirty__"] = False
        self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'hasmotherFatherclass5attribute0')
    	
    	# apply attribute name(motherFatherclass5attribute0) node
    	self.add_node()
    	self.vs[19]["MT_subtypeMatching__"] = False
    	self.vs[19]["MT_label__"] = """20"""
    	self.vs[19]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[19]["mm__"] = """MT_pre__Attribute"""
		self.vs[19]["MT_dirty__"] = False
		self.vs[19]["MT_pre__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn attr_value = "name"\u000a
p1
.""")
        self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass5attribute0')
        
        
        # Add the edges
        self.add_edges([
    		(4,), # apply_class Man(motherFatherclass4) -> backward_association
    		(,1), #  backward_association -> apply_class Member(motherFatherclass1)
    		(5,), # apply_class Woman(motherFatherclass5) -> backward_association
    		(,2), #  backward_association -> apply_class Member(motherFatherclass2)
    		(0,10), # match_class Family(motherFatherclass0) -> has_match_attribute lastName (motherFatherclass0attribute0)
    		(10,11), #  has_match_attribute lastName (motherFatherclass0attribute0) -> match_attribute lastName (motherFatherclass0attribute0)
    		(1,12), # match_class Member(motherFatherclass1) -> has_match_attribute firstName (motherFatherclass1attribute0)
    		(12,13), #  has_match_attribute firstName (motherFatherclass1attribute0) -> match_attribute firstName (motherFatherclass1attribute0)
    		(2,14), # match_class Member(motherFatherclass2) -> has_match_attribute firstName (motherFatherclass2attribute0)
    		(14,15), #  has_match_attribute firstName (motherFatherclass2attribute0) -> match_attribute firstName (motherFatherclass2attribute0)
    		(4,16), # apply_class Man(motherFatherclass4) -> has_apply_attribute name (motherFatherclass4attribute0)
    		(16,17), #  has_apply_attribute name (motherFatherclass4attribute0) -> apply_attribute name (motherFatherclass4attribute0)
    		(5,18), # apply_class Woman(motherFatherclass5) -> has_apply_attribute name (motherFatherclass5attribute0)
    		(18,19), #  has_apply_attribute name (motherFatherclass5attribute0) -> apply_attribute name (motherFatherclass5attribute0)
    		(3,8), # apply_class CommunityRoot(motherFatherclass3) -> association has
    		(8,4), # association has  -> apply_class Man(motherFatherclass4)
    		(3,9), # apply_class CommunityRoot(motherFatherclass3) -> association has
    		(9,5), # association has  -> apply_class Woman(motherFatherclass5)
    		(0,6), # match_class Family(motherFatherclass0) -> association father
    		(6,1), # association father  -> match_class Member(motherFatherclass1)
    		(0,7), # match_class Family(motherFatherclass0) -> association mother
    		(7,2) # association mother  -> match_class Member(motherFatherclass2)
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
        
        
    	def eval_associationType7(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return attr_value == "father"
	        
	        
    	def eval_associationType8(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
	        return attr_value == "mother"
	        
	        
        
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
        
        