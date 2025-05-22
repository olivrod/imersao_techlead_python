from pathlib import Path
from unicodedata import name
from typing import Any, Generator
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from charindex import CharIndex, tokenize

STATIC_PATH = Path(__file__).parent.absolute() / "static"

app = FastAPI(
    title="Mojifinder Web",
    description="Search for Unicode characters by name.",
)


class CharName(BaseModel):
    char: str
    name: str


def init(app: FastAPI) -> None:
    app.state.index = CharIndex()
    app.state.form = (STATIC_PATH / "form.html").read_text()


init(app)


@app.get("/search", response_model=list[CharName])
async def search(q: str) -> Generator[dict[str, str], None, None]:
    words = tokenize(q)
    chars = sorted(app.state.index.search(words))
    return ({"char": c, "name": name(c)} for c in chars)

@app.get("/names", response_model=list[CharName])
async def names(q: str) -> list[dict[str, str]]:
    resultado = []
    for char in q:
        try:
            resultado.append({
                "char": char,
                "name": name(char)
            })
        except ValueError:
            resultado.append({
                "char": char,
                "name": "<no name found>"
            })
    return resultado

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def form() -> Any:
    return app.state.form


# no main funcion to run with uvicorn
# uvicorn mojifinder:app --reload --reload-include '*.html'
# http://127.0.0.1:8000/
