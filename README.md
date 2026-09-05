# Pen Machine Agency

A [science-jubilee](https://github.com/machineagency/science-jubilee) tool plugin
for the `tool_pen_maag` tool.

## Origin & credits

This plugin packages the **Passive Pen Tool** originally designed by
[Poofjunior](https://github.com/Poofjunior) as part of the Machine Agency's
Jubilee project.

- Original hardware & documentation: <https://jubilee3d.com/index.php?title=Passive_Pen_Tool>
- Original source in the mother Jubilee repo:
  [`machineagency/jubilee/tools/jubilee_tools/tools/passive_pen_tool`](https://github.com/machineagency/jubilee/tree/main/tools/jubilee_tools/tools/passive_pen_tool)
- Initial commit:
  [`1b494b0`](https://github.com/machineagency/jubilee/commit/1b494b025e7d625bbd5bdda35f135f7a4f22eba5)
  by [Poofjunior](https://github.com/Poofjunior)
  ([full commit history](https://github.com/machineagency/jubilee/commits?author=Poofjunior))

This repo re-packages the original design as a standalone `science-jubilee`
plugin so it can be discovered and used via entry points, without forking the
core.

## Install

```bash
pip install git+https://github.com/<owner>/tool-pen-maag
```

After installation, `ToolChanger` discovers `PenMaag` automatically � no changes
to the science-jubilee source are needed.

## Duet firmware setup (once per machine)

Fill in the parking-post coordinates in the `.g.template` files under `templates/`,
then upload `tpre{N}.g`, `tpost{N}.g`, and `tfree{N}.g` to `0:/sys/` on the Duet.

## Usage

```python
from science_jubilee.machine_session import MachineSession

session = MachineSession.from_env(".env.hardware")
tool = session.tool_changer.get_tool("tool_pen_maag")
tool.run(session.deck_navigator)
```

## Hardware

<!-- TODO: add BOM, STL links, assembly notes -->
