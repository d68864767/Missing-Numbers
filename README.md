# Missing Numbers

## Description
In the city of Arrayville, every citizen is assigned a unique ID number from 1 to n. However, due to a system error, some of the ID numbers were erased from the city's database. The `findMissingIDs` function is designed to find out which ID numbers are missing.

## Functionality
The function `findMissingIDs(n, ids)` takes two parameters:
- `n`: an integer representing the total number of citizens in Arrayville.
- `ids`: an array of integers representing the existing ID numbers.

It returns an array of integers representing all the missing ID numbers, in ascending order.

## Usage
To use the function, simply import it and pass the total number of citizens and an array of existing IDs:

```python
from missing_numbers import findMissingIDs

missing_ids = findMissingIDs(5, [2, 3, 4, 5])
print(missing_ids)  # Output: [1]
```

## Constraints
- The function must not use more than O(n) space.
- The function must complete in less than O(n log n) time, avoiding the use of sorting algorithms that exceed this time complexity.

## Testing
The `test_missing_numbers.py` file contains a suite of unittests that can be run to verify the correctness of the `findMissingIDs` function.

To run the tests, execute the following command:

```bash
python test_missing_numbers.py
```

## Files
- `missing_numbers.py`: Contains the implementation of the `findMissingIDs` function.
- `test_missing_numbers.py`: Contains unittests for the `findMissingIDs` function.
- `README.md`: This file, which provides an overview of the project.
- `requirements.txt`: Lists the Python dependencies required for the project (if any).
- `.gitignore`: Specifies intentionally untracked files to ignore.

## Requirements
This project does not have any external dependencies and should run with standard Python 3.x.

## Author
This project is created by [Your Name].

## License
This project is licensed under the MIT License - see the LICENSE file for details.
