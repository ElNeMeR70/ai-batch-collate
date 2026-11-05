"""Dynamic Batch Collator"""

def collate_batch(sequences, pad_val=0):
    max_len = max(len(s) for s in sequences)
    padded = []
    masks = []
    for s in sequences:
        pad_len = max_len - len(s)
        padded.append(s + [pad_val] * pad_len)
        masks.append([1] * len(s) + [0] * pad_len)
    return padded, masks

if __name__ == "__main__":
    print("[RUN] Dynamic Batch Collator...")
    seqs = [[101, 2045], [101, 7592, 102]]
    pad, mask = collate_batch(seqs)
    print(f"[OK] Padded Batch: {pad} | Masks: {mask}")
