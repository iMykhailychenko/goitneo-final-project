def parse_input(user_input: str) -> list[str]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
