import google.genai as genai
from google.genai import types
from pydantic import ValidationError

from src.schemas import InvoiceDocument


def parse_unstructured_document(document_text: str) -> InvoiceDocument:
    """Ingests raw document text and returns a validated InvoiceDocument Pydantic instance."""
    
    client = genai.Client()

    system_instruction = (
        "You are an enterprise OCR data extraction engine. Extract all relevant transaction details "
        "from the unstructured text into the specified JSON schema. If an optional field is missing, "
        "set it to null. Ensure date strings are normalized to YYYY-MM-DD format."
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",  # Active model with fresh quota
        contents=f"Extract structured document data from this text:\n\n{document_text}",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            response_mime_type="application/json",
            response_schema=InvoiceDocument,
            temperature=0.0,
        ),
    )
    
    try:
        validated_data = InvoiceDocument.model_validate_json(response.text)
        return validated_data
    except ValidationError as error:
        print("CRITICAL: Extraction failed schema validation.")
        raise error