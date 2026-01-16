import json

def parse_bascii_to_json(bascii_block):
    """
    Parses a 5x11 B-ASCII matrix block into a 3D coordinate JSON.
    """
    lines = [line.strip() for line in bascii_block.strip().split('\n') if line.strip()]
    if len(lines) != 5:
        return {"error": "Invalid block height. Must be 5 lines."}

    # Anatomical height labels for the Y-axis
    height_map = {0: "head", 1: "shoulders", 2: "waist", 3: "knees", 4: "feet"}
    
    # Depth mapping for the Z-axis
    depth_values = {"o": 1.0, "-": 0.0, "|": -1.0}
    
    # Modifier mapping for flexion/rotation
    modifiers = {"v": "contracted", "\\": "flexed", "/": "flexed", "!": "tense"}

    movement_data = {"frame_data": {}}

    for y_idx, line in enumerate(lines):
        # Clean spacing to get the 11-column matrix
        chars = line.replace(" ", "")
        level_name = height_map[y_idx]
        movement_data["frame_data"][level_name] = []

        for x_idx, char in enumerate(chars):
            if char == ".":
