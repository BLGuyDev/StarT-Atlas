# Calculators and planners

This page lists the planning tools the pack community has published. Nothing here is generated: if you know a
better tool, open a pull request with the link and say where you verified it.

## Dynamo fuel and FE/t calculator

The official wiki links one calculator, from its *Dynamos* page (section "Calculators and Credits"):

- [Dynamo calculator (Google Sheet)](https://docs.google.com/spreadsheets/d/1n_muSKYPbVeTxJMGTGKpWlGKDjqaXruxRV3P3R-xkLA/edit?gid=616691493#gid=616691493)

It is meant for dynamo fuel consumption and FE/t. **Unverified:** the sheet was not opened for this project, so
check its numbers against the dynamo tooltip before sizing converters.

!!! note "No GregTech Planner link"
    A search of the official wiki and its source repository found no link to a general "GregTech Planner".
    This page will list one as soon as a public URL is confirmed.

## General advice

- **Read the tooltip, then the formula.** Upgrade kits, parallel hatches and overclocks change the real numbers.
  Use the tooltip of the machine you actually placed as the final word.
- **Size power by recipe EU/t, not by tier.** A recipe at 30 EU/t runs on an LV hatch even when the item is
  labelled HV. The machine panels in the chain pages show the tier ceiling (for example "up to 32 EU/t" for LV),
  not the recipe cost.
- **Overclock math:** each tier above the recipe tier doubles the speed and quadruples the EU/t. A spare hatch of a
  higher tier is only useful if the recipe really needs it.
- **Batch with parallels.** Where a multiblock accepts a parallel hatch, one machine can replace several; check the
  chain page for the recipe type.
- **Plan storage and buffers early.** Chains that run 24/7 need their fluids and drawers sized before the first run.
- **Keep a spreadsheet of your own.** Items per minute, machine counts and power draw per line are quick to total in
  any spreadsheet program and survive pack updates better than screenshots.

See also [Reference](reference.md) for tier voltages and [Build route](route.md) for the order of the lines.
