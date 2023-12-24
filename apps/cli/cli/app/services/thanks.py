from pathlib import Path

from cli.app.utils import render_image, with_confirmation

base = Path(__file__).parent.parent.parent.parent / "assets"


@with_confirmation
def thanks(*_) -> None:
    print("Thanks to Oleh and Eduard for making this app a reality\n\n\n")
    oleh = base / "oleh.png"
    render_image(oleh)

    print("\n\n\n")
    eduard = base / "eduard.png"
    render_image(eduard)
