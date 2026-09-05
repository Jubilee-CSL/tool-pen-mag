"""Pick up the pen tool and draw a G-code file from the experiment directory.

    draw_deck                              # finds the pen slot itself
    draw_deck --tool 1                     # override when the machine is ambiguous
    draw_deck --gcode mark_slots.gcode
    draw_deck --env .env.mock
"""

import argparse
import sys

from science_jubilee.machine_session import MachineSession

from tool_pen_maag.tool import PenMaag


def _find_slot(tool_changer) -> int:
    """The slot the Duet loaded this plugin into."""
    slots = [i for i, t in tool_changer.tools.items() if isinstance(t, PenMaag)]
    if not slots:
        sys.exit(
            f"No slot is running {PenMaag.TOOL_KEY!r}. Check the M563 name in config.g, "
            "or pass --tool <n>."
        )
    if len(slots) > 1:
        sys.exit(f"{PenMaag.TOOL_KEY!r} is in several slots {slots} — pass --tool <n>.")
    return slots[0]


def run() -> None:
    parser = argparse.ArgumentParser(
        description="Pick up pen tool and draw from JUBILEE_EXPERIMENT_DIR."
    )
    parser.add_argument("--env", default=".env.hardware", help="env file to load")
    parser.add_argument(
        "--tool", type=int, default=None, help="pen tool index (default: auto-detect)"
    )
    parser.add_argument(
        "--gcode",
        default="plan_jubilee.gcode",
        help="G-code filename inside experiment dir",
    )
    args = parser.parse_args()

    session = MachineSession.from_env(args.env)

    exp_dir = session.experiment_dir
    if exp_dir is None:
        sys.exit("JUBILEE_EXPERIMENT_DIR is not set — cannot locate the G-code file.")

    gcode_path = exp_dir / args.gcode
    if not gcode_path.exists():
        sys.exit(f"G-code file not found: {gcode_path}")

    tool_idx = args.tool if args.tool is not None else _find_slot(session.tool_changer)

    nav = session.free_navigator
    print(f"Picking up tool {tool_idx} ...")
    nav.pickup_tool(tool_idx)

    print(f"Drawing {gcode_path} ...")
    nav.run_gcode_file(gcode_path)

    print("Parking tool ...")
    nav.park_tool()
    print("Done.")


if __name__ == "__main__":
    run()
