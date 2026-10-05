import heapq


def huffman_codes(freq):
    heap = [
        [weight, i, [ch, ""]]
        for i, (ch, weight) in enumerate(freq.items())
    ]

    heapq.heapify(heap)
    counter = len(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[2:]:
            pair[1] = "0" + pair[1]

        for pair in hi[2:]:
            pair[1] = "1" + pair[1]

        heapq.heappush(
            heap,
            [lo[0] + hi[0], counter] + lo[2:] + hi[2:]
        )

        counter += 1

    return {ch: code for ch, code in heap[0][2:]}


freq = {
    "a": 45,
    "b": 13,
    "c": 12,
    "d": 16,
    "e": 9,
    "f": 5
}

codes = huffman_codes(freq)

for ch in sorted(codes, key=lambda c: (len(codes[c]), c)):
    print(ch, freq[ch], codes[ch])

bits = sum(freq[c] * len(codes[c]) for c in freq)
fixed = sum(freq.values()) * 3

print("Huffman bits:", bits, "| fixed 3-bit bits:", fixed)
