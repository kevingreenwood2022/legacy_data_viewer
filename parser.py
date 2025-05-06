def parse_legacy_data(filepath):
    records = []
    with open(filepath, 'r') as f:
        for line in f:
            if len(line.strip()) == 0:
                continue
            # Example: fixed-width positions
            record = {
                'account': line[0:10].strip(),
                'date': line[10:20].strip(),
                'description': line[20:40].strip(),
                'amount': line[40:52].strip(),
                'status': line[52:].strip()
            }
            records.append(record)
    return records