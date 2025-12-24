import re

class LogicParser:
    @staticmethod
    def parse_response(raw_text: str) -> dict:
        """
        Mengubah output teks mentah menjadi dictionary terstruktur.
        """
        # Gunakan Regex
        label_match = re.search(r"\*\*(.*?)\*\*", raw_text)
        label = label_match.group(1) if label_match else "Unknown"
        
        # Ambil penjelasan
        explanation = "Tidak ada penjelasan tersedia."
        if "Penjelasan:" in raw_text:
            explanation = raw_text.split("Penjelasan:")[-1].strip()
        
        return {
            "label": label,
            "explanation": explanation,
            "is_fallacy": label.lower() != "tidak ada" and label.lower() != "unknown"
        }

logic_parser = LogicParser()