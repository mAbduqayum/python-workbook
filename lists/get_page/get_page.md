# Get Page

An online store shows search results page by page. Extract a single page of results.

## Task

- Create a function `get_page(items, page_num, page_size)` that takes a list of items, a page number, and a page size
- Return a new list containing only the items on that page

## Template:

```python
def get_page(items: list, page_num: int, page_size: int) -> list:
    pass


if __name__ == "__main__":
    # Test your function
    print(get_page(["a", "b", "c", "d", "e"], 1, 2))  # ['a', 'b']
    print(get_page(["a", "b", "c", "d", "e"], 2, 2))  # ['c', 'd']
    print(get_page(["a", "b", "c", "d", "e"], 3, 2))  # ['e']
```

## Note

- Pages are 1-indexed: page 1 holds the first `page_size` items
- The last page may have fewer than `page_size` items
- A page past the end returns `[]`
