import openai
from pydantic import BaseModel

openai.organization = 'org-XfVbiPgBfXfKP2hxyBIt6jvY'
openai.api_key = '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'


class Document(BaseModel):
    item: str = 'Sentencia If'


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programación de nivel universitario.
        E.G
        Asignar la sentencia o codigo que se necesita
        E.G
        Set, Get, If, while.
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
