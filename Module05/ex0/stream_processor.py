from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: any) -> str:
        pass

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericPocessor(DataProcessor):
    def validate(self, data):
        try:
            if not isinstance(data, list):
                return False
            if len(data) == 0:
                return False
            for x in data:
                if not isinstance(x, (int, float)):
                    return False
            return True
        except ValueError:
            print("incorrect output")
        return True

    def process(self, data):
        if self.validate(data):
            print(f"Processing data: {data}")
            print("Validation: Numeric data verified")
        else:
            raise ValueError("bad processing unit")   
        len_data = len(data)
        sum_data = sum(data)
        avg_data = sum_data / len_data
        return f"Processed {len_data} numeric values, sum={sum_data}, avg={avg_data}"

    def format_output(self, result):
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data):
        try:
            if not isinstance(data, str):
                return False
            if len(data) == 0:
                return False
            return True
        except ValueError:
            print("incorrect output")
        return True

    def process(self, data):
        if self.validate(data):
            print(f"Processing data: {data}")
            print("Validation: Text data verified")
        else:
            raise ValueError("bad processing unit")   
        len_data = len(data)
        num_words = data.split(" ")
        return f"Processed text: {len_data} characters, {len(num_words)} words"

    def format_output(self, result):
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data):
        try:
            if not isinstance(data, str):
                return False
            if len(data) == 0:
                return False
            return True
        except ValueError:
            print("incorrect output")
        return True

    def process(self, data):
        if self.validate(data):
            print(f"Processing data: {data}")
            print("Validation: Text data verified")
        else:
            raise ValueError("bad processing unit")   
        len_data = len(data)
        num_words = data.split(" ")
        return f"Processed text: {len_data} characters, {len(num_words)} words"

    def format_output(self, result):
        return super().format_output(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("Initializing Numeric Processor...")
    Processor = NumericPocessor()
    Num_List = [1, 2, 3, 4, 5]
    first_output = Processor.process(Num_List)
    last_output = Processor.format_output(first_output)
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

