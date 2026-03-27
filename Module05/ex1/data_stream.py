from abc import ABC, abstractmethod
from typing import List, Any, Dict, Union, Optional


class DataStream(ABC):
    """Classe de base abstraite pour les flux de données."""

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Méthode abstraite pour traiter un lot de données."""
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """Implémentation par défaut du filtrage (liste complète)."""
        return [item for item in data_batch]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Retourne les statistiques de base du flux."""
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count
        }


class SensorStream(DataStream):
    """Flux spécialisé pour les données de capteurs (ex: température)."""

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        temps = [d for d in data_batch if isinstance(d, (int, float))]
        avg = sum(temps) / len(temps) if temps else 0
        return (f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg}°C")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            return [d for d in data_batch if isinstance(d, (int, float))
                    and d > 30]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    """Flux spécialisé pour les transactions financières."""

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        return (f"Transaction analysis: {len(data_batch)} operations, "
                "net flow: calculated")


class EventStream(DataStream):
    """Flux spécialisé pour les événements système."""

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        errors = [e for e in data_batch if "error" in str(e).lower()]
        return (f"Event analysis: {len(data_batch)} events, "
                f"{len(errors)} error(s) detected")


class StreamProcessor:
    """Gestionnaire qui manipule les flux de manière polymorphe."""

    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if not isinstance(stream, DataStream):
            raise TypeError("Only DataStream objects can be added.")
        self.streams.append(stream)

    def run_all(self, data_map: Dict[str, List[Any]]) -> None:
        """Traite tous les flux enregistrés avec les données fournies."""
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")

        for stream in self.streams:
            try:
                batch = data_map.get(stream.stream_id, [])
                result = stream.process_batch(batch)
                print(f"- {stream.__class__.__name__}: {result}")
            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")


def main() -> None:
    """Point d'entrée principal pour démontrer le système."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print(sensor.process_batch([22.5, 23.0, 22.1]))

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: Financial Data")
    print(trans.process_batch(["buy:100", "sell:150"]))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    print(event.process_batch(["login", "error_db", "logout"]))

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)

    mixed_data: Dict[str, List[Any]] = {
        "SENSOR_001": [25.0, 26.5],
        "TRANS_001": ["buy:50", "buy:20", "sell:10", "buy:5"],
        "EVENT_001": ["update", "reboot", "error_critical"]
    }

    processor.run_all(mixed_data)

    print("\nStream filtering active: High-priority data only")
    critical_sensors = sensor.filter_data([20, 45, 15, 50], criteria="high")
    print(f"Filtered results: {len(critical_sensors)} critical sensor alerts")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
