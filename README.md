# Concentric Decreasing Number Square

This Python program generates a square pattern of concentric numbers that decrease toward the center. The pattern is symmetric both vertically and horizontally, forming a beautiful number structure. The outermost layer contains the highest number (based on input), and the center contains the smallest number.

---

## Example Output

**Input:**  
```
9
```

**Output:**
```
9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  9
9  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  9
9  8  7  7  7  7  7  7  7  7  7  7  7  7  7  8  9
9  8  7  6  6  6  6  6  6  6  6  6  6  6  7  8  9
9  8  7  6  5  5  5  5  5  5  5  5  5  6  7  8  9
9  8  7  6  5  4  4  4  4  4  4  4  5  6  7  8  9
9  8  7  6  5  4  3  3  3  3  3  4  5  6  7  8  9
9  8  7  6  5  4  3  2  2  2  3  4  5  6  7  8  9
9  8  7  6  5  4  3  2  1  2  3  4  5  6  7  8  9
9  8  7  6  5  4  3  2  2  2  3  4  5  6  7  8  9
9  8  7  6  5  4  3  3  3  3  3  4  5  6  7  8  9
9  8  7  6  5  4  4  4  4  4  4  4  5  6  7  8  9
9  8  7  6  5  5  5  5  5  5  5  5  5  6  7  8  9
9  8  7  6  6  6  6  6  6  6  6  6  6  6  7  8  9
9  8  7  7  7  7  7  7  7  7  7  7  7  7  7  8  9
9  8  8  8  8  8  8  8  8  8  8  8  8  8  8  8  9
9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  9  9
````

---

## How It Works

- The square is of size `(2 * x - 1)`.
- Numbers form **concentric layers**.
- Each layer decreases by 1 as you move toward the center.
- It is symmetric on both X and Y axes.

---

## How to Run

Make sure you have Python installed, then run:

```bash
python concentric_decreasing_number_square.py
````

You’ll be prompted to enter a number (`x`), and the pattern will be printed in the terminal.

---

## Files

* `concentric_decreasing_number_square.py` – Main Python script.
* `README.md` – Documentation for the project.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Syed Hammad Hashmi**
