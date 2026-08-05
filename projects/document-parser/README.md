# Document Parser

A Python CLI tool that uses the **Google Gemini API** to extract structured data from raw receipt/invoice text files (OCR output) and saves the results as clean JSON.

---

## Project Structure

```
document-parser/
├── .env                  # API keys and environment variables (do not commit to Git)
├── .gitignore            # Ignores .env, venv/, __pycache__/
├── requirements.txt      # Project dependencies
├── README.md             # Project setup and run instructions
│
├── data/
│   ├── inputs/           # Raw text/OCR receipt files (.txt)
│   └── outputs/          # Generated JSON output files (.json)
│
└── src/
    ├── __init__.py       # Makes src a Python package
    ├── schemas.py        # Pydantic data models (InvoiceDocument, LineItem)
    ├── parser.py         # Gemini API call and extraction logic
    └── main.py           # CLI entry point to run the parser
```

---

## Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd document-parser
```

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the `.env` file and add your API key:

```bash
# Edit .env and set your Gemini API key
GEMINI_API_KEY=your_actual_api_key_here
```

> ⚠️ **Never commit `.env` to Git.** It is already listed in `.gitignore`.

Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## Usage

Place your raw receipt/invoice `.txt` files in `data/inputs/`, then run:

```bash
python src/main.py --input data/inputs/receipt.txt --output data/outputs/receipt.json
```

### Arguments

| Argument   | Description                                  | Default                  |
|------------|----------------------------------------------|--------------------------|
| `--input`  | Path to the input `.txt` file                | Required                 |
| `--output` | Path for the output `.json` file             | `data/outputs/out.json`  |

---

## Output Format

The parser extracts the following fields into a structured JSON:

```json
{
  "vendor_name": "Example Store",
  "invoice_number": "INV-001",
  "invoice_date": "2024-01-15",
  "total_amount": 99.99,
  "currency": "USD",
  "line_items": [
    {
      "description": "Item Name",
      "quantity": 2,
      "unit_price": 49.99,
      "total_price": 99.98
    }
  ]
}
```

---

## Dependencies

| Package              | Purpose                        |
|----------------------|--------------------------------|
| `google-generativeai`| Gemini API client              |
| `pydantic`           | Data validation and schemas    |
| `python-dotenv`      | Load environment variables     |
