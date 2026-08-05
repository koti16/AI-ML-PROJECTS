# Document Parser: AI-Powered Structured Data Extractor

A fast, structured data extraction pipeline built with Python, Pydantic, and the Google Gemini API (`google-generativeai`). It converts unstructured invoices, receipts, and documents into strictly validated JSON schemas.

---

## 🚀 Features

- **Structured Extraction**: Extracts key vendor details, transaction metadata, and itemized line items from raw receipt/invoice files.
- **Type Safety & Schema Validation**: Uses **Pydantic** models to strictly validate field types (`quantity`, `unit_price`, `total_amount`, dates, etc.).
- **Flexible Data Pipeline**: Reads documents from `data/inputs/` and automatically formats and writes structured output to `data/outputs/`.
- **Environment Driven**: Clean configuration using `python-dotenv` for managing API keys and settings.

---

## 🛠️ Tech Stack & Dependencies

| Dependency | Purpose |
| :--- | :--- |
| `google-generativeai` | Gemini API client for multimodal visual-text inference |
| `pydantic` | Data validation, type enforcement, and JSON schema parsing |
| `python-dotenv` | Loads environment variables safely from `.env` |

---

## 📁 Directory Structure

```text
document-parser/
├── data/
│   ├── inputs/                 # Raw input files (receipts, invoices, images, PDFs)
│   │   └── sample_receipt.png
│   └── outputs/                # Formatted JSON output
│       └── parsed_invoice.json
├── src/
│   ├── __init__.py
│   ├── main.py                 # Pipeline execution entry point
│   ├── parser.py               # Gemini prompt logic & extraction handlers
│   └── schemas.py              # Pydantic models (Invoice, LineItem, Vendor)
├── .env                        # Local environment variables (API keys)
├── .env.example                # Template for required environment variables
├── .gitignore
├── README.md
└── requirements.txt            # Project dependencies