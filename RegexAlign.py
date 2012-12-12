import sublime
import sublime_plugin
import re

# Takes the sublime.View and a sublime.Region object
# Return the array of strings, each element represents on line of the selection
def get_lines(view, selection_region):
  multiline_text = view.substr(selection_region)
  lines = re.split(r'(.*\n)', multiline_text, re.DOTALL)
  return lines

# Takes the delimiter string given by the user and splits the text string
# on the delimiter. It will also take into account any spaces before 
# the delimiter, which is the spacing that changes to cause text to 
# appear to align in columns.
# Returns and array in which each element represents the line split up 
# by the delimiter.
# Eg:
# split_on_delimiter(":a => :b", "=>")
# [":a", " =>", " :b"]
def split_on_delimiter(text, delimiter):
  return re.split(r'(%s)' % delimiter, text)

# Takes tokens, which is an array of arrays in which the first level of the
# array represents each line, and the second level represents the line split
# up by the delimiter, and the delimiter string itself.
# This method will join each line together, taking into account the spacing of 
# the delimiter, and produce a multi-line string to replace the origingal
# selection.
def merge_tokens(tokens, delimiter):
  result = []
  
  # Iterate until all sub arrays have been merged into the first sub-element
  # of each array.
  # Eg:
  # Start: [['a', ' =>', ' b'], ['cc', ' =>', ' dd, ee', ' =>', ' ff']]
  # Step1: [['a  => b'], ['cc => dd, ee', ' =>', ' ff']]
  # Step2: [['a  => b'], ['cc => dd, ee => ff']]
  #
  # Note how each array always starts with an odd number of element and
  # in the end all the arrays are reduced into the first element, so
  # that each array ends up with exacly one element.
  while max(map(len, tokens)) > 1:
    # We look at the first element of each aray to determine 
    # which is the longest
    max_length = max(map(len, zip(*tokens)[0]))
    
    # The first 3 tokens in the array (pre_delimiter, delimiter, post_delimiter)
    # and merge them into the first element, making sure to modify the 'delimiter'
    # element to have the correct number of spaces.
    for i, token in enumerate(tokens):
      if len(token) == 1: continue
      num_spaces = (max_length - len(token[0]))
      repl       = lambda match: (' ' * num_spaces + match.group(1))
      sub        = re.sub(r'\s*(%s)' % delimiter, repl, token[1])
      token      = [token[0] + sub + token[2]] + token[3:]
      tokens[i]  = token
  return "".join(sum(tokens, []))

class RegexAlignCommand(sublime_plugin.TextCommand):

  # The entry method for the function. Calls the UI input panel and delegates
  # to a callback when the user enters input.
  def run(self, view):
    window = sublime.active_window()
    window.show_input_panel("Regex", '=>', self.regex_align, None, None)
    # self.regex_align('=>') # debugging

  # Takes in the delimiter the user entered. Figures out which view in the 
  # editor is active and gets the selected text for that view. Calculates the
  # replacement text for that selection and replaces the text with the newly
  # aligned text. Works for each selection group in the view (in the case of 
  # multi-select).
  def regex_align(self, delimiter):
    delimiter = r'\s+%s' % delimiter # include preceding spaces
    view      = sublime.active_window().active_view()
    edit      = view.begin_edit()
    
    for selection in view.sel():
      lines = get_lines(view, selection)
      tokens = []

      for line in lines:
        token = split_on_delimiter(line, delimiter)
        tokens.append(token)

      replacement_text = merge_tokens(tokens, delimiter)
      view.replace(edit, selection, replacement_text)

    view.end_edit(edit)




