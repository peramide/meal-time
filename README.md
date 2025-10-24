### 🕒 Meal Time

**Meal Time** is a simple Python program that helps determine what meal corresponds to a given time of day.

Suppose you’re in a country where it’s customary to eat:

* 🍳 **Breakfast** between **7:00 and 8:00**
* 🥪 **Lunch** between **12:00 and 13:00**
* 🍲 **Dinner** between **18:00 and 19:00**

Wouldn’t it be nice if you had a program that could tell you what to eat when?

This program does exactly that!
It prompts the user to input a time in **24-hour format** (`#:##` or `##:##`), converts it into a floating-point representation of hours, and then determines if it’s breakfast, lunch, or dinner time.

---

### ⚙️ How It Works

The program consists of two main parts:

1. **`main()`** – Prompts the user for input and decides what meal time it is.
2. **`convert()`** – Converts the input time (as a string) into hours as a floating-point number.

   * Example: `"7:30"` → `7.5`

Each meal’s range is **inclusive**.
So, whether it’s `7:00`, `7:30`, or `8:00`, the program will say it’s **breakfast time**.

---

### 🧪 How to Test

You can test the program manually in your terminal.

Run:

```bash
python meal.py
```

Then try the following inputs:

| Input   | Expected Output |
| ------- | --------------- |
| `7:30`  | breakfast time  |
| `12:00` | lunch time      |
| `18:45` | dinner time     |
| `10:15` | *(no output)*   |

---

### 🧩 Example Output

```
What time is it? 7:45
breakfast time
```

```
What time is it? 15:00
```

*(no output — not meal time)*

---
