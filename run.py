from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.panel import Panel
from rich.text import Text
import requests
import time

console = Console()

def get_server_ip(server_input):
    if server_input.startswith("https://cfx.re/join/"):
        server_code = server_input
    elif server_input.startswith("cfx.re/join/"):
        server_code = f"https://{server_input}"
    else:
        server_code = f"https://cfx.re/join/{server_input}"

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
        ) as progress:
            task = progress.add_task("Connecting to server...", total=100)
            for _ in range(5):  
                time.sleep(0.2)
                progress.update(task, advance=20)

        response = requests.head(server_code, allow_redirects=True)
        citizenfx_url = response.headers.get("x-citizenfx-url", None)

        if citizenfx_url:
            ip_address = citizenfx_url.replace("http://", "").strip("/")
            console.print(
                Panel(
                    f"[bold cyan]Server URL:[/bold cyan] {server_code}\n[bold green]IP Address:[/bold green] {ip_address}",
                    title="[bold magenta]Success![/bold magenta]",
                )
            )
        else:
            console.print(
                Panel(
                    "[bold red]Error:[/bold red] Could not retrieve the server's IP address.\n"
                    "Make sure the server code or URL is correct and the server is online.",
                    title="[bold red]Failed[/bold red]",
                )
            )

    except requests.RequestException as e:
        console.print(
            Panel(
                f"[bold red]Error:[/bold red] Unable to fetch data.\nDetails: {e}",
                title="[bold red]Request Error[/bold red]",
            )
        )

if __name__ == "__main__":
    console.print(
        Panel(
            Text("CFX.re Server IP Finder", justify="center", style="bold white on blue"),
            subtitle="Made by [bold magenta]v2ce[/bold magenta]",
            expand=False,
        )
    )
    while True:
        server_input = console.input(
            "[bold yellow]Enter the server code or URL: [/bold yellow] "
        )
        get_server_ip(server_input)
        console.print("[bold magenta]Press Ctrl+C to exit or enter another server code/URL.[/bold magenta]")
