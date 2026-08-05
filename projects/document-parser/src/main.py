import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import ValidationError

from src.parser import parse_unstructured_document

# Load environment variables from .env file
load_dotenv()


def main():
    # Verify API key availability
    if not os.getenv("GEMINI_API_KEY"):
        raise ValueError("GEMINI_API_KEY not found. Ensure it is set in your .env file.")

    # Define project paths
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / "data" / "inputs" / "sample_receipt.txt"
    output_file = base_dir / "data" / "outputs" / "parsed_invoice.json"

    # Create dummy sample input if file does not exist
    if not input_file.exists():
        input_file.parent.mkdir(parents=True, exist_ok=True)
        sample_data = """
        ACME Hardware & Tech Ltd. - RECEIPT #INV-2026-9981
        Date of Sale: March 14, 2026
        Customer Account: TechCorp Inc.

        Purchased Items:
        1. Ergonomic Mesh Chair - Qty: 2 @ $250.00 each -> $500.00
        2. USB-C Docking Station - Qty: 1 @ $180.00 each -> $180.00
        3. Cat6 Ethernet Cable (10ft) - Qty: 4 @ $12.50 each -> $50.00

        ---------------------------------------------------------
        Subtotal: $730.00
        Sales Tax (8.5%): $62.05
        TOTAL DUE: $792.05

        Payment Method: Visa ending in 1104 [PAID IN FULL]
        """
        input_file.write_text(sample_data)
        print(f"Created sample input file at: {input_file}")

    print(f"Reading input document from: {input_file}")
    raw_text = input_file.read_text()

    try:
        # Run parsing pipeline
        parsed_doc = parse_unstructured_document(raw_text)

        # Save extracted JSON to outputs/
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(parsed_doc.model_dump_json(indent=2))

        print(f"Successfully saved output to: {output_file}\n")
        print("--- Extraction Summary ---")
        print(f"Vendor:      {parsed_doc.vendor_name}")
        print(f"Invoice ID:  {parsed_doc.invoice_number}")
        print(f"Grand Total: ${parsed_doc.total_amount}")

    except ValidationError as e:
        print(f"Validation Error: {e}")
    except Exception as e:
        print(f"Execution Error: {e}")


if __name__ == "__main__":
    main()