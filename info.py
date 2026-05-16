class NiveauFormatError(Exception):
    """When bad file"""
    pass


def _parse_ints(line, expected_count, line_num):
    """To ignore the #."""
    line = line.split("#")[0].strip()
    if not line:
        raise NiveauFormatError(
            f"Ligne {line_num} vide ou seulement un commentaire, "
            f"{expected_count} valeurs attendues."
        )
    parts = line.split(",")
    if len(parts) != expected_count:
        raise NiveauFormatError(
            f"Ligne {line_num} : {expected_count} valeurs attendues, "
            f"{len(parts)} trouvée(s) → '{line}'"
        )
    result = []
    for i, p in enumerate(parts):
        p = p.strip()
        try:
            result.append(int(p))
        except ValueError:
            raise NiveauFormatError(
                f"Ligne {line_num}, valeur {i+1} : "
                f"entier attendu, '{p}' trouvé."
            )
    return result


def open_file(filename):
    """
    Add a file for a level.

    Awaited format :
        x,y                     # position of the character
        x1,y1,x2,y2            # the goal
        x1,y1,x2,y2            # 1st block
        ...                     # other blocks
    """
    # Readind the file
    try:
        with open(filename, "r", encoding="utf-8") as f:
            raw_lines = f.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"File couldn't be found : '{filename}'\n"
            f"Verify that the file exists/the path to the file is correct."
        )

    # Filter the empty and commented lines
    lines = []
    for raw in raw_lines:
        stripped = raw.split("#")[0].strip()
        if stripped:
            lines.append(raw)

    # Verifying if the file has enough lines
    if len(lines) < 3:
        raise NiveauFormatError(
            f"The file '{filename}' has only {len(lines)} line(s)."
            f"has to have at least 3 lines."
        )

    # character
    px, py = _parse_ints(lines[0], expected_count=2, line_num=1)


    personnage = {
        "position": (px, py),
        "velocity": (0, 0)
    }

    # the goal
    gx1, gy1, gx2, gy2 = _parse_ints(lines[1], expected_count=4, line_num=2)
    goal = (gx1, gy1, gx2, gy2)

    # blocks
    lst_blocs = []
    for i in range(2, len(lines)):
        bx1, by1, bx2, by2 = _parse_ints(lines[i], expected_count=4, line_num=i + 1)
        lst_blocs.append((bx1, by1, bx2, by2))

    return personnage, lst_blocs, goal

character, lst_blocks, goal = open_file("niveau_info.txt")