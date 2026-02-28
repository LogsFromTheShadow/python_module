from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or not data:
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Les données numériques sont invalides.")
        print(f"Traitement des données : {data}")
        print("Validation : Données numériques vérifiées")
        len_data = len(data)
        sum_data = sum(data)
        avg_data = sum_data / len_data
        return (f"Traité {len_data} valeurs numériques, "
                f"somme={sum_data}, moyenne={avg_data}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and bool(data)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Les données textuelles sont invalides.")
        print(f"Traitement des données : {data}")
        print("Validation : Données textuelles vérifiées")
        return (f"Texte traité : {len(data)} caractères, "
                f"{len(data.split())} mots")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Entrée de log invalide")

        print(f'Traitement des données : "{data}"')
        print("Validation : Entrée de log vérifiée")

        try:
            parts = data.split(":", 1)
            niveau = parts[0].strip()
            message = parts[1].strip()
            return f"{niveau} level detected: {message}"
        except Exception as e:
            return f"Error processing log: {e}"

    def format_output(self, result: str) -> str:
        texte_de_base = super().format_output(result)
        if "ERROR" in result:
            return texte_de_base.replace("Output: ", "Output: [ALERT] ")
        elif "INFO" in result:
            return texte_de_base.replace("Output: ", "Output: [INFO] ")
        return texte_de_base


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("Initializing Numeric Processor...")
    processor = NumericProcessor()
    num_list = [1, 2, 3, 4, 5]
    first_output = processor.process(num_list)
    last_output = processor.format_output(first_output)
    print(last_output)

    print()

    print("Initializing Text Processor..")
    text_proc = TextProcessor()
    proc = "Hello Nexus World"
    text_fout = text_proc.process(proc)
    text_lout = text_proc.format_output(text_fout)
    print(text_lout)

    print()

    print("Initializing Log Processor...")
    log = LogProcessor()
    log_msg = "ERROR: Connection timeout"
    log_pro = log.process(log_msg)
    log_lpro = log.format_output(log_pro)
    print(log_lpro)

    print()

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    demo_streams = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello world!"),
        (LogProcessor(), "INFO: System ready")
    ]

    for i, (processeur, donnee) in enumerate(demo_streams, start=1):
        try:
            resultat_brut = processeur.process(donnee)
            resultat_formate = processeur.format_output(resultat_brut)
            affichage_final = resultat_formate.replace("Output:",
                                                       f"Result {i}:")
            print(affichage_final)
        except Exception as e:
            print(f"Result {i}: Error - {e}")

    print("Foundation systems online. Nexus ready for advanced streams.")
