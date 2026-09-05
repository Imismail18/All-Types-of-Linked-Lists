# Linked Lists

A Python implementation of multiple linked list types, including:

- Singly linked list with tail
- Singly linked list without tail
- Doubly linked list
- Circular linked list
- Circular doubly linked list

This project is designed as a learning and reference implementation for common linked list operations.

## Features

Each list supports core operations such as:

- append
- prepend
- insert
- remove
- pop
- search
- get
- display
- length checking
- empty-state checks
- looping throgh items

## Time Complexity

- `append()`: O(1)
- `prepend()`: O(1)
- `insert()`: O(n)
- `remove()`: O(n)
- `pop()`: O(n)
- `search()`: O(n)
- `get()`: O(n)
- `display()`: O(n)
- `__len__()`: O(1)
- `is_empty()`: O(1)
- `__contains__`: O(n)
- `__repr__`: O(n)
- `__iter__`: O(n)
  
## File

- `allLinkedLists.py` – contains all linked list classes and demo usage

## Usage

```python
from allLinkedLists import SinglyLinkedList, DoublyLinkedList, CircularLinkedList

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.prepend(5)

print(sll)      # displays the list
print(len(sll)) # prints 3
print(20 in sll) # True

# Doubly linked list example
 dll = DoublyLinkedList()
 dll.append(1)
 dll.append(2)
 print(dll)
```

## Example output

```python
Tail<->1<->2<->3<->Head
```

## Notes

- This repository focuses on understanding linked list behavior and pointer management.
- Each method includes comments explaining its purpose and time complexity.
- The file also includes a small demonstration section that runs when executed directly.

## Run locally

```bash
python3 allLinkedLists.py
```

## Project Structure

```text
Stack/
├── allLinkedLists.py
├── README.md
```

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## Author

Ismail - [@Imismail18](https://github.com/Imismail18)

## License

MIT License

Copyright (c) 2026 Ismail


This project is provided for educational purposes.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
