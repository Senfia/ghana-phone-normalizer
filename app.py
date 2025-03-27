import sys
import re

def normalize_phone_number(num):
    """Normalize phone number to 10-digit format starting with 0"""
    # Remove all non-digit characters
    cleaned = re.sub(r'[^\d]', '', num)
    
    # Handle numbers starting with 00233, 233, or +233
    if cleaned.startswith('00233'):
        cleaned = cleaned[5:]  # Remove 00233 prefix
    elif cleaned.startswith('233'):
        cleaned = cleaned[3:]  # Remove 233 prefix
    
    # Ensure number starts with 0 and has correct length
    if not cleaned.startswith('0'):
        cleaned = '0' + cleaned
    
    # Verify final length is 10 digits
    if len(cleaned) != 10:
        raise ValueError(f"Invalid number length after processing: {num} → {cleaned} (expected 10 digits)")
    
    return cleaned

def process_numbers():
    processed = set()  # Using a set to automatically handle duplicates
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            normalized = normalize_phone_number(line)
            processed.add(normalized)
        except ValueError as e:
            print(f"Skipping invalid number: {line} ({str(e)})", file=sys.stderr)
    
    # Output sorted results
    for num in sorted(processed):
        print(num)

if __name__ == "__main__":
    process_numbers()