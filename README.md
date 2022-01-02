# LarvaMatch

Find your larva or punk match.

## UI
TBD

## API (not started)
The API will allow you to specify a punk by token id to find a larva match, and vice versa.

### larvamatch/findmylarva/{punkTokenId}
Tries to find a larva that looks similar to the given punk.

### larvamatch/findmypunk/{larvaTokenId}
Tries to find a punk that looks similar to the given larva.

## Larva2Punk and Punk2Larva mappings (in progress)
A simple script will run periodically to traverse all the larvas by token id to find all their corresponding punks, and vice versa.  It will store metadata about the traversal for future use in a format similar to:
```json
{
    "larvaTokenId": 1966,
    "larvaImageUrl": "https://somedomain/larva/1966",
    "similarPunks": [
        {
            "punkTokenId": 9482,
            "punkImageUrl": "https://somedomain/punk/9482"
        },
        {
            "punkTokenId": 4382,
            "punkImageUrl": "https://somedomain/punk/4382"
        }
    ]
}
```

```bash
❯ python do_larva_match.py 
Finding punks that are similar to LarvaLad1966.jpg
ape-with-cap-cigarette.png is similar to LarvaLad1966.jpg
female-with-purple-cap.jpg is similar to LarvaLad1966.jpg
female-with-red-hair-mask.jpg is similar to LarvaLad1966.jpg
zombie-with-eye-patch.jpg is similar to LarvaLad1966.jpg
Found 4 similar punks
Finding punks that are similar to LarvaLad2828.jpg
female-with-purple-cap.jpg is similar to LarvaLad2828.jpg
Found 1 similar punks
```