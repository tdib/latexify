import pyperclip

latex_map = {
  '{': '{',
  '}': '}',
  '¬': 'neg',
  '∧': 'wedge',
  '∨': 'vee',
  '⇒': 'Rightarrow',
  '⇔': 'Leftrightarrow',
  r'|=': 'vDash',
  'ϕ': 'phi',
  'ψ': 'psi',
  '->': 'Rightarrow',
  '~': 'neg',

}

def convert(initial=''):
  while True:
    if not initial:
      formatted = input('Type your latex: ')
    else:
      formatted = initial
      initial = ''

    # Replace unicode characters with their LaTeX counterparts
    for symbol, replacement_content in latex_map.items():
      replacement = f'\{replacement_content} '
      formatted = formatted.replace(symbol, replacement)

    # Copy to clipboard and print to the user
    pyperclip.copy(formatted)
    print(formatted)
    print()


if __name__ == '__main__':
  # User has not passed parameters to convert - prompt for their input
  convert()