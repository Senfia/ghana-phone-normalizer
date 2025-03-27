# 📱 Ghana Phone Number Normalizer

A lightweight Python utility to standardize Ghanaian phone numbers into a consistent 10-digit format.

## ✨ Features

- **Format Conversion**: Normalizes multiple phone number formats to standard 0XXXXXXXXX
- **Input Flexibility** handles:
  - Local numbers (`0541234567`, `541234567`)
  - International formats (`233...`, `+233...`, `00233...`)
- **Duplicate Removal**: Automatically filters out duplicate numbers
- **Validation**: Ensures all output numbers are valid 10-digit Ghanaian numbers
- **Error Reporting**: Identifies and reports invalid numbers

## 📦 Installation

```bash
git clone https://github.com/Senfia/ghana-phone-normalizer.git
cd ghana-phone-normalizer

```

## 🚀 Usage

### Basic Usage
```bash
python app.py < input.txt > clean_numbers.txt
```

### Interactive Mode

```bash
python app.py
> 233541234567
> 0541234567
> [Ctrl+D to process]
```

### Common Patterns
Process a CSV file:
```bash
cut -d',' -f1 contacts.csv | python app.py > clean_numbers.txt
```
Combine with other commands:
```bash
grep "Ghana" contacts.json | jq '.phone' | python app.py
```
