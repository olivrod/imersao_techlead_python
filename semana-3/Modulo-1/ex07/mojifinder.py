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
    code: str
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
    if not chars:
        chars = list(q)
    return ({"code": f"U+{ord(c):04X}", "char": c, "name": name(c)} for c in chars)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def form() -> Any:
    return app.state.form

# no main funcion to run with uvicorn
