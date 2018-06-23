import argparse

blocks = ('\n' + open('foo.py').read()).split("\n'''\n")

code = True
for block in blocks:
    if code and block.strip():
        print('```python')
        print(block.strip())
        print('```')
    elif not code:
        print(block.strip())
        
    code = not code
