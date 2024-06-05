class LLMStub:
    # This class is for testing purposes, returns nothing as output.

    def __init__(self) -> None:
        pass

    def generate(self, input_text: str) -> str:
        # This stub does nothing and returns a simple static response
        return f"Stub response for: {input_text}"