#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bincrafters import build_template_default


if __name__ == "__main__":

    builder = build_template_default.get_builder(pure_c=False)

    print("Filtering shared Visual Studio builds...")
    builds_nb_before = len(builder.items)

    builder.builds = list(filter(lambda b: not (b.settings["compiler"] == "Visual Studio" and b.options["bullet3:shared"]), builder.items))

    builds_nb_after = len(builder.items)
    print("Removed {} builds.".format(builds_nb_before - builds_nb_after))

    builder.run()
