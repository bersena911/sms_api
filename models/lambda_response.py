from dataclasses import dataclass, field


@dataclass
class LambdaResponse:
    headers: dict = field(default_factory=dict)
    isBase64Encoded: bool = True
    statusCode: int = 200
    body: str = ''
