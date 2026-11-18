import typer

app = typer.Typer()

@app.command()
def main(indicators: list[str]):
    """Enrich one or more indicators."""
    for ioc in indicators:
        typer.echo(f"received: {ioc}")


if __name__ == "__main__":
    app()
