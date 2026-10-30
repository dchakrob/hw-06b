# HW-06b: Triangle Testing

## Author
Danica Chakroborty

## Assignment Description
The purpose of this assignment is to develop and execute unit tests for an existing triangle classification program, identify defects using the test results, correct the defects in the program, and rerun the same test suite to verify the corrected implementation.

## Files
- `Triangle.py` - Contains the `classifyTriangle()` function used to classify triangles.
- `TestTriangle.py` - Contains the unit tests used to test the triangle classification program.

## Testing
The test suite contains 13 unit tests covering:
- Right triangles
- Equilateral triangles
- Isosceles triangles
- Scalene triangles
- Inputs that do not form a triangle
- Zero and negative side lengths
- Side lengths greater than 200
- Non-integer input

The tests were executed with:

`python -m unittest TestTriangle`

## Test Results

### Initial Test Run
The initial version of `Triangle.py` was tested before any defects were corrected.

- Tests executed: 13
- Tests passed: 4
- Tests failed: 9

### Final Test Run
After correcting the identified defects, the same 13-test suite was executed again.

- Tests executed: 13
- Tests passed: 13
- Tests failed: 0

The final test run completed successfully with all tests passing.
