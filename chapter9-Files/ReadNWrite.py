from pathlib import Path
p = Path('spam.txt')

p.write_text('Hello again')
print(p.read_text())
