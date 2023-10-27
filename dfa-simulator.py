import sys

class DFA:
 def __init__(self, node_strs, alphabet):
  self.nodes = dict()
  self.initial_node = None

  for node_str in node_strs:
   new_node = Node(node_str, alphabet)
   self.nodes[new_node.name] = new_node
   if node_str[0] == '>': self.initial_node = new_node

 def run(self, string):
  current_node = self.initial_node

  for char in string:
   current_node = self.nodes[current_node.transitions[char]]
  return current_node

class Node:
 def __init__(self, string, alphabet):
  self.is_accept   = string[1] == 'F'
  self.name        = string[2]
  self.transitions = dict(zip(alphabet, string[3:].split()))

for arg in sys.argv[1:]:
 # Get input
 alph_str, *node_strs, input_string = arg.splitlines()

 # Parse input
 alphabet = alph_str.split()
 myDFA = DFA(node_strs, alphabet)
 input_string = input_string.strip('"')
 
 # Run DFA on given string
 result = myDFA.run(input_string)

 print(f"{result.name} {['Reject', 'Accept'][result.is_accept]}")
