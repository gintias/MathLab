from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class ConstructionEvent:
    """
    Workspace-level event recording how a record was produced.
    """

    name: str
    input_records: list[int] = field(default_factory=list)
    output_record: Optional[int] = None
    protocol: Optional[str] = None
    guarantees: list[str] = field(default_factory=list)
    data: dict[str, Any] = field(default_factory=dict)


class ConstructionGraph:
    """
    Minimal directed index of construction dependencies.
    """

    def __init__(self):
        self.events: list[ConstructionEvent] = []
        self.inputs_to_events: dict[int, list[int]] = {}
        self.output_to_event: dict[int, int] = {}

    def add_event(self, event: ConstructionEvent) -> None:
        event_id = len(self.events)
        self.events.append(event)

        for record_id in event.input_records:
            self.inputs_to_events.setdefault(record_id, []).append(event_id)

        if event.output_record is not None:
            self.output_to_event[event.output_record] = event_id

    def history_of(self, record_id: int) -> list[ConstructionEvent]:
        event_id = self.output_to_event.get(record_id)
        if event_id is None:
            return []
        return [self.events[event_id]]

    def inputs_of(self, record_id: int) -> list[int]:
        history = self.history_of(record_id)
        if not history:
            return []
        return history[0].input_records.copy()

    def outputs_depending_on(self, record_id: int) -> list[int]:
        outputs = []
        for event_id in self.inputs_to_events.get(record_id, []):
            output_record = self.events[event_id].output_record
            if output_record is not None:
                outputs.append(output_record)
        return outputs
