import json
from pathlib import Path

INPUT_FILE = Path("data/all-ward.json")
OUTPUT_FILE = Path("data/wards.py")


DISTRICT_NAME_MAP = {
    "Tabora Urban": "Tabora Municipal",
}


def main():
    with INPUT_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    wards = []
    seen = set()

    for item in data:
        ward_name = item.get("name", {}).get("local")

        parent = item.get("parent", {})
        district_name = parent.get("name", {}).get("local")

        if not ward_name or not district_name:
            continue

        district_name = DISTRICT_NAME_MAP.get(
            district_name,
            district_name
        )

        key = (
            ward_name.strip().lower(),
            district_name.strip().lower()
        )

        if key not in seen:
            seen.add(key)

            wards.append({
                "name": ward_name.strip(),
                "district_name": district_name.strip(),
            })

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        file.write("wards = [\n")

        for ward in wards:
            file.write(
                f'    {{"name": "{ward["name"]}", '
                f'"district_name": "{ward["district_name"]}"}},\n'
            )

        file.write("]\n")

    print(f"✅ Generated {len(wards)} wards")
    print(f"📁 File: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()